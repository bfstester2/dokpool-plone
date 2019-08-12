# -*- coding: utf-8 -*-
#
# File: dashboardsconfig.py
#
# Copyright (c) 2016 by Bundesamt für Strahlenschutz
# Generator: ConPD2
#            http://www.condat.de
#

__author__ = ''
__docformat__ = 'plaintext'

"""Definition of the DashboardsConfig content type. See dashboardsconfig.py for more
explanation on the statements below.
"""
from AccessControl import ClassSecurityInfo
from plone.dexterity.content import Container
from plone.directives import form
from zope.interface import implements


class IDashboardsConfig(form.Schema):
    """
    """


class DashboardsConfig(Container):
    """
    """

    security = ClassSecurityInfo()

    implements(IDashboardsConfig)

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
        args = {'portal_type': 'DashboardCollection'}
        args.update(kwargs)
        return [obj.getObject() for obj in self.getFolderContents(args)]
