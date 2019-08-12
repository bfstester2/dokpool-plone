from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from Products.CMFCore.utils import getToolByName
from docpool.dashboard import DocpoolMessageFactory as _
from AccessControl.SecurityInfo import allow_module
from docpool.base.utils import getDocumentPoolSite


class DashboardCollectionsVocabulary(object):
    """
    """

    implements(IVocabularyFactory)

    def __call__(self, context, raw=False):
        # print context
        esd = getDocumentPoolSite(context)
        path = "/".join(esd.getPhysicalPath()) + "/contentconfig"
        cat = getToolByName(esd, 'portal_catalog', None)
        if cat is None:
            if not raw:
                return SimpleVocabulary([])
            else:
                return []
        types = cat(
            {
                "portal_type": "DashboardCollection",
                "sort_on": "sortable_title",
                "path": path,
            }
        )
        if not raw:
            types = [(brain.getObject(), brain.Title) for brain in types]
        else:
            types = [(brain.getId, brain.Title) for brain in types]

        if not raw:
            items = [SimpleTerm(i[0], i[0], i[1]) for i in types]
            return SimpleVocabulary(items)
        else:
            return types


DashboardCollectionsVocabularyFactory = DashboardCollectionsVocabulary()


allow_module("docpool.dashboard.vocabularies")
