from Testing import ZopeTestCase
from Products.contentmigration.migrator import InlineFieldActionMigrator
from Products.contentmigration.walker import CustomQueryWalker

import transaction

from Products.PloneTestCase import PloneTestCase
PloneTestCase.setupPloneSite()

# Callback methods

def makeUpper(obj, val, **kwargs):
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
    if 'd1' in obj.getId():
        return False
    else:
        return True
    
def callAfterObject(obj, **kwargs):
    kwargs['lst'].append(obj.getId())

def callAfterAttribute(obj, attributeName, attributeValue, **kwargs):
    kwargs['lst'].append("%s: %s = %s" % (obj.getId(), attributeName, attributeValue,))

# Test migrator
class TestMigrator(InlineFieldActionMigrator):
    src_portal_type = 'Document'
    src_meta_type = 'ATDocument'

class ContentMigratorTestCase(PloneTestCase.PloneTestCase):

    class Session(dict):
        def set(self, key, value):
            self[key] = value

    def _setup(self):
        PloneTestCase.PloneTestCase._setup(self)
        self.app.REQUEST['SESSION'] = self.Session()
        
    def execute(self, query, actions, callBefore=None, **kwargs):
        TestMigrator.fieldActions = actions
        walker = CustomQueryWalker(self.portal, TestMigrator, 
                                    query = query,
                                    callBefore = callBefore, 
                                    **kwargs)
        # Need this to avoid copy errors....
        transaction.commit(1)
        walker.go(**kwargs)