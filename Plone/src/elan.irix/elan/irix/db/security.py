# -*- coding: utf-8 -*-
from docpool.dbaccess.interfaces import IDataSecurity
from docpool.dbaccess.interfaces import IProtectedEntityClass
from docpool.dbaccess.security import DefaultSecurity
from Products.PluggableAuthService.interfaces.authservice import IBasicUser
from zope.component import adapter
from zope.interface import implementer


class IELANProtectedEntityClass(IProtectedEntityClass):
    pass


@implementer(IDataSecurity)
@adapter(IELANProtectedEntityClass, IBasicUser)
class IRIXSecurity(DefaultSecurity):
    """
    """
    # adapts(ISubscriptionSupport)

    def __init__(self, klass, user):
        DefaultSecurity.__init__(self, klass, user)
        self.isManager = user.has_role(
            "Manager") or user.has_role("Site Administrator")

    def can_access(self):
        return self.isManager

    def can_delete(self, item):
        """
        """
        return self.isManager

    def can_delete_all(self):
        """
        """
        return self.isManager

    def can_update(self, item):
        """
        """
        return self.can_access()
