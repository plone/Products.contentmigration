from setuptools import setup, find_packages

version = '2.2.1'

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
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
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
