# -*- coding: utf-8 -*-

from docpool.base.appregistry import registerApp
from docpool.config.local.elan import dpAdded
from docpool.config.local.elan import dpRemoved
from docpool.elan.behaviors.elandoctype import IELANDocType
from docpool.elan.behaviors.elandocument import IELANDocument
from docpool.elan.config import ELAN_APP


registerApp(
    ELAN_APP,
    u"ELAN",
    IELANDocType,
    IELANDocument,
    dpAdded,
    dpRemoved,
    icon="elan_app_icon.png",
)
