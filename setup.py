from setuptools import setup, find_packages

import sys


if sys.version_info[0] != 2:
    # Prevent creating or installing a distribution with Python 3.
    raise ValueError("Products.contentmigration is based on Archetypes, which is Python 2 only.")

version = '2.2.2.dev0'

setup(
    name='Products.contentmigration',
    version=version,
    description="A generic content migration framework for Plone.",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: Core",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Plone Archetypes ATContentTypes',
    author='Martin Aspeli (and others)',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.org/project/Products.contentmigration',
    license='LGPL',
    packages=find_packages(),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    python_requires='==2.7.*',
    extras_require=dict(
        test=[
            'archetypes.schemaextender',
            'plone.app.testing',
            'Products.CMFPlone',
            'six',
            'zope.testing',
            'Zope2',
        ],
    ),
    install_requires=[
        'setuptools',
    ],
)
