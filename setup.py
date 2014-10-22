'''
Created on Aug 29, 2014

@author: tmahrt
'''
from distutils.core import setup
setup(name='praatio',
      version='1.0.0',
      author='Tim Mahrt',
      author_email='timmahrt@gmail.com',
      package_dir={'praatio':'praatio'},
      packages=['praatio'],
      license='LICENSE',
      long_description=open('README.rst', 'r').read(),
#       install_requires=[], # No requirements! # requires 'from setuptools import setup'
      )