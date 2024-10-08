"""Setup script for the package."""

import setuptools

VERSION = "0.0.9"

with open("README.md", "r") as file_object:
    LONG_DESCRIPTION = file_object.read()

setuptools.setup(
    name="colortimelog",
    version=VERSION,
    author="Quan Wang",
    author_email="quanw@google.com",
    description="A util for logging the time elapsed for a task.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/wq2012/colortimelog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
