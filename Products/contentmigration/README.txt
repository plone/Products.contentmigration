Content migration utilities  
by Martin Aspeli <optilude@gmx.net>

Released under the GNU Lesser General Public License (LGPL) version 2.0

This is a generic content migration framework, which should help you write
your own content migrations. It has no UI and no value on its own, but
makes it easy to write certain type of content migrations.

At present, only one migrator is available, the AT Field Migrator. This migrator
is capable of migrating between two different versions of the same AT content
type. It is capable of renaming fields, changing a field's storage (with or
without a rename in the process), or applying any transformation on a field's
contents via a callback function.

Please see the docstring on atfieldmigrator.migrate() for full details. For
examples, see tests/testATFieldMigration.