# initialize cmf test content
from Products.CMFCore import permissions

def initialize(context):
    import Products.contentmigration.testcontent
    from Products.CMFCore import utils
    utils.ContentInit(
            'CMF Default Content',
            content_types=(),
            permission=permissions.AddPortalContent,
            extra_constructors=(testcontent.addDocument,),
            visibility=None,
            ).initialize(context)
