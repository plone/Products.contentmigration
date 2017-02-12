Changelog
=========

2.1.15 (2017-02-12)
-------------------

Bug fixes:

- Errors has been dropped/deprecated errors from OFS.CopySupport.
  [tschorr]


2.1.14 (2016-11-01)
-------------------

Bug fixes:

- Remove unused import of Archetypes. [davisagli]


2.1.13 (2016-08-11)
-------------------

Fixes:

- Use zope.interface decorator.
  [gforcada]


2.1.12 (2016-03-31)
-------------------

Fixes:

- HAS_LINGUA_PLONE now checks only if LinguaPlone is installed.
  No more if LinguaPlone or plone.app.multilingual is installed.
  [bsuttor]


2.1.11 (2015-07-18)
-------------------

- Remove implicit dependency on CMFDefault by moving testcontent to product.
  [tomgross]


2.1.10 (2015-04-17)
-------------------

- Ported to plone.app.testing
  [acattla, tomgross]


2.1.9 (2014-09-07)
------------------

- Migrate translated items when plone.app.multilingual or LinguaPlone present.
  [pbauer]

2.1.8 (2014-04-14)
------------------

- Changed all old-style to new-style classes for easier method overloading from
  derived classes.
  [thet]


2.1.7 (2014-01-27)
------------------

- Nothing changed yet.


2.1.6 (2013-09-23)
------------------

- Unlock items with webdav.
  [maurits]


2.1.5 (2013-07-15)
------------------

- Keep redirections from plone.app.redirect when migrating.
  [maurits]


2.1.4 (2013-04-06)
------------------

- Default to position 0 if folder position is not assigned.
  [kroman0, pbauer]


2.1.3 (2013-03-05)
------------------

- Modify UIDMigrator so that it also works for items which
  provides IMutableUUID.
  [pabo]


2.1.2 (2012-12-21)
------------------

- When Joe is the Creator of an object and Jane is the Owner, make
  sure Joe stays the Creator after migrating.
  [maurits]


2.1.1 (2012-04-15)
------------------

- Migrate marker interfaces.
  Fixes http://dev.plone.org/ticket/11424
  [maurits]

- Migrate extension fields too (archetypes.schemaextender).
  [maurits]

- Use obj.__parent__ instead of obj getParentNode() for Zope trunk
  compatibility.
  [elro]

2.1.0 (2011-10-06)
------------------

- Add support for a `limit` option for the catalog based walkers, so it only
  tries to load up to `limit` items at a time, defaulting to no limit.
  [hannosch]

- Catch attribute errors during `brain.getObject` and log them instead of
  breaking the upgrade.
  [hannosch]

2.0.3 (2011-08-11)
------------------

- Undo patch correctly
  [jfroche]

2.0.2 (2011-08-10)
------------------

- Fix migration for folder containing an object (which is often the case) by patching the 'notifyWorkflowCreated' method on WorkflowAware class
  [jfroche]

- Fix for folderish items, also use ATItemMigratorMixin
  [jfroche]

- Add local buildout config
  [jfroche]

- Use module name, not the full file path, to register with the logging module.
  [mj]

2.0.1 - 2010-12-08
------------------

- Unlock locked objects prior to migrating them.
  [ggozad]

2.0 - 2010-07-18
----------------

- No changes.

2.0b1 - 2010-06-13
------------------

- Avoid deprecation warnings under Zope 2.13.
  [hannosch]

- Added support for archetypes.schemaextender >= 2.0 and disable the schema
  cache during migrations.
  [hannosch]

2.0a3 - 2009-11-15
------------------

- Fix issue with my adjustment to the _createObjectByType function where the
  portal_type wasn't getting set properly in Plone 3.
  [davisagli]


2.0a2 - 2009-11-15
------------------

- Make the _createObjectByType function call the _constructInstance method
  of the FTI, rather than trying to duplicate its logic.  This adds
  compatibility with CMF 2.2.
  [davisagli]


2.0a1 - 2009-11-14
------------------

- Avoid zope.app dependencies.
  [hannosch]

- Use Zope interfaces from `OFS` and `Archetypes`.
  [witsch]


1.2 - 2009-08-09
----------------

- Fix tests to run on Plone 3.3.
  [witsch]

- Fix issue with leftover local role assignments for deleted users.
  [pbugni, rossp]


1.1 - 2009-03-05
----------------

- Add missing imports in various places.
  [wichert]

- Fix a bug in the permission migration logic, which caused the Manager
  role to gain all permissions.
  [ivo, wichert]


1.0 - 2008-09-17
----------------

- Update documentation to fit the code.
  [pbugni]

- Modify CatalogWalker to root the search at the portal passed in. This
  makes it possible to only migrate in parts of a site.
  [wichert]

- Correct path handling, cleanup classifiers, make short description short.
  [wichert]

- Use standard naming convention for the contentmigration package.
  [wichert]

- Be more graceful with schema mismatches.
  [wichert]

- Replaced deprecated transaction.commit(1) with
  transaction.savepoint(optimistic=True).
  [stonor]


1.0b4 - 2007-06-11
------------------

- Add import for os so egg can be built.
  [derek_richardson]

- Added missing `configure.zcml`.
  [witsch]

- Reorganize contentmigration trunk for eggification. If you are using the
  trunk as a product, pin to the previous revision or change your external
  to use src/Products/contentmigration.
  [derek_richardson]

- First eggified release.
