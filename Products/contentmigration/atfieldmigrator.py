from Products.CMFCore.utils import getToolByName
from Products.Archetypes.Storage import AttributeStorage

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
    - 'actions' specifies a list of actions to apply to each object. It should
        be a tuple or list of dicts, with the keys:
        
            - attribute (requied)
            - storage (optional; default = AttributeStorage)
            - callBefore
            - transform
            - newAttribute
            - newStorage (optional; default = same as 'storage')
            - transform 
            - callAfter 
       
        For each object found by the query, the migrator will test for the
        existence of an attribute given by 'attribute'. If found, migration
        of this attribute will take place.
        
        The 'storage' argument gives the storage used for this field. By default
        a plain AttributeStorage will be used, but if the field used a specific
        storage, this should be passed in. If newAttribute is given, the same
        storage will be used, unless newStorage is also given. It is also
        possible to give just newStorage, which is equivalent to switching
        the storage on a field.
       
        First, callBefore is called, if given. This should be method with the
        signrature
       
            callBefore(obj, attributeName, attributeValue, **kwargs)
        
        If this returns True, migration continues. If newAttribute is given,
        the attribute named in 'attribute' is deleted and replaced by one named
        in 'newAttribte'. If 'transform' is given, this is used to transform
        the value of the attribute between the two attributes. This should be a
        method with the following signature
        
            transform(obj, oldAttributeName, value, **kwargs)
        
        It should return the transformed attribute. If 'transform' is given
        and 'newAttribute' is not, the return value from 'transform' is
        stored back in 'attribute'.
        
        Finally, if callAfter is given, it is called with the same arguments as
        callBefore().
        
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

def migrateAttribute(portal, obj, action, **kwargs):
    """Apply a single action. See migrate() for details.
    """
    
    storage = action.get('storage', AttributeStorage())
    newStorage = action.get('newStorage', None)
    attributeName = action['attribute']
    callBefore = action.get('callBefore', None)
    transform = action.get('transform', None)
    newAttribute = action.get('newAttribute', None)
    callAfter = action.get('callAfter', None)
    
    try:
        value = storage.get(attributeName, obj)
    except AttributeError:
        return False
    
    # Call and test callBefore, if given
    if callBefore is not None:
        status = callBefore(obj, attributeName, value, **kwargs)
        if not status:
            return
    
    # Apply transform, if given
    if transform is not None:
        value = transform(obj, attributeName, value, **kwargs)
    
    # Get new attribute and assign, if necessary
    if newAttribute is not None:
        if newStorage is None:
            storage.set(newAttribute, obj, value)
        else:
            newStorage.set(newAttribute, obj, value)
        storage.unset(attributeName, obj)
    # If there is a new storage, but no new attribute, set only this
    elif newStorage is not None:
        newStorage.set(attributeName, obj, value)
        storage.unset(attributeName, obj)
    # If there was a transform, but no new attribute or storage, re-set value
    elif transform is not None:
        storage.set(attributeName, obj, value)

    # Call callAfter, if given
    if callAfter is not None:
        callAfter(obj, attributeName, value, **kwargs)
  
    return True