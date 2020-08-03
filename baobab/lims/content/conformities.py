from Products.ATContentTypes.content import schemata
from Products.Archetypes import atapi
from baobab.lims.config import PROJECTNAME
from plone.app.folder.folder import ATFolder, ATFolderSchema
from zope.interface.declarations import implements
from baobab.lims.interfaces import IConformities

schema = ATFolderSchema.copy()


class Conformities(ATFolder):
    implements(IConformities)
    displayContentsTab = False
    schema = schema


schemata.finalizeATCTSchema(schema, folderish=True, moveDiscussion=False)
atapi.registerType(Conformities, PROJECTNAME)