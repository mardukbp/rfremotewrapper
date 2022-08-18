#!/usr/bin/env python

from setuptools import setup

CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Topic :: Software Development :: Testing
"""

setup(name='robotframework-javaremote',
      version="0.1",
      description='Description',
      long_description="readme",
      long_description_content_type='text/markdown',
      author='Author',
      maintainer='Maintainer',
      maintainer_email='maintainer@email.com',
      url='https://github.com/user/repo',
      license='Apache 2',
      keywords='robotframework testing test automation',
      platforms='windows',
      classifiers=CLASSIFIERS.splitlines(),
      package_data={'': ['lib/jrobotremoteserver.jar']},
      package_dir={'': 'src'},
      packages=['JavaRemote'],
      install_requires=[
          'robotframework',
      ],
)