from setuptools import setup, find_packages

setup(
    name='judgement_analysis',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib'
    ],
    author='Vrishin Desai',
    author_email='vrishindesaiGM@gmail.com',
    description='A package for simulating the card game of judgement',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Vrdesai123/judgement_analysis',
    )