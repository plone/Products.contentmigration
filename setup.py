from setuptools import setup, find_packages

version = '2.1.10'

setup(name='Products.contentmigration',
      version=version,
      description="A generic content migration framework for Plone.",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        ],
      keywords='Plone Archetypes ATContentTypes',
      author='Martin Aspeli (and others)',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/Products.contentmigration',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
            test=['zope.testing', 'Zope2', 'Products.CMFPlone',
                  'plone.app.testing', 'archetypes.schemaextender']),
      install_requires=[
          'setuptools',
      ],
)
