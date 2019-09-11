# -*- coding: utf-8 -*-

from docpool.base.appregistry import registerApp
from docpool.rei.behaviors.reidoc import IREIDoc
from docpool.rei.behaviors.reitype import IREIType
from docpool.rei.config import REI_APP

# This logic should eventually be bundled in the global docpool.config
# module to allow for easy customization
from docpool.rei.local.rei import dpAdded
from docpool.rei.local.rei import dpRemoved


# TODO: register any app specific type extension, doc extension, methods
# to be executed when docpools are created
registerApp(
    REI_APP,
    u"REI",
    IREIType,
    IREIDoc,
    dpAdded,
    dpRemoved,
    icon="rei_app_icon.png",
    implicit=False,
)
