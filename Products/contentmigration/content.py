from Products.Archetypes.Storage import AttributeStorage
from attributes import migrateAttribute

def migrateContent(portal, obj, newMetaType, attributeActions, **kwargs):
    """Migrate a content object to a new type
    
    - portal should be the portal root
    - obj should be the object to migrate from
    - newMetaType is the meta-type to switch the objec to
    - attributeActions is a list of attribute action dicts to apply in order
        to transform the attributes of the old object to the new one. See
        attributes.py for details.
    """
    
    raise NotImplementedError, "Content migration not yet implemented"
    
    # We may want to use ATContentTypes' migrator for this
    #
    # - This method is about migrating a single content object. That would
    #   be nice, but not strictly necessary.
    # - Ability to pass in custom query to typemigrator.migrate() (which
    #   calls migrateContent) is quite important. Need to ensure ATCT walker
    #   can handle this
    # - Want to apply attribute actions (see attributes.py) as part of
    #   migration.