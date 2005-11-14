from Products.CMFCore.utils import getToolByName
from content import migrateContent

def migrate(portal, query, metaType, attributeActions, callBefore=None, callAfter=None, **kwargs):
    """Migrate from one content type to another. You can use this method to 
    change content from one type to another.
    
    - portal is the root of the portal.
    - query is a dict to pass to a catalog for finding the types to migrate.
        Typically, this would be something like {'portal_type' : 'MyType'}
    - metaType is the new meta type to migrate to
    - attributeActions is a list of attribute migration actions. Please see 
        attributes.py for details.
    - callBefore, if given, should be method with the signature
            
            callBefore(obj, **kwargs)
    
        It will be called before any other migration is attempted, for each
        object returned by query. callBefore should return True if this object
        is to be migrated, or False if this objects should be skipped.
    - callAfter, is given, is analogous to callBefore, but called after 
        migration of an object. It should not return anything.
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
            
        # Execute all migration
        migrateContent(portal, obj, metaType, action, **kwargs)
                
        # Apply callAfter() if applicable
        if callAfter is not None:
            callAfter(obj, **kwargs)
    
        # Store success
        migrated.append('/'.join(obj.getPhysicalPath()))
    
    return migrated

