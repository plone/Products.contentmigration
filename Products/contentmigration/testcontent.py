from App.class_init import InitializeClass
from Products.Archetypes import atapi
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

InitializeClass(Document)
DocumentFactory = Factory(Document)
