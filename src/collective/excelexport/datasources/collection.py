from datetime import datetime

#from Products.CMFCore.interfaces import ISyndicatable
from plone.app.contenttypes.interfaces import ICollection
from collective.excelexport.datasources.base import BaseContentsDataSource
from plone import api
from zope.component import adapts
from zope.interface import Interface


class FolderContentsDataSource(BaseContentsDataSource):
    """Export the contents of a folder
    """
    adapts(ICollection, Interface)

    def get_filename(self):
        return "%s-%s" % (
            datetime.now().strftime("%d-%m-%Y"),
            self.context.getId(),
        )

    def get_objects(self):

        #import pdb; pdb.set_trace()
        #brains = self.context.items()
        #objects = self.context.listFolderContents()
        #these are not really brains
        brains =  self.context.items()
        #return [b[1]() for b in brains]
        #items = self.context.items()
        return [b[1] for b in brains]

        #Could maybe return just the (indexed) fields ?
        #return self.context.results()
        #return [b.getObject() for b in brains]
        #return brains

    def xget_objects(self):
        #query = self.context.query
        #query.pop('excelexport.policy', None)
        catalog = api.portal.get_tool('portal_catalog')
        ##brains = catalog.searchResults(**query)
        brains = catalog.searchResults(self.context.query)
        #return [b.getObject() for b in brains]
        mylist = [b.getObject() for b in brains]
        import pdb; pdb.set_trace()
        return mylist
