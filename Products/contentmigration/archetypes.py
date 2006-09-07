from Acquisition import aq_inner

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.ArchetypeTool import getType

from Products.ATContentTypes.migration.common import _createObjectByType
from Products.ATContentTypes.migration.migrator import BaseCMFMigrator
from Products.ATContentTypes.migration.migrator import ItemMigrationMixin
from Products.ATContentTypes.migration.migrator import FolderMigrationMixin
from Products.ATContentTypes.migration.migrator import UIDMigrator

from Products.contentmigration.inplace import BaseInplaceCMFMigrator
from Products.ATContentTypes.migration.migrator import InplaceItemMigrationMixin
from Products.ATContentTypes.migration.migrator import InplaceFolderMigrationMixin
from Products.ATContentTypes.migration.migrator import InplaceUIDMigrator

def migrate_dummy(self):
    """Do nothing.  Used to override inherited methods we don't
    want to run."""
    pass

class ATMigratorMixin:
    """Migrates content of one AT type to another AT type.""" 

    fields_map = {}
    only_fields_map = False

    # Override some methods from BaseCMFMigrator that we don't want to
    # run for AT migrations.
    migrate_dc = migrate_dummy
    migrate_allowDiscussion = migrate_dummy

    def beforeChange_storeDates(self):
        """Save creation date and modification date
        """
        old_schema = self.old.Schema()
        for field_name in ['creation_date', 'modification_date']:
            old_field = old_schema[field_name]
            accessor = (old_field.getEditAccessor(self.old) or
                        old_field.getAccessor(self.old))
            setattr(self, 'old_' + field_name, accessor())

    # XXX Can this be set through the call to the constructor?
    def last_migrate_date(self):
        """migrate creation / last modified date

        Must be called as *last* migration
        """
        new_schema = self.new.Schema()
        for field_name in ['creation_date', 'modification_date']:
            new_field = new_schema[field_name]
            mutator = new_field.getMutator(self.new)
            mutator(getattr(self, 'old_' + field_name))

class BaseATMigrator(ATMigratorMixin, BaseCMFMigrator):
    """Migrates content of one AT type to another AT type."""
    pass

class ATItemMigratorMixin:
    """Migrator for items implementing the AT API."""

    def beforeChange_schema(self):
        """Load the values of fields from according to fields_map if present.
        Each key in fields_map is a field in the old schema and each
        value is a field in the new schema.  If fields_map isn't a
        mapping, each filed in the old schema will be migrated into
        the new schema.  Obeys field modes for readable and writable
        fields.  These values are then passed in as field kwargs into
        the constructor in the createNew method."""
        _checkLoadAttr(self, 'schema')

        old_schema = self.old.Schema()

        typesTool = getToolByName(self.parent, 'portal_types')
        fti = typesTool.getTypeInfo(self.dst_portal_type)
        archetype = getType(self.dst_portal_type, fti.product)
        new_schema = archetype['klass'].schema 

        if self.only_fields_map:
            old_field_names = self.fields_map.keys()
        else:
            old_field_names = old_schema.keys()

        # Let the migrator handle the id and dates
        for omit_field_name in ['id', 'creation_date',
                                'modification_date']:
            if omit_field_name in old_field_names:
                old_field_names.remove(omit_field_name)

        self.schema = kwargs = {}
        for old_field_name in old_field_names:
            old_field = self.old.getField(old_field_name)
            new_field_name = self.fields_map.get(old_field_name,
                                                 old_field_name)

            if new_field_name is None:
                continue

            new_field = new_schema[new_field_name]

            if ('r' in old_field.mode and 'w' in new_field.mode):
                accessor = (old_field.getEditAccessor(self.old) or
                            old_field.getAccessor(self.old))
                value = accessor()
                kwargs[new_field_name] = value

    def createNew(self):
        """Create the new object passing in the loaded archetypes
        schema field values as kwargs."""
        _createObjectByType(self.dst_portal_type, self.parent,
                            self.new_id, **self.schema)
        self.new = getattr(aq_inner(self.parent).aq_explicit,
                           self.new_id)

class ATItemMigrator(ATItemMigratorMixin, ItemMigrationMixin,
                     UIDMigrator, BaseATMigrator):
    """Migrator for items implementing the AT API."""
    pass

class ATFolderMigrator(FolderMigrationMixin, UIDMigrator,
                       BaseATMigrator):
    """Migrator from folderish items implementing the AT API."""
    pass

# Inplace migrators

class BaseInplaceATMigrator(ATMigratorMixin, BaseInplaceCMFMigrator):
    """Migrates content of one AT type to another AT type inplace."""
    pass

class InplaceATItemMigrator(ATItemMigratorMixin,
                            InplaceItemMigrationMixin,
                            InplaceUIDMigrator,
                            BaseInplaceATMigrator):
    """Migrator for items implementing the AT API."""
    pass

class InplaceATFolderMigrator(InplaceFolderMigrationMixin,
                              InplaceUIDMigrator,
                              BaseInplaceATMigrator):
    """Migrator from folderish items implementing the AT API."""
    pass
