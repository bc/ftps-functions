#!/usr/bin/python

from setuptools import setup
from os import path

p = path.abspath(path.dirname(__file__))
readme_filepath = path.join(p, 'README.md')
README = "See https://github.com/bc/ftpsconnector for full documentation."
if os.path.isfile(readme_filepath):
      with open(readme_filepath) as f:
          README = f.read()

setup(name='ftpsconnector',
      version='0.2.1',
      description='Initial FTPS Binary File Upload/Dowload connector code for Pensieve',
      long_description=README,
      long_description_content_type="text/markdown",
      url='http://github.com/bc/ftpsconnector',
      author='Brian Cohn',
      author_email='brian.cohn@usc.edu',
      license='MIT',
      packages=['ftpsconnector'],
      install_requires=['tqdm'],
      zip_safe=False)
