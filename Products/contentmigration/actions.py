from Products.Archetypes.Storage import AttributeStorage

def migrateAttribute(portal, obj, action, newObj=None, **kwargs):
    """Apply a single action.
    - portal should be the portal root
    - obj should be the object to migrate from
    - newObj, if given, should be the object to migrate to. If not given,
        migration happens within obj only. If newObj is giving, attributes
        will not be unset on obj even if a newAttribute for an action is
        specified.
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
        
            transform(obj, oldAttr, newObj, newAttr, value, **kwargs)
        
        Note that newObj and newAttr may be the same as obj and oldAttr,
        respectively, if no object- or attribute-migration is taking place.
        
        It should return the transformed attribute. If 'transform' is given
        and 'newAttribute' is not, the return value from 'transform' is
        stored back in 'attribute'.
        
        Finally, if callAfter is given, it is called with the same arguments as
        callBefore().
    """
    
    storage = action.get('storage', AttributeStorage())
    newStorage = action.get('newStorage', None)
    attributeName = action['attribute']
    callBefore = action.get('callBefore', None)
    transform = action.get('transform', None)
    newAttribute = action.get('newAttribute', None)
    callAfter = action.get('callAfter', None)
    
    migrateObject = True
    if newObj is None:
        migrateObject = False
        newObj = obj
        
    
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
        if newAttribute is None:
            newAttributeName = attributeName
        else:
            newAttributeName = newAttribute
        value = transform(obj, attributeName, newObj, newAttributeName, value, **kwargs)
    
    # Get new attribute and assign, if necessary
    if newAttribute is not None:
        if newStorage is None:
            storage.set(newAttribute, newObj, value)
        else:
            newStorage.set(newAttribute, newObj, value)
        if not migrateObject:
            storage.unset(attributeName, obj)
    # If there is a new storage, but no new attribute, set only this
    elif newStorage is not None:
        newStorage.set(attributeName, newObj, value)
        if not migrateObject:
            storage.unset(attributeName, newObj)
    # If there was a transform, but no new attribute or storage, re-set value
    elif transform is not None:
        storage.set(attributeName, newObj, value)

    # Call callAfter, if given
    if callAfter is not None:
        callAfter(newObj, attributeName, value, **kwargs)
  
    return True