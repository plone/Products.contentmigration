import unittest
import doctest

from plone.testing import layered

optionflags = (doctest.NORMALIZE_WHITESPACE |
               doctest.ELLIPSIS |
               doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.REPORT_NDIFF)

from Products.contentmigration.tests.layer import TestLayer


def test_suite():
    suite = unittest.TestSuite()
    test_files = [
        '../inplace.txt',
        '../translocate.txt',
        '../archetypes.txt',
        '../bugfixes.txt',
        '../schemaextender.txt'
    ]
    for test_file in test_files:
            suite.addTest(layered(
            doctest.DocFileSuite(test_file, package='Products.contentmigration.tests',
                                 optionflags=optionflags),
            layer=TestLayer))
    return suite
