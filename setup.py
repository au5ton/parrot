# import os
import setuptools
# import urllib.request
# import json
# import shutil
# import tarfile
# from zipfile import ZipFile
# from pathlib import Path
# import platform

# Prepare build directory
# BUILD_DIR = Path('./build/tmp')
# BUILD_DIR.mkdir(parents=True, exist_ok=True)

# Short-hand for downloading file
# def downloadFile(url: str, outpath: str) -> None:
#     # Download C-lang dependency
#     with urllib.request.urlopen(url) as response, open(outpath, 'wb') as outfile:
#         shutil.copyfileobj(response, outfile)
#         # returns for convenience
#         return str(outpath)


# # Get release information for binary dependent
# with urllib.request.urlopen("https://api.github.com/repos/Tiiffi/mcrcon/releases/latest") as response:
#     manifest = json.loads(response.read().decode('utf-8'))
#     # Iterates over every release asset
#     for release in manifest["assets"]:
#         # Downloads:
#         # 'https://github.com/Tiiffi/mcrcon/releases/download/v0.7.1/mcrcon-0.7.1-linux-x86-32.tar.gz'
#         # ->
#         # 'mcrcon-0.7.1-linux-x86-32.tar.gz'
#         asset = downloadFile(
#             release["browser_download_url"], BUILD_DIR / release["name"])
#         # Extract .tar, if it is one
#         if asset.endswith(".tar.gz"):
#             with tarfile.open(asset) as tar:
#                 tar.extractall(Path(asset).parent)
#         if asset.endswith(".zip"):
#             with ZipFile(asset) as zip:
#                 zip.extractall(Path(asset).parent)

# Prepare mcrcon bundle
# drivers = []
# # Prepare linux64
# src = str(next(BUILD_DIR.glob('*-linux-*-64*/mcrcon')))
# dst = f'{src}64'
# shutil.copy(src, dst)
# drivers += [dst]
# # Prepare linux32
# src = str(next(BUILD_DIR.glob('*-linux-*-32*/mcrcon')))
# dst = f'{src}32'
# shutil.copy(src, dst)
# drivers += [dst]
# # Prepare win32
# drivers += [str(next(BUILD_DIR.glob('*windows*/*.exe')))]


# # Generate package metadata
# with open('MANIFEST.in', 'w') as f:
#     for d in drivers:
#         f.write(f'{d}\n')
#     f.write('\n')

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="parrot_mc",
    version="0.0.1",
    author="Austin Jackson",
    author_email="austinjckson@gmail.com",
    description="Exposes MCRCON as a REST API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/au5ton/parrot",
    packages=setuptools.find_packages(),
    scripts=['parrot/scripts/parrot-mc.py'],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# # Cleanup
# shutil.rmtree(BUILD_DIR / 'mcrcon-master')
# os.remove(BUILD_DIR / 'master.zip')
