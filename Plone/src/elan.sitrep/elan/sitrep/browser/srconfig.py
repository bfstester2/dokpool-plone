# -*- coding: utf-8 -*-
#
# File: srconfig.py
#
# Copyright (c) 2015 by Condat AG
# Generator: ConPD2
#            http://www.condat.de
#

"""Define a browser view for the content type. In the FTI 
configured in profiles/default/types/*.xml, this is being set as the default
view of that content type.
"""


from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.memoize.instance import memoize

##code-section imports
##/code-section imports

class SRConfigView(BrowserView):
    """Default view
    """
 
    __call__ = ViewPageTemplateFile('srconfig.pt')
   
    ##code-section methods1
    ##/code-section methods1     



##code-section bottom
##/code-section bottom