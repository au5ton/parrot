import os
import setuptools
from setuptools import Extension
import urllib.request
import shutil
from zipfile import ZipFile
from pathlib import Path

# Prepare build directory
BUILD_DIR = Path('./build')
BUILD_DIR.mkdir(exist_ok=True)

# Download C-lang dependency
with urllib.request.urlopen("https://github.com/Tiiffi/mcrcon/archive/master.zip") as response, open(BUILD_DIR / 'master.zip', 'wb') as outfile:
  shutil.copyfileobj(response, outfile)

# Unzip repo
with ZipFile(BUILD_DIR / 'master.zip', 'r') as zip:
  zip.extractall(BUILD_DIR)

with open("README.md", "r") as fh:
    long_description = fh.read()

thing = setuptools.setup(
    name="parrot-mc",
    version="0.0.1",
    author="Austin Jackson",
    author_email="austinjckson@gmail.com",
    description="Exposes MCRCON as a REST API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/au5ton/parrot",
    packages=setuptools.find_packages(),
    ext_modules=[
      Extension('mcrcon', [
          str(BUILD_DIR / 'mcrcon-master' / 'mcrcon.c')
        ])
    ],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

print('------------------------')
print(thing)
print(thing.has_c_libraries())


# Cleanup
shutil.rmtree(BUILD_DIR / 'mcrcon-master')
os.remove(BUILD_DIR / 'master.zip')