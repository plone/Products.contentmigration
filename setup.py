from setuptools import setup, find_packages

version = '1.0b4'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name='Products.contentmigration',
      version=version,
      description="A generic content migration framework for Plone, which has no UI or value on its own, but should help you write your own content migrations.",
      long_description=(
        read('src/Products/contentmigration/README.txt')
        + '\n\n' +
        read('src/Products/contentmigration/CHANGES.txt')
        ),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone archetypes atct',
      author='Martin Aspeli (and others)',
      author_email='optilude@gmx.net',
      url='',
      license='LGPL',
      package_dir={'':'src'},
      packages=find_packages('src'),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
