from setuptools import find_packages, setup
from typing import List


def get_requirments(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        [req.replace('\n', '') for req in requirments]
        if '-e .' in requirments:
            requirments.remove('-e .')
    return requirments

setup(name='mlproject1',
    version='0.0.1',
    author='Thulana',
    author_email='thulanavimukthi93@gmail.com',
    packages=find_packages(),
    install_requires= get_requirments('requirments.txt')
)