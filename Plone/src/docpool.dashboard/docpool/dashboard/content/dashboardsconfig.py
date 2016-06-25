# -*- coding: utf-8 -*-
#
# File: dashboardsconfig.py
#
# Copyright (c) 2016 by Condat AG
# Generator: ConPD2
#            http://www.condat.de
#

__author__ = ''
__docformat__ = 'plaintext'

"""Definition of the DashboardsConfig content type. See dashboardsconfig.py for more
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

from plone.dexterity.content import Container

from Products.CMFCore.utils import getToolByName

##code-section imports
##/code-section imports 

from docpool.dashboard.config import PROJECTNAME

from docpool.dashboard import DocpoolMessageFactory as _

class IDashboardsConfig(form.Schema):
    """
    """

##code-section interface
##/code-section interface


class DashboardsConfig(Container):
    """
    """
    security = ClassSecurityInfo()
    
    implements(IDashboardsConfig)
    
##code-section methods
##/code-section methods 

    def myDashboardsConfig(self):
        """
        """
        return self

    def getFirstChild(self):
        """
        """
        fc = self.getFolderContents()
        if len(fc) > 0:
            return fc[0].getObject()
        else:
            return None

    def getAllContentObjects(self):
        """
        """
        return [obj.getObject() for obj in self.getFolderContents()]

    def getDashboardCollections(self, **kwargs):
        """
        """
        args = {'portal_type':'DashboardCollection'}
        args.update(kwargs)
        return [obj.getObject() for obj in self.getFolderContents(args)] 


##code-section bottom
##/code-section bottom 
