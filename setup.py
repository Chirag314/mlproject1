from setuptools import setup, find_packages
from typing import List

CONST = "-e ."


def get_requirements(file_path: str) -> list[str]:
    """This function returns the list of requirements"""
    requirements = []
    with open(file_path, "r") as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if CONST in requirements:
            requirements.remove(CONST)
    return requirements


setup(
    name="mlproject1",
    version="0.1",
    author="Chirag",
    author_email="chirag.d314@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
