from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase.layer import PloneSite


class TestLayer(PloneSite):
    """ layer for integration tests """

    @classmethod
    def setUp(cls):
        fiveconfigure.debug_mode = True
        from Products import contentmigration
        zcml.load_config('testing.zcml', package=contentmigration)
        fiveconfigure.debug_mode = False

    @classmethod
    def tearDown(cls):
        pass
