from plone.app.testing import bbb
from plone.app import testing


class PloneTestCaseFixture(bbb.PloneTestCaseFixture):

    defaultBases = (bbb.PTC_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        from Products import contentmigration
        self.loadZCML('testing.zcml', package=contentmigration)
        self.loadZCML('testing-schemaextender.zcml', package=contentmigration)

PCM_FIXTURE = PloneTestCaseFixture()
TestLayer = testing.FunctionalTesting(
    bases=(PCM_FIXTURE, ), name='PloneContentMigrationTestCase:Functional')

SchemaExtenderTestLayer = TestLayer
