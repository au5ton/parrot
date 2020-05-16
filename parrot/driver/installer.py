import os
import stat
import urllib.request
import json
import shutil
import tarfile
from zipfile import ZipFile
from pathlib import Path
from typing import List
import platform

# Short-hand for downloading file
def downloadFile(url: str, outpath: str) -> None:
  with urllib.request.urlopen(url) as response, open(outpath, 'wb') as outfile:
    shutil.copyfileobj(response, outfile)
    # returns for convenience
    return str(outpath)


def installGithubReleases(BUILD_DIR: Path) -> None:
  # Get release information for binary dependent
  with urllib.request.urlopen("https://api.github.com/repos/Tiiffi/mcrcon/releases/latest") as response:
    manifest = json.loads(response.read().decode('utf-8'))
    # Iterates over every release asset
    for release in manifest["assets"]:
      # Downloads:
      # 'https://github.com/Tiiffi/mcrcon/releases/download/v0.7.1/mcrcon-0.7.1-linux-x86-32.tar.gz'
      # ->
      # 'mcrcon-0.7.1-linux-x86-32.tar.gz'
      asset = downloadFile(
        release["browser_download_url"], BUILD_DIR / release["name"])
      # Extract .tar, if it is one
      if asset.endswith(".tar.gz"):
        with tarfile.open(asset) as tar:
          tar.extractall(Path(asset).parent)
      if asset.endswith(".zip"):
        with ZipFile(asset) as zip:
          zip.extractall(Path(asset).parent)

def linkExecutables(BUILD_DIR: Path) -> List[str]:
  # Prepare mcrcon bundle
  drivers = []
  # Prepare linux64
  src = str(next(BUILD_DIR.glob('*-linux-*-64*/mcrcon')))
  dst = f'{src}64'
  shutil.copy(src, dst)
  drivers += [dst]
  # Prepare linux32
  src = str(next(BUILD_DIR.glob('*-linux-*-32*/mcrcon')))
  dst = f'{src}32'
  shutil.copy(src, dst)
  drivers += [dst]
  # Prepare win32
  drivers += [str(next(BUILD_DIR.glob('*windows*/*.exe')))]

  # Copy to known location
  for f in drivers:
    shutil.copy(f, BUILD_DIR)
    p = BUILD_DIR / Path(f).name
    st = os.stat(p)
    os.chmod(p, st.st_mode | stat.S_IEXEC)

  # seldom used
  return drivers

def install() -> None:
  # Prepare build directory
  BUILD_DIR = getDefaultInstall()
  BUILD_DIR.mkdir(exist_ok=True)

  # Inform the user
  print(f'Installing https://github.com/Tiiffi/mcrcon to {BUILD_DIR}')

  # Run procedures
  installGithubReleases(BUILD_DIR)
  linkExecutables(BUILD_DIR)

  print('Install of mcrcon has finished')

def checkExists() -> bool:
  BUILD_DIR = getDefaultInstall()
  return BUILD_DIR.exists()

def getDefaultInstall() -> Path:
  return Path.home() / '.parrot-mc'

def getBinary() -> str:
  BUILD_DIR = getDefaultInstall()
  # Determine the correct platform for the driver
  system = platform.system()
  arch, _ = platform.architecture()
  if system == 'Linux':
    if arch == '64bit':
      return (BUILD_DIR / 'mcrcon64').resolve()
    else:
      return (BUILD_DIR / 'mcrcon32').resolve()
  if system == 'Windows':
    return (BUILD_DIR / 'mcrcon.exe').resolve()
  if system == 'Darwin':
    return (BUILD_DIR / 'mcrcon64').resolve()
  
  # if all else fails
  return (BUILD_DIR / 'mcrcon64').resolve()