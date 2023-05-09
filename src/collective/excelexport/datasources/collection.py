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
        #context.results()
        return [r.getObject() for r in self.context.results()]
