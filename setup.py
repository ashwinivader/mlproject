from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT= '_e.'

def get_requirments(file_path:str)->List[str]:
    '''
    This function will return requirments mentioned in requirments.txt
    '''
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[require.replace("\n","") for require in requirements]
       
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements 
    

setup(
    name='mlproject',
    version= '0.0.1',
    author= "AAK",
    author_email="@",
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn']
    install_requirs=get_requirments("requirments.txt")

)