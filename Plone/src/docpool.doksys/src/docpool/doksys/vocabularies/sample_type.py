# -*- coding: utf-8 -*-

# from plone import api
from docpool.doksys import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class SampleType(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(u'PARK', _(u'PARK')),
            VocabItem(u'PARK Modellbereiche', _(u'PARK Modellbereiche')),
            VocabItem(
                u'Abwasser, Reststoffe  und Abfaelle',
                _(u'Abwasser, Reststoffe  und Abfaelle'),
            ),
            VocabItem(u'Klaeranlage', _(u'Klaeranlage')),
            VocabItem(
                u'Abwasser aus Klaeranlagenablauf',
                _(u'Abwasser aus Klaeranlagenablauf'),
            ),
            VocabItem(
                u'Wasser aus Kanalisation, Klaeranlagenzulauf, Regenrueckhaltebecken',
                _(
                    u'Wasser aus Kanalisation, Klaeranlagenzulauf, Regenrueckhaltebecken'
                ),
            ),
            VocabItem(u'Klaerschlamm', _(u'Klaerschlamm')),
            VocabItem(u'Verbrennungsanlage', _(u'Verbrennungsanlage')),
            VocabItem(
                u'Filterstaub, Filterasche',
                _(u'Filterstaub, Filterasche')),
            VocabItem(u'Kesselasche, Schlacke', _(u'Kesselasche, Schlacke')),
            VocabItem(
                u'Feste Rueckstaende aus Rauchgaswaesche',
                _(u'Feste Rueckstaende aus Rauchgaswaesche'),
            ),
            VocabItem(
                u'Fluessige Rueckstaende aus Rauchgaswaesche',
                _(u'Fluessige Rueckstaende aus Rauchgaswaesche'),
            ),
            VocabItem(u'Muelldeponie', _(u'Muelldeponie')),
            VocabItem(
                u'Sicker- und Grundwasser',
                _(u'Sicker- und Grundwasser')),
            VocabItem(u'Deponieoberflaeche', _(u'Deponieoberflaeche')),
            VocabItem(u'Kompostierungsanlage', _(u'Kompostierungsanlage')),
            VocabItem(u'Kompost', _(u'Kompost')),
            VocabItem(
                u'organische Duengemittel (aus landwirtschaftlichen Abfaellen)',
                _(u'organische Duengemittel (aus landwirtschaftlichen Abfaellen)'),
            ),
            VocabItem(
                u'Spezielle Reststoffe und Abfaelle',
                _(u'Spezielle Reststoffe und Abfaelle'),
            ),
            VocabItem(u'Luftfilter', _(u'Luftfilter')),
            VocabItem(u'Gartenabfaelle', _(u'Gartenabfaelle')),
            VocabItem(u'Folien', _(u'Folien')),
            VocabItem(
                u'sonstige spezielle Reststoffe und Abfaelle',
                _(u'sonstige spezielle Reststoffe und Abfaelle'),
            ),
            VocabItem(
                u'Reststoffe aus der Trinkwasseraufbereitung',
                _(u'Reststoffe aus der Trinkwasseraufbereitung'),
            ),
            VocabItem(u'Bauschutt', _(u'Bauschutt')),
            VocabItem(u'Boden', _(u'Boden')),
            VocabItem(
                u'Boden in-situ (flaechenbezogene Aktivitaet)',
                _(u'Boden in-situ (flaechenbezogene Aktivitaet)'),
            ),
            VocabItem(
                u'Boden in-situ (flaechenbezogene Aktivitaet); Boden unversiegelt',
                _(u'Boden in-situ (flaechenbezogene Aktivitaet); Boden unversiegelt'),
            ),
            VocabItem(
                u'Boden in-situ (flaechenbezogene Aktivitaet); Boden versiegelt',
                _(u'Boden in-situ (flaechenbezogene Aktivitaet); Boden versiegelt'),
            ),
            VocabItem(u'Bodenauflage', _(u'Bodenauflage')),
            VocabItem(
                u'Boden in-situ (nuklidspezifische Dosisleistung)',
                _(u'Boden in-situ (nuklidspezifische Dosisleistung)'),
            ),
            VocabItem(
                u'Boden in-situ (nuklidspez. Dosisleistung),Boden unversiegelt',
                _(u'Boden in-situ (nuklidspez. Dosisleistung),Boden unversiegelt'),
            ),
            VocabItem(
                u'Boden in-situ (nuklidspez. Dosisleistung),Boden versiegelt',
                _(u'Boden in-situ (nuklidspez. Dosisleistung),Boden versiegelt'),
            ),
            VocabItem(
                u'Weide-/ Acker-/ Wald-/ Freizeitflaechen-/ oedland- und Gartenboeden',
                _(
                    u'Weide-/ Acker-/ Wald-/ Freizeitflaechen-/ oedland- und Gartenboeden'
                ),
            ),
            VocabItem(u'Weideboeden', _(u'Weideboeden')),
            VocabItem(u'Ackerboeden', _(u'Ackerboeden')),
            VocabItem(u'Waldboeden', _(u'Waldboeden')),
            VocabItem(u'Freizeitflaechenboeden', _(u'Freizeitflaechenboeden')),
            VocabItem(u'oedlandboeden, Brachen', _(u'oedlandboeden, Brachen')),
            VocabItem(u'Gartenboeden', _(u'Gartenboeden')),
            VocabItem(u'Futtermittel', _(u'Futtermittel')),
            VocabItem(
                u'Gruenfutter (einschl. Weide- und Wiesenbewuchs)',
                _(u'Gruenfutter (einschl. Weide- und Wiesenbewuchs)'),
            ),
            VocabItem(
                u'Weide- u. Wiesenbewuchs',
                _(u'Weide- u. Wiesenbewuchs')),
            VocabItem(
                u'Gruenfutterpflanzen (ausser Weide- u. Wiesenbewuchs)',
                _(u'Gruenfutterpflanzen (ausser Weide- u. Wiesenbewuchs)'),
            ),
            VocabItem(u'Mais', _(u'Mais')),
            VocabItem(u'Mais (ganze Pflanze)', _(u'Mais (ganze Pflanze)')),
            VocabItem(u'Futtergetreide', _(u'Futtergetreide')),
            VocabItem(
                u'Futtergetreide (einschl. Maiskoerner)',
                _(u'Futtergetreide (einschl. Maiskoerner)'),
            ),
            VocabItem(u'Hackfruechte', _(u'Hackfruechte')),
            VocabItem(
                u'Futterkartoffeln und Futterrueben',
                _(u'Futterkartoffeln und Futterrueben'),
            ),
            VocabItem(
                u'Heu, Stroh, Cobs, Trockenmehle', _(
                    u'Heu, Stroh, Cobs, Trockenmehle')
            ),
            VocabItem(u'Heu', _(u'Heu')),
            VocabItem(
                u'Stroh, Cobs, Trockenmehle',
                _(u'Stroh, Cobs, Trockenmehle')),
            VocabItem(u'Sonstige Futtermittel', _(u'Sonstige Futtermittel')),
            VocabItem(
                u'Mischfuttermittelrohstoffe',
                _(u'Mischfuttermittelrohstoffe')),
            VocabItem(u'Maisprodukte', _(u'Maisprodukte')),
            VocabItem(u'Schrote', _(u'Schrote')),
            VocabItem(u'Maniok und Tapioka', _(u'Maniok und Tapioka')),
            VocabItem(u'Mischfuttermittel', _(u'Mischfuttermittel')),
            VocabItem(u'Kraftfuttermischungen', _(u'Kraftfuttermischungen')),
            VocabItem(u'Gewaesser', _(u'Gewaesser')),
            VocabItem(u'Fliessgewaesser', _(u'Fliessgewaesser')),
            VocabItem(
                u'Wasser in Fliessgewaessern',
                _(u'Wasser in Fliessgewaessern')),
            VocabItem(
                u'Schwebstoff in Fliessgewaessern',
                _(u'Schwebstoff in Fliessgewaessern'),
            ),
            VocabItem(
                u'Sediment in Fliessgewaessern', _(
                    u'Sediment in Fliessgewaessern')
            ),
            VocabItem(u'Stehende Gewaesser', _(u'Stehende Gewaesser')),
            VocabItem(
                u'Wasser in stehenden Gewaessern', _(
                    u'Wasser in stehenden Gewaessern')
            ),
            VocabItem(
                u'Schwebstoffe in stehenden Gewaessern',
                _(u'Schwebstoffe in stehenden Gewaessern'),
            ),
            VocabItem(
                u'Sedimente in stehenden Gewaessern',
                _(u'Sedimente in stehenden Gewaessern'),
            ),
            VocabItem(u'Meer', _(u'Meer')),
            VocabItem(u'Meerwasser', _(u'Meerwasser')),
            VocabItem(
                u'Schwebstoffe im Meerwasser',
                _(u'Schwebstoffe im Meerwasser')),
            VocabItem(
                u'Sedimente im Meerwasser',
                _(u'Sedimente im Meerwasser')),
            VocabItem(u'Grundwasser', _(u'Grundwasser')),
            VocabItem(
                u'Grundwasser (nicht zur Trinkwassergewinnung)',
                _(u'Grundwasser (nicht zur Trinkwassergewinnung)'),
            ),
            VocabItem(
                u'Rohwasser zur Trinkwassergewinnung',
                _(u'Rohwasser zur Trinkwassergewinnung'),
            ),
            VocabItem(
                u'Rohwasser, geschuetzt, aus Grund- und Tiefenwasser',
                _(u'Rohwasser, geschuetzt, aus Grund- und Tiefenwasser'),
            ),
            VocabItem(
                u'Rohwasser, ungeschuetzt, aus Oberflaechenwasser',
                _(u'Rohwasser, ungeschuetzt, aus Oberflaechenwasser'),
            ),
            VocabItem(u'Zisternenwasser', _(u'Zisternenwasser')),
            VocabItem(u'Sonstige Waesser', _(u'Sonstige Waesser')),
            VocabItem(u'Wasser zur Viehtraenke', _(u'Wasser zur Viehtraenke')),
            VocabItem(
                u'Bio-Indikatoren, Tabak und Arzneimittel',
                _(u'Bio-Indikatoren, Tabak und Arzneimittel'),
            ),
            VocabItem(
                u'Pflanzliche Indikatoren',
                _(u'Pflanzliche Indikatoren')),
            VocabItem(u'Blaetter', _(u'Blaetter')),
            VocabItem(u'Nadeln', _(u'Nadeln')),
            VocabItem(u'Gras', _(u'Gras')),
            VocabItem(
                u'Moose, Farne, Flechten u. Heidekraut',
                _(u'Moose, Farne, Flechten u. Heidekraut'),
            ),
            VocabItem(u'Wasserpflanzen', _(u'Wasserpflanzen')),
            VocabItem(u'Gras (REI)', _(u'Gras (REI)')),
            VocabItem(u'Tabak', _(u'Tabak')),
            VocabItem(u'Tabakblaetter', _(u'Tabakblaetter')),
            VocabItem(u'Zigaretten, Zigarren', _(u'Zigaretten, Zigarren')),
            VocabItem(u'Arzneimittel', _(u'Arzneimittel')),
            VocabItem(
                u'Ausgangsstoffe fuer Arzneimittel',
                _(u'Ausgangsstoffe fuer Arzneimittel'),
            ),
            VocabItem(u'Arzneimittelprodukte', _(u'Arzneimittelprodukte')),
            VocabItem(u'Luft und Niederschlag', _(u'Luft und Niederschlag')),
            VocabItem(u'Luft/Gammastrahlung', _(u'Luft/Gammastrahlung')),
            VocabItem(u'Gamma-Ortsdosis', _(u'Gamma-Ortsdosis')),
            VocabItem(
                u'Gamma-Ortsdosisleistung',
                _(u'Gamma-Ortsdosisleistung')),
            VocabItem(
                u'Luft/Neutronenstrahlung',
                _(u'Luft/Neutronenstrahlung')),
            VocabItem(u'Neutronen-Ortsdosis', _(u'Neutronen-Ortsdosis')),
            VocabItem(
                u'Neutronen-Ortsdosisleistung', _(
                    u'Neutronen-Ortsdosisleistung')
            ),
            VocabItem(u'Luft/Aerosole', _(u'Luft/Aerosole')),
            VocabItem(u'Aerosole', _(u'Aerosole')),
            VocabItem(
                u'Bilanzierungsmessung Aerosole', _(
                    u'Bilanzierungsmessung Aerosole')
            ),
            VocabItem(
                u'Luft/gasfoermige Komponenten (einschl. Iod)',
                _(u'Luft/gasfoermige Komponenten (einschl. Iod)'),
            ),
            VocabItem(u'Luft/gasfoermiges Iod', _(u'Luft/gasfoermiges Iod')),
            VocabItem(u'Luft/Edelgase', _(u'Luft/Edelgase')),
            VocabItem(
                u'andere gasfoermige Komponenten (ausser Iod u. Edelgase)',
                _(u'andere gasfoermige Komponenten (ausser Iod u. Edelgase)'),
            ),
            VocabItem(
                u'Bilanzierungsmessung Luft/Iod', _(
                    u'Bilanzierungsmessung Luft/Iod')
            ),
            VocabItem(
                u'Bilanzierungsmessung Luft/Edelgase',
                _(u'Bilanzierungsmessung Luft/Edelgase'),
            ),
            VocabItem(
                u'Bilanzierungsmessung andere gasfoermige Komponenten (ausser Iod und Edelgase)',
                _(
                    u'Bilanzierungsmessung andere gasfoermige Komponenten (ausser Iod und Edelgase)'
                ),
            ),
            VocabItem(u'Niederschlag', _(u'Niederschlag')),
            VocabItem(
                u'Niederschlag (Aktivitaetskonzentration)',
                _(u'Niederschlag (Aktivitaetskonzentration)'),
            ),
            VocabItem(
                u'nasse Niederschlaege (Deposition)',
                _(u'nasse Niederschlaege (Deposition)'),
            ),
            VocabItem(
                u'trockene Niederschlaege (Deposition)',
                _(u'trockene Niederschlaege (Deposition)'),
            ),
            VocabItem(u'Niederschlagsmenge', _(u'Niederschlagsmenge')),
            VocabItem(u'Spurenmessung Luft', _(u'Spurenmessung Luft')),
            VocabItem(
                u'Spurenmessung Luft - Aerosole', _(
                    u'Spurenmessung Luft - Aerosole')
            ),
            VocabItem(
                u'Spurenmessung Luft - gasfoermige Komponenten (einschl. Iod)',
                _(u'Spurenmessung Luft - gasfoermige Komponenten (einschl. Iod)'),
            ),
            VocabItem(
                u'Spurenmessung Luft - Edelgase', _(
                    u'Spurenmessung Luft - Edelgase')
            ),
            VocabItem(u'Meteo-Umweltbereich', _(u'Meteo-Umweltbereich')),
            VocabItem(
                u'Nahrungsmittel (einschl. Trinkwasser)',
                _(u'Nahrungsmittel (einschl. Trinkwasser)'),
            ),
            VocabItem(u'Milch', _(u'Milch')),
            VocabItem(u'Sammelmilch (Kuh-)', _(u'Sammelmilch (Kuh-)')),
            VocabItem(u'Hofmilch (Kuh-)', _(u'Hofmilch (Kuh-)')),
            VocabItem(
                u'bearbeitete Trinkmilch (Kuh-)', _(
                    u'bearbeitete Trinkmilch (Kuh-)')
            ),
            VocabItem(
                u'Milch anderer Tiere (Schaf, Ziege, Stute)',
                _(u'Milch anderer Tiere (Schaf, Ziege, Stute)'),
            ),
            VocabItem(u'Humanmilch', _(u'Humanmilch')),
            VocabItem(
                u'Frischgemuese (einschl. Kartoffeln und Pilze)',
                _(u'Frischgemuese (einschl. Kartoffeln und Pilze)'),
            ),
            VocabItem(
                u'Blattgemuese, ungeschuetzter Anbau',
                _(u'Blattgemuese, ungeschuetzter Anbau'),
            ),
            VocabItem(
                u'Wurzelgemuese, ungeschuetzter Anbau',
                _(u'Wurzelgemuese, ungeschuetzter Anbau'),
            ),
            VocabItem(
                u'Fruchtgemuese, ungeschuetzter Anbau',
                _(u'Fruchtgemuese, ungeschuetzter Anbau'),
            ),
            VocabItem(
                u'Sprossgemuese, ungeschuetzter Anbau',
                _(u'Sprossgemuese, ungeschuetzter Anbau'),
            ),
            VocabItem(u'Kartoffeln', _(u'Kartoffeln')),
            VocabItem(
                u'Blattgemuese, geschuetzter Anbau',
                _(u'Blattgemuese, geschuetzter Anbau'),
            ),
            VocabItem(
                u'Wurzelgemuese, geschuetzter Anbau',
                _(u'Wurzelgemuese, geschuetzter Anbau'),
            ),
            VocabItem(
                u'Fruchtgemuese, geschuetzter Anbau',
                _(u'Fruchtgemuese, geschuetzter Anbau'),
            ),
            VocabItem(
                u'Sprossgemuese, geschuetzter Anbau',
                _(u'Sprossgemuese, geschuetzter Anbau'),
            ),
            VocabItem(u'Wildpilze', _(u'Wildpilze')),
            VocabItem(u'Kulturpilze', _(u'Kulturpilze')),
            VocabItem(u'Sonstige Wildpilze', _(u'Sonstige Wildpilze')),
            VocabItem(
                u'Sonstiges Gemuese, ungeschuetzter Anbau',
                _(u'Sonstiges Gemuese, ungeschuetzter Anbau'),
            ),
            VocabItem(
                u'Sonstiges Gemuese, geschuetzter Anbau',
                _(u'Sonstiges Gemuese, geschuetzter Anbau'),
            ),
            VocabItem(u'Getreide', _(u'Getreide')),
            VocabItem(
                u'Getreidekoerner (Weizen-,Roggen-, Gersten-, Hafer-, Mais-, Triticalenkoerner)',
                _(
                    u'Getreidekoerner (Weizen-,Roggen-, Gersten-, Hafer-, Mais-, Triticalenkoerner)'
                ),
            ),
            VocabItem(u'Sonstige Getreidearten', _(u'Sonstige Getreidearten')),
            VocabItem(u'Obst', _(u'Obst')),
            VocabItem(u'Schalenobst (Nuesse)', _(u'Schalenobst (Nuesse)')),
            VocabItem(u'Kernobst', _(u'Kernobst')),
            VocabItem(u'Steinobst', _(u'Steinobst')),
            VocabItem(
                u'Beerenobst, ungeschuetzter Anbau (ausser Wald-/Wildbeeren)',
                _(u'Beerenobst, ungeschuetzter Anbau (ausser Wald-/Wildbeeren)'),
            ),
            VocabItem(
                u'Beerenobst, geschuetzter Anbau', _(
                    u'Beerenobst, geschuetzter Anbau')
            ),
            VocabItem(u'Wald-/Wildbeeren', _(u'Wald-/Wildbeeren')),
            VocabItem(u'Sonstige Obstarten', _(u'Sonstige Obstarten')),
            VocabItem(u'Fleisch', _(u'Fleisch')),
            VocabItem(u'Rindfleisch', _(u'Rindfleisch')),
            VocabItem(u'Kalbfleisch', _(u'Kalbfleisch')),
            VocabItem(u'Schweinefleisch', _(u'Schweinefleisch')),
            VocabItem(u'Gefluegelfleisch', _(u'Gefluegelfleisch')),
            VocabItem(u'Lammfleisch', _(u'Lammfleisch')),
            VocabItem(u'Haarwildfleisch', _(u'Haarwildfleisch')),
            VocabItem(u'Sonstiges Fleisch', _(u'Sonstiges Fleisch')),
            VocabItem(
                u'Fisch und Meeresfruechte',
                _(u'Fisch und Meeresfruechte')),
            VocabItem(u'Suesswasserfisch', _(u'Suesswasserfisch')),
            VocabItem(u'Seefisch', _(u'Seefisch')),
            VocabItem(u'Meeresfruechte', _(u'Meeresfruechte')),
            VocabItem(u'Fischerzeugnisse', _(u'Fischerzeugnisse')),
            VocabItem(
                u'Wasserpflanzen, Trockenprodukte',
                _(u'Wasserpflanzen, Trockenprodukte'),
            ),
            VocabItem(u'Trinkwasser', _(u'Trinkwasser')),
            VocabItem(
                u'Reinwasser aus geschuetzten Rohwasservorkommen',
                _(u'Reinwasser aus geschuetzten Rohwasservorkommen'),
            ),
            VocabItem(
                u'Reinwasser aus ungeschuetzten Rohwasservorkommen',
                _(u'Reinwasser aus ungeschuetzten Rohwasservorkommen'),
            ),
            VocabItem(
                u'Reinwasser aus Mischrohwasser', _(
                    u'Reinwasser aus Mischrohwasser')
            ),
            VocabItem(
                u'Rohwasser, geschuetzt, aus Grund- und Tiefenwasser (ungueltig)',
                _(u'Rohwasser, geschuetzt, aus Grund- und Tiefenwasser (ungueltig)'),
            ),
            VocabItem(
                u'Rohwasser, ungeschuetzt, aus Oberflaechenwasser (ungueltig)',
                _(u'Rohwasser, ungeschuetzt, aus Oberflaechenwasser (ungueltig)'),
            ),
            VocabItem(
                u'Zisternenwasser (ungueltig)', _(
                    u'Zisternenwasser (ungueltig)')
            ),
            VocabItem(
                u'Gesamtnahrung, Fertiggerichte und Getraenke',
                _(u'Gesamtnahrung, Fertiggerichte und Getraenke'),
            ),
            VocabItem(u'Gesamtnahrung', _(u'Gesamtnahrung')),
            VocabItem(
                u'Saeuglings- und Kleinkindernahrung',
                _(u'Saeuglings- und Kleinkindernahrung'),
            ),
            VocabItem(
                u'Fertiggerichte, verzehrsfertig (einschl. Suppen)',
                _(u'Fertiggerichte, verzehrsfertig (einschl. Suppen)'),
            ),
            VocabItem(
                u'Fertiggerichte, Trockensubstanz (einschl. Suppen)',
                _(u'Fertiggerichte, Trockensubstanz (einschl. Suppen)'),
            ),
            VocabItem(
                u'Getraenke, trinkfertig, nicht alkoholisch (einschl. Tee und Kaffee)',
                _(
                    u'Getraenke, trinkfertig, nicht alkoholisch (einschl. Tee und Kaffee)'
                ),
            ),
            VocabItem(
                u'Getraenke, Trockensubstanz, nicht alkoholisch (einschl. Tee und Kaffee)',
                _(
                    u'Getraenke, Trockensubstanz, nicht alkoholisch (einschl. Tee und Kaffee)'
                ),
            ),
            VocabItem(u'Getraenke, alkoholisch', _(u'Getraenke, alkoholisch')),
            VocabItem(u'Nahrungsmittelprodukte', _(u'Nahrungsmittelprodukte')),
            VocabItem(u'Kaese aus Kuhmilch', _(u'Kaese aus Kuhmilch')),
            VocabItem(
                u'Kaese aus Milch anderer Tiere', _(
                    u'Kaese aus Milch anderer Tiere')
            ),
            VocabItem(
                u'Milchprodukte ausser Kaese, Frischprodukte',
                _(u'Milchprodukte ausser Kaese, Frischprodukte'),
            ),
            VocabItem(
                u'Milchprodukte ausser Kaese, Trockenprodukte',
                _(u'Milchprodukte ausser Kaese, Trockenprodukte'),
            ),
            VocabItem(
                u'Milchprodukte ausser Kaese, haltbar gemacht',
                _(u'Milchprodukte ausser Kaese, haltbar gemacht'),
            ),
            VocabItem(
                u'Gemueseprodukte einschl. Kartoffeln, Frischprodukte auch tiefgefroren',
                _(
                    u'Gemueseprodukte einschl. Kartoffeln, Frischprodukte auch tiefgefroren'
                ),
            ),
            VocabItem(
                u'Gemueseprodukte einschl. Kartoffeln, Trockenprodukte',
                _(u'Gemueseprodukte einschl. Kartoffeln, Trockenprodukte'),
            ),
            VocabItem(
                u'Gemueseprodukte einschl. Kartoffeln, haltbar gemacht',
                _(u'Gemueseprodukte einschl. Kartoffeln, haltbar gemacht'),
            ),
            VocabItem(
                u'Wildpilzprodukte, Frischprodukte auch tiefgefroren',
                _(u'Wildpilzprodukte, Frischprodukte auch tiefgefroren'),
            ),
            VocabItem(
                u'Wildpilzprodukte, Trockenprodukte',
                _(u'Wildpilzprodukte, Trockenprodukte'),
            ),
            VocabItem(
                u'Wildpilzprodukte, haltbar gemacht',
                _(u'Wildpilzprodukte, haltbar gemacht'),
            ),
            VocabItem(
                u'Kulturpilzprodukte, Frischprodukte auch tiefgefroren',
                _(u'Kulturpilzprodukte, Frischprodukte auch tiefgefroren'),
            ),
            VocabItem(
                u'Kulturpilzprodukte, Trockenprodukte',
                _(u'Kulturpilzprodukte, Trockenprodukte'),
            ),
            VocabItem(
                u'Kulturpilzprodukte, haltbar gemacht',
                _(u'Kulturpilzprodukte, haltbar gemacht'),
            ),
            VocabItem(
                u'Getreideprodukte ausser Brot', _(
                    u'Getreideprodukte ausser Brot')
            ),
            VocabItem(u'Brote und Gebaecke', _(u'Brote und Gebaecke')),
            VocabItem(
                u'Obstprodukte, Frischprodukte auch tiefgefroren',
                _(u'Obstprodukte, Frischprodukte auch tiefgefroren'),
            ),
            VocabItem(
                u'Obstprodukte, Trockenprodukte', _(
                    u'Obstprodukte, Trockenprodukte')
            ),
            VocabItem(
                u'Obstprodukte, haltbar gemacht', _(
                    u'Obstprodukte, haltbar gemacht')
            ),
            VocabItem(
                u'Fleischprodukte u. Wurstwaren, ohne Wild, Frischprod. auch tiefgefr.',
                _(
                    u'Fleischprodukte u. Wurstwaren, ohne Wild, Frischprod. auch tiefgefr.'
                ),
            ),
            VocabItem(
                u'Fleischprodukte u. Wurstwaren, ohne Wild, haltbar gemacht',
                _(u'Fleischprodukte u. Wurstwaren, ohne Wild, haltbar gemacht'),
            ),
            VocabItem(
                u'Wildfleischprodukte u. -wurstwaren, Frischprod. auch tiefgefr.',
                _(u'Wildfleischprodukte u. -wurstwaren, Frischprod. auch tiefgefr.'),
            ),
            VocabItem(
                u'Wildfleischprodukte u. -wurstwaren, haltbar gemacht',
                _(u'Wildfleischprodukte u. -wurstwaren, haltbar gemacht'),
            ),
            VocabItem(
                u'Fischprodukte, Frischprod. auch tiefgefr.',
                _(u'Fischprodukte, Frischprod. auch tiefgefr.'),
            ),
            VocabItem(
                u'Fischprodukte, haltbar gemacht', _(
                    u'Fischprodukte, haltbar gemacht')
            ),
            VocabItem(
                u'Meeresfruechteprodukte, Frischprod. auch tiefgefr.',
                _(u'Meeresfruechteprodukte, Frischprod. auch tiefgefr.'),
            ),
            VocabItem(
                u'Meeresfruechteprodukte, haltbar gemacht',
                _(u'Meeresfruechteprodukte, haltbar gemacht'),
            ),
            VocabItem(
                u'Sonstige Nahrungsmittel',
                _(u'Sonstige Nahrungsmittel')),
            VocabItem(u'Huehnereier', _(u'Huehnereier')),
            VocabItem(u'Honig', _(u'Honig')),
            VocabItem(u'weitere Nahrungsmittel', _(u'weitere Nahrungsmittel')),
            VocabItem(
                u'Umweltbereiche fuer Stoerfall', _(
                    u'Umweltbereiche fuer Stoerfall')
            ),
            VocabItem(u'Luft - Stoerfall', _(u'Luft - Stoerfall')),
            VocabItem(
                u'Luft/aeussere Strahlung (Gamma-ODL) - Stoerfall',
                _(u'Luft/aeussere Strahlung (Gamma-ODL) - Stoerfall'),
            ),
            VocabItem(
                u'Luft/Aerosole - Stoerfall',
                _(u'Luft/Aerosole - Stoerfall')),
            VocabItem(
                u'Luft/gasfoermiges Iod - Stoerfall',
                _(u'Luft/gasfoermiges Iod - Stoerfall'),
            ),
            VocabItem(
                u'Luft/aeussere Strahlung (Gamma-OD) -Stoerfall',
                _(u'Luft/aeussere Strahlung (Gamma-OD) -Stoerfall'),
            ),
            VocabItem(
                u'Boden/-Oberflaeche - Stoerfall', _(
                    u'Boden/-Oberflaeche - Stoerfall')
            ),
            VocabItem(
                u'Bodenoberflaeche (unversiegelt, in-situ, flaechenbezogene Aktivitaet) - Stoerfall',
                _(
                    u'Bodenoberflaeche (unversiegelt, in-situ, flaechenbezogene Aktivitaet) - Stoerfall'
                ),
            ),
            VocabItem(u'Boden - Stoerfall', _(u'Boden - Stoerfall')),
            VocabItem(
                u'Bodenoberflaeche (versiegelt, in-situ, flaechenbezogene Aktivitaet) - Stoerfall',
                _(
                    u'Bodenoberflaeche (versiegelt, in-situ, flaechenbezogene Aktivitaet) - Stoerfall'
                ),
            ),
            VocabItem(
                u'Pflanzen/Bewuchs - Stoerfall', _(
                    u'Pflanzen/Bewuchs - Stoerfall')
            ),
            VocabItem(
                u'Weide- und Wiesenbewuchs - Stoerfall',
                _(u'Weide- und Wiesenbewuchs - Stoerfall'),
            ),
            VocabItem(
                u'Gruenfutterpflanzen (ausser Weide- und Wiesenbewuchs) - Stoerfall',
                _(u'Gruenfutterpflanzen (ausser Weide- und Wiesenbewuchs) - Stoerfall'),
            ),
            VocabItem(
                u'Oberirdische Gewaesser - Stoerfall',
                _(u'Oberirdische Gewaesser - Stoerfall'),
            ),
            VocabItem(
                u'Oberflaechenwasser (Fliessgewaesser) - Stoerfall',
                _(u'Oberflaechenwasser (Fliessgewaesser) - Stoerfall'),
            ),
            VocabItem(
                u'Oberflaechenwasser (stehende Gewaesser) - Stoerfall',
                _(u'Oberflaechenwasser (stehende Gewaesser) - Stoerfall'),
            ),
            VocabItem(
                u'Oberflaechenwasser (Viehtraenke) - Stoerfall',
                _(u'Oberflaechenwasser (Viehtraenke) - Stoerfall'),
            ),
            VocabItem(
                u'Rindfleisch - Stoerfall',
                _(u'Rindfleisch - Stoerfall')),
            VocabItem(
                u'Kalbfleisch - Stoerfall',
                _(u'Kalbfleisch - Stoerfall')),
            VocabItem(
                u'Schweinefleisch - Stoerfall', _(
                    u'Schweinefleisch - Stoerfall')
            ),
            VocabItem(
                u'Gefluegelfleisch - Stoerfall', _(
                    u'Gefluegelfleisch - Stoerfall')
            ),
            VocabItem(
                u'Lammfleisch - Stoerfall',
                _(u'Lammfleisch - Stoerfall')),
            VocabItem(
                u'Blattgemuese, ungeschuetzter Anbau - Stoerfall',
                _(u'Blattgemuese, ungeschuetzter Anbau - Stoerfall'),
            ),
            VocabItem(
                u'Wurzelgemuese, ungeschuetzter Anbau - Stoerfall',
                _(u'Wurzelgemuese, ungeschuetzter Anbau - Stoerfall'),
            ),
            VocabItem(
                u'Fruchtgemuese, ungeschuetzter Anbau - Stoerfall',
                _(u'Fruchtgemuese, ungeschuetzter Anbau - Stoerfall'),
            ),
            VocabItem(
                u'Sprossgemuese, ungeschuetzter Anbau - Stoerfall',
                _(u'Sprossgemuese, ungeschuetzter Anbau - Stoerfall'),
            ),
            VocabItem(u'Kartoffeln - Stoerfall', _(u'Kartoffeln - Stoerfall')),
            VocabItem(
                u'Getreidekoerner (Weizen, Roggen, Gerste, Hafer, Mais, Triticale) - Stoerfall',
                _(
                    u'Getreidekoerner (Weizen, Roggen, Gerste, Hafer, Mais, Triticale) - Stoerfall'
                ),
            ),
            VocabItem(
                u'Schalenobst (Nuesse) - Stoerfall',
                _(u'Schalenobst (Nuesse) - Stoerfall'),
            ),
            VocabItem(u'Kernobst - Stoerfall', _(u'Kernobst - Stoerfall')),
            VocabItem(u'Steinobst - Stoerfall', _(u'Steinobst - Stoerfall')),
            VocabItem(
                u'Beerenobst (ausser Wald-/Wildbeeren) - Stoerfall',
                _(u'Beerenobst (ausser Wald-/Wildbeeren) - Stoerfall'),
            ),
            VocabItem(
                u'Sonstige Obstarten - Stoerfall', _(
                    u'Sonstige Obstarten - Stoerfall')
            ),
            VocabItem(u'Sonstige Mediengruppen', _(u'Sonstige Mediengruppen')),
            VocabItem(u'Baustoffe', _(u'Baustoffe')),
            VocabItem(
                u'mineralische Ausgangsstoffe fuer Baustoffe',
                _(u'mineralische Ausgangsstoffe fuer Baustoffe'),
            ),
            VocabItem(
                u'verarbeitete mineralische Baustoffe',
                _(u'verarbeitete mineralische Baustoffe'),
            ),
            VocabItem(
                u'organische Ausgangsstoffe fuer Baustoffe',
                _(u'organische Ausgangsstoffe fuer Baustoffe'),
            ),
            VocabItem(
                u'verarbeitete organische Baustoffe',
                _(u'verarbeitete organische Baustoffe'),
            ),
            VocabItem(u'Bodenschaetze', _(u'Bodenschaetze')),
            VocabItem(u'Rohgas', _(u'Rohgas')),
            VocabItem(u'Reingas', _(u'Reingas')),
            VocabItem(
                u'Bedarfsgegenstaende und Kosmetische Mittel',
                _(u'Bedarfsgegenstaende und Kosmetische Mittel'),
            ),
            VocabItem(
                u'Bedarfsgegenstaende mit Lebensmittelkontakt',
                _(u'Bedarfsgegenstaende mit Lebensmittelkontakt'),
            ),
            VocabItem(
                u'Bedarfsgegenstaende zur Verpackung von Tabakerz. und kosmet. Mitteln',
                _(
                    u'Bedarfsgegenstaende zur Verpackung von Tabakerz. und kosmet. Mitteln'
                ),
            ),
            VocabItem(
                u'Bedarfsgegenstaende mit Koerperkontakt/ Spielwaren/ Kleidung',
                _(u'Bedarfsgegenstaende mit Koerperkontakt/ Spielwaren/ Kleidung'),
            ),
            VocabItem(
                u'Bedarfsgegenstaende zur Reinigung und Pflege',
                _(u'Bedarfsgegenstaende zur Reinigung und Pflege'),
            ),
            VocabItem(
                u'Kosmetische Mittel und Stoffe zu deren Herstellung',
                _(u'Kosmetische Mittel und Stoffe zu deren Herstellung'),
            ),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token, token=item.token.encode('utf'), title=item.value
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


SampleTypeFactory = SampleType()
