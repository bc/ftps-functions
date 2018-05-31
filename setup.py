from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(name='ftpsconnector',
      version='0.1.3',
      description='Initial connector code for pensieve',
      long_description=long_description,
	  long_description_content_type="text/markdown",
      url='http://github.com/bc/ftpsconnector',
      author='Brian Cohn',
      author_email='brian.cohn@usc.edu',
      license='MIT',
      packages=['ftpsconnector'],
      zip_safe=False)
