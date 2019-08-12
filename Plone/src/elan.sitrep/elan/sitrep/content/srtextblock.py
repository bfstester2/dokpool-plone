# -*- coding: utf-8 -*-
#
# File: srtextblock.py
#
# Copyright (c) 2017 by Condat AG
# Generator: ConPD2
#            http://www.condat.de
#

__author__ = ''
__docformat__ = 'plaintext'

"""Definition of the SRTextBlock content type. See srtextblock.py for more
explanation on the statements below.
"""
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from zope.component import adapts
from zope import schema
from plone.directives import form, dexterity
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from collective import dexteritytextindexer
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder
from Products.CMFPlone.utils import log, log_exc

from plone.dexterity.content import Item
from docpool.base.content.contentbase import ContentBase, IContentBase

from Products.CMFCore.utils import getToolByName

from docpool.base.utils import back_references
from zope.component import adapter
from plone.dexterity.interfaces import IEditFinishedEvent
from zope.lifecycleevent.interfaces import IObjectRemovedEvent

from elan.sitrep.config import PROJECTNAME

from elan.sitrep import DocpoolMessageFactory as _


class ISRTextBlock(form.Schema, IContentBase):
    """
    """

    dexteritytextindexer.searchable('text')
    text = RichText(
        title=_(u'label_srtextblock_text', default=u'Text'),
        description=_(u'description_srtextblock_text', default=u''),
        required=False,
    )


class SRTextBlock(Item, ContentBase):
    """
    """

    security = ClassSecurityInfo()

    implements(ISRTextBlock)

    def moduleConfigs(self):
        """
        All SRModuleConfigs, where I am used
        """
        mcs = back_references(self, "textBlocks")
        return mcs

    def getSRScenarioNames(self):
        """
        Index Method
        """
        res = []
        for mod in self.moduleConfigs():
            res.extend(mod.getSRScenarioNames())
        return res

    def getSRScenarioRefs(self):
        """
        Index Method
        """
        res = []
        for mod in self.moduleConfigs():
            res.extend(mod.getSRScenarioRefs())
        return res

    def getSRPhaseNames(self):
        """
        Index method
        """
        res = []
        for mod in self.moduleConfigs():
            res.extend(mod.getSRPhaseNames())
        return res

    def getSRPhaseRefs(self):
        """
        Index method
        """
        res = []
        for mod in self.moduleConfigs():
            res.extend(mod.getSRPhaseRefs())
        return res

    def getSRModuleNames(self):
        """
        Index Method
        """
        return [mod.getId() for mod in self.moduleConfigs()]

    def getSRModuleRefs(self):
        """
        Index Method
        """
        return [mod.UID() for mod in self.moduleConfigs()]

    def createActions(self):
        sr_cat = getToolByName(self, "sr_catalog")
        sr_cat._reindexObject(self)


@adapter(ISRTextBlock, IEditFinishedEvent)
def updated(obj, event=None):
    log("SRTextBlock updated: %s" % str(obj))
    sr_cat = getToolByName(obj, "sr_catalog")
    sr_cat._reindexObject(obj)


@adapter(ISRTextBlock, IObjectRemovedEvent)
def removed(obj, event):
    log("SRTextBlock removed: %s" % str(obj))
    sr_cat = getToolByName(obj, "sr_catalog")
    op = event.oldParent
    id = event.oldName
    path = "/".join(op.getPhysicalPath()) + "/" + id
    sr_cat.uncatalog_object(path)
