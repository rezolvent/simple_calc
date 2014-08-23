#!/usr/bin/env python

# Use setuptools if we can
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import os
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='calc',
    version='0.9.5',
    description='Calculator: A simple calculator for calculate same expressions',
    long_description=README,
    author='Makarov Danil',
    packages=find_packages(),
    include_package_data=True,
)
