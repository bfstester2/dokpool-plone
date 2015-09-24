# -*- coding: utf-8 -*-
#
# File: srfolder.py
#
# Copyright (c) 2015 by Condat AG
# Generator: ConPD2
#            http://www.condat.de
#

__author__ = ''
__docformat__ = 'plaintext'

"""Definition of the SRFolder content type. See srfolder.py for more
explanation on the statements below.
"""
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from zope.component import adapts
from zope import schema
from plone.directives import form, dexterity
from plone.app.textfield import RichText
from collective import dexteritytextindexer
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder
from Products.CMFPlone.utils import log, log_exc

from plone.dexterity.content import Container
from docpool.base.content.simplefolder import SimpleFolder, ISimpleFolder

from Products.CMFCore.utils import getToolByName

##code-section imports
##/code-section imports 

from elan.sitrep.config import PROJECTNAME

from elan.sitrep import ELAN_EMessageFactory as _

class ISRFolder(form.Schema, ISimpleFolder):
    """
    """

##code-section interface
    form.omitted('allowedDocTypes')
##/code-section interface


class SRFolder(Container, SimpleFolder):
    """
    """
    security = ClassSecurityInfo()
    
    implements(ISRFolder)
    
##code-section methods
##/code-section methods 

    def mySRFolder(self):
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

    def getSRFolders(self, **kwargs):
        """
        """
        args = {'portal_type':'SRFolder'}
        args.update(kwargs)
        return [obj.getObject() for obj in self.getFolderContents(args)] 

    def getSRModules(self, **kwargs):
        """
        """
        args = {'portal_type':'SRModule'}
        args.update(kwargs)
        return [obj.getObject() for obj in self.getFolderContents(args)] 

    def getSituationReports(self, **kwargs):
        """
        """
        args = {'portal_type':'SituationReport'}
        args.update(kwargs)
        return [obj.getObject() for obj in self.getFolderContents(args)] 


##code-section bottom
##/code-section bottom 
