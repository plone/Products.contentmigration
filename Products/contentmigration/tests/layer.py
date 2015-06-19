from plone.app.testing import bbb
from plone.app import testing
from plone.testing import z2
from Products.GenericSetup import EXTENSION, profile_registry


def setupSampleTypeProfile():
    profile_registry.registerProfile('CMF_sampletypes',
        'CMF Sample Content Types',
        'Extension profile including CMF sample content types',
        'profiles/testing',
        'Products.contentmigration',
        EXTENSION)


class PloneTestCaseFixture(bbb.PloneTestCaseFixture):

    defaultBases = (bbb.PTC_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        setupSampleTypeProfile()
        from Products import contentmigration
        self.loadZCML('testing.zcml', package=contentmigration)
        self.loadZCML('testing-schemaextender.zcml', package=contentmigration)
        z2.installProduct(app, 'Products.contentmigration')

    def setUpPloneSite(self, portal):
        testing.applyProfile(portal, 'Products.contentmigration:CMF_sampletypes')

PCM_FIXTURE = PloneTestCaseFixture()
TestLayer = testing.FunctionalTesting(
    bases=(PCM_FIXTURE, ), name='PloneContentMigrationTestCase:Functional')

SchemaExtenderTestLayer = TestLayer
