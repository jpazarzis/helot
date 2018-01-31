#!/usr/bin/env python
import os
from setuptools import find_packages, setup


def get_requirements(requirements_file=None):
    """
    Return the contents of the 'requirements.txt' (without the comments)
    """
    if not requirements_file:
        requirements_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "requirements.txt"))

    requirements = []
    for line in open(requirements_file).readlines():
        # Get rid of comments and empty lines
        if line.find("#") != -1:
            line = line[:line.find("#")]
        line = line.strip()
        if not line:
            continue

        # If we got "-r ..." , try to recursively get the requirements
        # for that file...
        if line.startswith("-r ") or line.startswith("-r\t"):
            nested_requirements_file = line[3:].strip()
            requirements += get_requirements(nested_requirements_file)
            continue
        else:
            # Add the requirement
            requirements.append(line)
    return requirements


setup(
    name="helot",
    description="Commonly reused functionality.",
    long_description="Impements configuration and mysql wrapper.",
    url="http://www.github.com/jpazarzis",
    author="John Pazarzis",
    install_requires=get_requirements(),
    packages=find_packages(),
    version='1.0.0',
)
