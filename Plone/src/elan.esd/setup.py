# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


version = '0.1.156'

setup(
    name='elan.esd',
    version=version,
    description="",
    long_description="""\
""",
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    author='Condat AG',
    author_email='hr@condat.de',
    url='http://www.condat.de',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['elan'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        # -*- Extra requirements: -*-
        'setuptools',
        'plone.app.dexterity [relations]',
        'collective.autopermission',
        'plone.namedfile [blobs]',
        'collective.dexteritytextindexer',
        'plone.app.contenttypes',
        'plone.app.relationfield',
    ],
    extras_require=dict(test=['loremipsum']),
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
