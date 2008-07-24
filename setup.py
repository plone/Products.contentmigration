import os
from setuptools import setup, find_packages

version = '1.0b4'

def read(rnames):
    return open(os.path.join(*rnames.split("/"))).read()

setup(name='Products.contentmigration',
      version=version,
      description="A generic content migration framework for Plone.",
      long_description=(
        read('Products/contentmigration/README.txt')
        + '\n\n' +
        read('Products/contentmigration/CHANGES.txt')
        ),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone archetypes atct',
      author='Martin Aspeli (and others)',
      author_email='optilude@gmx.net',
      url='',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
