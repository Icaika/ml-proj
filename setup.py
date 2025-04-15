from setuptools import setup, find_packages
from typing import List

def get_requirements(path: str) -> List[str]:
    requirements = []
    with open(path) as file_obj:
        requirements = open(path , 'r').read().splitlines()
        if '-e .' in requirements:
            requirements.remove('-e .')

setup(
    name = 'ML Project',
    version='1.0',
    author='Nikunj',
    author_email='guptanikunj8@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)