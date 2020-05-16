import setuptools

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
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
