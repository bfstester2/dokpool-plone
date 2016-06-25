# -*- coding: utf-8 -*-
#
# File: documentextension.py
#
# Copyright (c) 2016 by Condat AG
# Generator: ConPD2
#            http://www.condat.de
#

__author__ = ''
__docformat__ = 'plaintext'

"""Definition of the DocumentExtension content type. See documentextension.py for more
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

from Products.CMFCore.utils import getToolByName

##code-section imports
##/code-section imports 

from docpool.base.config import PROJECTNAME

from docpool.base import DocpoolMessageFactory as _

class IDocumentExtension(form.Schema):
    """
    """

##code-section interface
##/code-section interface


class DocumentExtension(Item):
    """
    """
    security = ClassSecurityInfo()
    
    implements(IDocumentExtension)
    
##code-section methods
##/code-section methods 


##code-section bottom
##/code-section bottom 
