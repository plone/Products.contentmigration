from setuptools import setup, find_packages

version = '2.1.16'

setup(
    name='Products.contentmigration',
    version=version,
    description="A generic content migration framework for Plone.",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Plone Archetypes ATContentTypes',
    author='Martin Aspeli (and others)',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/Products.contentmigration',
    license='LGPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    extras_require=dict(
        test=[
            'archetypes.schemaextender',
            'plone.app.testing',
            'Products.CMFPlone',
            'zope.testing',
            'Zope2',
        ],
    ),
    install_requires=[
        'setuptools',
    ],
)
