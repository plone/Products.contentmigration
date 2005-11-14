import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from Testing import ZopeTestCase
from Products.contentmigration.tests import cmtc
from Products.contentmigration.atfieldmigrator import migrate
from Products.Archetypes.Storage.annotation import AnnotationStorage
from Products.Archetypes.Storage import AttributeStorage

default_user = ZopeTestCase.user_name

def makeUpper(obj, attr, newObj, newAttr, val, **kw):
    s = str(val)
    s = s.upper()
    val.update(s, obj)
    return val

def conditionallyAbortObject(obj, **kwargs):
    if obj.getId() == 'd1':
        return False
    else:
        return True

def conditionallyAbortAttribute(obj, attributeName, attributeValue, **kwargs):
    if obj.getId() == 'd1':
        return False
    else:
        return True
    
def callAfterObject(obj, **kwargs):
    kwargs['lst'].append(obj.getId())

def callAfterAttribute(obj, attributeName, attributeValue, **kwargs):
    kwargs['lst'].append("%s: %s = %s" % (obj.getId(), attributeName, attributeValue,))

    
class TestAttributeMigration(cmtc.ContentMigratorTestCase):
    """Test migration"""

    def afterSetUp(self):
        # Create some content to migrate
        self.folder.invokeFactory('Document', 'd1')
        self.folder.invokeFactory('Document', 'd2')
        self.folder.invokeFactory('News Item', 'n1')
        self.folder.invokeFactory('News Item', 'n2')
    
        self.folder['d1'].setTitle('Document 1')
        self.folder['d1'].setDescription('Description 1')
        self.folder['d1'].setText('Body one')
        
        self.folder['d2'].setTitle('Document 2')
        self.folder['d2'].setDescription('Description 2')
        self.folder['d2'].setText('Body two')
        
        self.folder['n1'].setTitle('News 1')
        self.folder['n1'].setDescription('Description 3')
        self.folder['n1'].setText('News one')
        
        self.folder['n2'].setTitle('News 2')
        self.folder['n2'].setDescription('Description 4')
        self.folder['n2'].setText('News two')
    
    def testAttributeRenaming(self):
        storage = AnnotationStorage()
        migrate(self.portal, 
                 query   = {'portal_type' : 'Document'}, 
                 actions = ({'attribute'    : 'text',
                             'newAttribute' : 'bodyText',
                             'storage'      : storage
                             },
                            )
               )
        self.assertEqual(storage.get('bodyText', self.folder['d1']).getRaw(), 'Body one')
        self.assertEqual(storage.get('bodyText', self.folder['d2']).getRaw(), 'Body two')
        
        try:
           storage.get('text', self.folder['d1'])
        except AttributeError:
            pass
        else:
            self.fail()

    def testTransform(self):
        storage = AnnotationStorage()
        migrate(self.portal, 
                 query   = {'portal_type' : 'Document'}, 
                 actions = ({'attribute'    : 'text',
                             'storage'      : storage,
                             'transform'    : makeUpper
                             },
                            )
               )
        self.assertEqual(storage.get('text', self.folder['d1']).getRaw(), 'BODY ONE')
        self.assertEqual(storage.get('text', self.folder['d2']).getRaw(), 'BODY TWO')

    def testAttributeRenamingAndTransform(self):
        storage = AnnotationStorage()
        migrate(self.portal, 
                 query   = {'portal_type' : 'Document'}, 
                 actions = ({'attribute'    : 'text',
                             'newAttribute' : 'bodyText',
                             'storage'      : storage,
                             'transform'    : makeUpper
                             },
                            )
               )
        self.assertEqual(storage.get('bodyText', self.folder['d1']).getRaw(), 'BODY ONE')
        self.assertEqual(storage.get('bodyText', self.folder['d2']).getRaw(), 'BODY TWO')
    
    def testNewStorageAndAttribute(self):
        storage = AnnotationStorage()
        newStorage = AttributeStorage()
        migrate(self.portal, 
                 query   = {'portal_type' : 'Document'}, 
                 actions = ({'attribute'    : 'text',
                             'newAttribute' : 'bodyText',
                             'storage'      : storage,
                             'newStorage'   : newStorage
                             },
                            )
               )
        self.assertEqual(getattr(self.folder['d1'], 'bodyText').getRaw(), 'Body one')
        self.assertEqual(getattr(self.folder['d2'], 'bodyText').getRaw(), 'Body two')
        
        try:
            storage.get('text', self.folder['d1'])
        except AttributeError:
            pass
        else:
            self.fail()

    def testNewStorageOnly(self):
        storage = AnnotationStorage()
        newStorage = AttributeStorage()
        migrate(self.portal, 
                 query   = {'portal_type' : 'Document'}, 
                 actions = ({'attribute'    : 'text',
                             'storage'      : storage,
                             'newStorage'   : newStorage
                             },
                            )
               )
        self.assertEqual(getattr(self.folder['d1'], 'text').getRaw(), 'Body one')
        self.assertEqual(getattr(self.folder['d2'], 'text').getRaw(), 'Body two')
        
        try:
            storage.get('text', self.folder['d1'])
        except AttributeError:
            pass
        else:
            self.fail()

    def testAbortAttribute(self):
        storage = AnnotationStorage()
        migrate(self.portal, 
                 query   = {'portal_type' : 'Document'}, 
                 actions = ({'attribute'    : 'text',
                             'transform'    : makeUpper,
                             'storage'      : storage,
                             'callBefore'   : conditionallyAbortAttribute,
                             },
                            )
               )
               
        self.assertEqual(storage.get('text', self.folder['d1']).getRaw(), 'Body one')
        self.assertEqual(storage.get('text', self.folder['d2']).getRaw(), 'BODY TWO')
    
    def testAbortObject(self):
        storage = AnnotationStorage()
        migrate(self.portal, 
                 query   = {'portal_type' : 'Document'}, 
                 actions = ({'attribute'    : 'text',
                             'transform'    : makeUpper,
                             'storage'      : storage,
                             },
                            ),
                callBefore = conditionallyAbortObject,
               )
               
        self.assertEqual(storage.get('text', self.folder['d1']).getRaw(), 'Body one')
        self.assertEqual(storage.get('text', self.folder['d2']).getRaw(), 'BODY TWO')

    def testCallAfterObject(self):
        storage = AnnotationStorage()
        lst = []
        migrate(self.portal, 
                 query   = {'portal_type' : 'Document'}, 
                 actions = ({'attribute'    : 'text',
                             'transform'    : makeUpper,
                             'storage'      : storage,
                             },
                            ),
                 callAfter = callAfterObject,
                 lst = lst,
               )
        lst.sort()
        self.assertEqual(lst, ['d1', 'd2'])
    
    def testCallAfterAttribute(self):
        storage = AnnotationStorage()
        lst = []
        migrate(self.portal, 
                 query   = {'portal_type' : 'Document'}, 
                 actions = ({'attribute'    : 'text',
                             'transform'    : makeUpper,
                             'storage'      : storage,
                             'callAfter'    : callAfterAttribute
                             },
                            ),
                 lst = lst,
               )
        lst.sort()
        self.assertEqual(lst, ['d1: text = BODY ONE', 'd2: text = BODY TWO'])

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestAttributeMigration))
    return suite

if __name__ == '__main__':
    framework()
