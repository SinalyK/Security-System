from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirements:List[str]=[]
    try:
        with open('requirements.txt','r')as file:
            lines=file.readlines()

            for line in lines:
                requirement=line.strip()

                if requirement and requirement !='-e .':
                    requirements.append(requirement)
    except FileNotFoundError as e:
        raise("File not found")

    return requirements

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Sinaly Kanadjigui",
    author_email="sinaly.kanadjigui.23@ump.ac.ma",
    packages=find_packages(),
    install_requires=get_requirements()
)