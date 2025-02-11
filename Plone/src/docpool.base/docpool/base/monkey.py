# -*- coding: utf-8 -*-
from Acquisition import aq_get
from Acquisition import aq_inner
from plone.app.discussion.browser.conversation import ConversationView
from Products.CMFCore.MemberDataTool import MemberData
from Products.ZCatalog.CatalogBrains import AbstractCatalogBrain
from zope.globalrequest import getRequest

import logging
import ssl


log = logging.getLogger(__name__)


# from plone.app.controlpanel.usergroups import UsersOverviewControlPanel


# Patches for the automatic creation of group folders


def enabled(self):
    """
    Needs to be patched, so that comments are enabled for the DPDocument type.
    Normally, they cannot be enabled for a folderish type.
    """
    # print "enabled"
    from docpool.base.content.dpdocument import IDPDocument

    context = aq_inner(self.context)
    if IDPDocument.providedBy(context):
        if not context.isArchive():
            return True
        else:
            return False
    else:
        return self.original_enabled()


if not hasattr(ConversationView, "original_enabled"):
    ConversationView.original_enabled = ConversationView.enabled
    ConversationView.enabled = enabled


def getURL(self, relative=0, original=False):
    """
    Patched so we can provide special URLs for category documents in listings
    such as livesearch. The category objects are viewed within a collections (see @@dview)
    Also we make sure that sections don't get an URL, so they are not linked to in the navigation.
    """
    request = aq_get(self, 'REQUEST', None)
    if request is None:
        request = getRequest()
    if (
        # original set we ignore this special code
        (not original)
        # only valid for DPDocuments
        and self.portal_type == 'DPDocument'
        # resolveid does not exist in url
        and not request['URL'].find('resolveuid') > -1
        and not request['URL'].find('Transfers') > -1
        or 'overview' in str(request.get('myfolder_url',"/"))
    ):
        if self.cat_path:
            # This is it: we use the path of the category
            return "%s/@@dview?d=%s&disable_border=1" % (
                self.cat_path, self.UID)
        else:
            pass

    # This is the normal implementation
    return request.physicalPathToURL(self.getPath(), relative)

if not hasattr(AbstractCatalogBrain, "original_getURL"):
    AbstractCatalogBrain.original_getURL = AbstractCatalogBrain.getURL
    AbstractCatalogBrain.getURL = getURL


ssl._create_default_https_context = ssl._create_unverified_context


def setProperties(self, properties=None, **kw):
    request = aq_get(self, 'REQUEST', None)
    if request is None:
        request = getRequest()

    if request.get('HTTP_X_REQUESTED_WITH', '') == 'XMLHttpRequest':
        mapping = kw if properties is None else properties
        for key in ('login_time', 'last_login_time'):
            if key in mapping.keys():
                value = mapping.pop(key)
                log.info('Not setting property {0}: {1}'.format(key, value))

    self._orig_setProperties(properties, **kw)


MemberData._orig_setProperties = MemberData.setProperties
MemberData.setProperties = setProperties
