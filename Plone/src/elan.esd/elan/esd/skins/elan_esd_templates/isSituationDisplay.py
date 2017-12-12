## Python Script "isSituationDisplay"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
from Products.Archetypes.utils import shasattr
from docpool.elan.config import ELAN_APP

if shasattr(context, "myDocumentPool", acquire=True):
    return context.isActive(ELAN_APP)
else:
    return False 