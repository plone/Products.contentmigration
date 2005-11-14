from Products.CMFCore.utils import getToolByName
from actions import migrateAttribute

def migrate(portal, query, actions=[], callBefore=None, callAfter=None, **kwargs):
    """Run a migration.
    
    - portal is the root of the portal.
    - query is a dict to pass to a catalog for finding the types to migrate.
        Typically, this would be something like {'portal_type' : 'MyType'}
    - callBefore, if given, should be method with the signature
            
            callBefore(obj, **kwargs)
    
        It will be called before any other migration is attempted, for each
        object returned by query. callBefore should return True if this object
        is to be migrated, or False if this objects should be skipped.
    - callAfter, is given, is analogous to callBefore, but called after 
        migration of an object. It should not return anything.
    - actions is a list of migration actions. Please see actions.py for details.
    - Returns a list of the url's to objects that were successfully migrated.
    """
    
    catalog = getToolByName(portal, 'portal_catalog')
    results = catalog.searchResults(query)
    
    migrated = []
    
    for res in results:
        obj = res.getObject()
        
        # Apply callBefore() if applicable
        if callBefore is not None:
            status = callBefore(obj, **kwargs)
            if not status:
                continue
            
        # Execute all actions
        for action in actions:
            migrateAttribute(portal, obj, action, **kwargs)
                
        # Apply callAfter() if applicable
        if callAfter is not None:
            callAfter(obj, **kwargs)
    
        # Store success
        migrated.append('/'.join(obj.getPhysicalPath()))
    
    return migrated

