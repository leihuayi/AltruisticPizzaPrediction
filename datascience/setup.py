#!/usr/bin/env python3
from os import path
from setuptools import setup, find_packages

NAME = 'raopred'


setup(
    name=f'raopred',
    version='0.0.4',
    description='Random Acts of Pizza Prediction',
    author='Sarah Gross',
    author_email='leihuayi@gmail.com',
    packages=find_packages(exclude=['tests', 'research']),
    package_data={
        'raopred': ['pickles/*']
    },
    install_requires=[
        'nltk==3.7',
        'scikit-learn==1.0.2'
    ],
    extras_require={
        'train': [
            'pandas>=1.3.0',
            'seaborn==0.11.2',
            'jupyter==1.0.0'
    ],
    },
)