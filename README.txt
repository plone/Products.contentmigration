Content migration utilities
===========================

by Martin Aspeli <optilude@gmx.net> and others

Released under the GNU Lesser General Public License (LGPL) version 2.0

This is a generic content migration framework, which should help you write
your own content migrations. It has no UI and no value on its own, but
makes it easy to write certain type of content migrations.

This replaces the ATContentTypes migration framework, and provide three useful
extensions:

* A CustomQueryWalker can be used to specify a more specific catalog query
  for a walker to use (e.g. which content to actually migrate). This can
  be used with any migrator.

* A BaseInlineMigrator is similar to BaseMigrator, but does not migrate by
  copying the old object to a temporary location, creating a new object and
  applying migration methods. Instead, migration methods are applied in-place.
  This simplifies the code significantly, because attributes, local roles etc.
  does not need to be copied over.

  Note that whereas BaseMigrator works in terms of self.old and self.new as
  the objects being migrated, BaseInlineMigrator only has a single object,
  stored in self.obj. This can be used with any walker.

* An extension of this class called FieldActionMigrator uses the
  action-based migration framework for Archetypes fields, found in field.py.
  Please refer to that file for full details, but briefly, you specify a list
  of attributes to migrate at the storage level, instructing the migrator
  whether to rename, transform, unset or change the storage for an attribute.

Please see the docstrings in walker.py, migrator.py and field.py for full
details. For examples, see tests/cmtc.py and tests/testATFieldMigration.py.
