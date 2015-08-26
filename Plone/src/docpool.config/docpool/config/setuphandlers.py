# -*- coding: utf-8 -*-


def post_install(context):
    """Post install script"""
    if context.readDataFile('docpoolconfig_default.txt') is None:
        return
    # Do something during the installation of this package


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('docpoolconfig_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
