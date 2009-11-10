#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='syncables',
      version='0.1',
      packages=find_packages(),
      package_data={'syncables': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'syncables': ['bin/*.pyc']}
     )
