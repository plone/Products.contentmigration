from App.class_init import InitializeClass
from Products.CMFCore.PortalContent import PortalContent
from zope.component.factory import Factory

def addDocument(self, id, title='', description='', text_format='', text=''):
    """Add a Document.
    """
    o = Document(id, title, description, text_format, text)
    self._setObject(id, o, suppress_events=True)


class Document(PortalContent):
    """ A Document """

    def __init__(self, id, title='', description='', text_format='', text=''):
        self.id = id
        self.title = title
        self.description = description

    def Title(self):
        return self.title

    def listCreators(self):
        return ('test_user_1_',)

    def Creator(self):
        return self.listCreators()[0]


InitializeClass(Document)
DocumentFactory = Factory(Document)
