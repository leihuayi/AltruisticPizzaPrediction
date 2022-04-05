#!/usr/bin/env python3
from os import path
from setuptools import setup, find_packages
from setuptools.command.install import install
from distutils.core import setup, Command

NAME = 'raopred'

setup(
    name=f'raopred',
    version='0.0.1',
    description='Random Acts of Pizza Prediction',
    author='Sarah Gross',
    author_email='leihuayi@gmail.com',
    packages=find_packages(exclude=['tests', 'research']),
    package_data={
        'raopred': ['pickles/*']
    },
    install_requires=['nltk', 'scikit-learn'],
    extras_require={
        'train': ['numpy', 'pandas', 'seaborn', 'jupyter'],
    }
)