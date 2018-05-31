#!/usr/bin/python

from setuptools import setup
from os import path

p = path.abspath(path.dirname(__file__))
with open(path.join(p, 'README.md')) as f:
    README = f.read()
setup(name='ftpsconnector',
      version='0.1.6',
      description='Initial connector code for pensieve',
      long_description=README,
      long_description_content_type="text/markdown",
      url='http://github.com/bc/ftpsconnector',
      author='Brian Cohn',
      author_email='brian.cohn@usc.edu',
      license='MIT',
      packages=['ftpsconnector'],
      install_requires=['tqdm'],
      zip_safe=False)
