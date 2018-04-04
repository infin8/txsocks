from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='txsocks',
      version=version,
      description="Socks 5 Client for Twisted",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='twisted socks socks5',
      author='n8',
      author_email='yo.its.n8@gmail.com',
      url='https://infin8.github.io/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
