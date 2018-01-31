#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="helot",
    description="Commonly reused functionality.",
    long_description="Impements configuration and mysql wrapper.",
    url="http://www.github.com/jpazarzis",
    author="John Pazarzis",
    install_requires=[
        "pyyaml",
        "mysqlclient",
        "coverage"
    ],
    packages=find_packages(),
    version='1.0.1',
)
