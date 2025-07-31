from setuptools import find_packages , setup
from typing import List
 
def get_requirements()->list[str]:
    """
    this function will return the list of requiremnets
    """
    requirement_lst:list = []
    try:
        with open("requirements.txt","r") as file:
            # reading the line from file
            lines=file.readlines()
            # process line
            for line in lines:
                requirement = line.strip()
                ## ignore empty line and -e.
                if requirement and requirement !='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Returning an empty list.")
    return requirement_lst


setup(
    name = "networksecurity",
    version = "0.0.1",
    author = "deepak",
    author_email = "deepakreturns7@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    description = "This is a network security project"
)