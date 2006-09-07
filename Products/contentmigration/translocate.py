"""Support for migrators that place the destination object in a
different location from the source object."""

from Acquisition import aq_inner

from Products.ATContentTypes.migration.common import _createObjectByType

class TranslocatingMigratorMixin:
    """A migrator that placees the destination object in a different
    location from the source object."""

    def getDestinationParent(self):
        """Return the container into which the destination will be
        added."""
        return self.parent

    def createNew(self):
        """Create the new object
        """
        dst_parent = self.getDestinationParent()

        # Support AT migration if used
        schema = getattr(self, 'schema', {})
        
        _createObjectByType(self.dst_portal_type, dst_parent,
                            self.new_id, **schema)
        self.new = getattr(aq_inner(dst_parent).aq_explicit, self.new_id)
