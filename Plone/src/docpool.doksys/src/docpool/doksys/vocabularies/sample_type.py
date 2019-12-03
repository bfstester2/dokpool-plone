# -*- coding: utf-8 -*-
from docpool.doksys import _
from Products.CMFPlone.utils import safe_encode
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class SampleType(object):

    def __call__(self, context=None):
        items = [
            (u'PARK', _(u'PARK')),
            (u'PARK Modellbereiche', _(u'PARK Modellbereiche')),
            (u'Abwasser, Reststoffe  und Abfaelle', _(u'Abwasser, Reststoffe  und Abfaelle')),
            (u'Klaeranlage', _(u'Klaeranlage')),
            (u'Abwasser aus Klaeranlagenablauf', _(u'Abwasser aus Klaeranlagenablauf')),
            (u'Wasser aus Kanalisation, Klaeranlagenzulauf, Regenrueckhaltebecken', _(u'Wasser aus Kanalisation, Klaeranlagenzulauf, Regenrueckhaltebecken')),
            (u'Klaerschlamm', _(u'Klaerschlamm')),
            (u'Verbrennungsanlage', _(u'Verbrennungsanlage')),
            (u'Filterstaub, Filterasche', _(u'Filterstaub, Filterasche')),
            (u'Kesselasche, Schlacke', _(u'Kesselasche, Schlacke')),
            (u'Feste Rueckstaende aus Rauchgaswaesche', _(u'Feste Rueckstaende aus Rauchgaswaesche')),
            (u'Fluessige Rueckstaende aus Rauchgaswaesche', _(u'Fluessige Rueckstaende aus Rauchgaswaesche')),
            (u'Muelldeponie', _(u'Muelldeponie')),
            (u'Sicker- und Grundwasser', _(u'Sicker- und Grundwasser')),
            (u'Deponieoberflaeche', _(u'Deponieoberflaeche')),
            (u'Kompostierungsanlage', _(u'Kompostierungsanlage')),
            (u'Kompost', _(u'Kompost')),
            (u'organische Duengemittel (aus landwirtschaftlichen Abfaellen)', _(u'organische Duengemittel (aus landwirtschaftlichen Abfaellen)')),
            (u'Spezielle Reststoffe und Abfaelle', _(u'Spezielle Reststoffe und Abfaelle')),
            (u'Luftfilter', _(u'Luftfilter')),
            (u'Gartenabfaelle', _(u'Gartenabfaelle')),
            (u'Folien', _(u'Folien')),
            (u'sonstige spezielle Reststoffe und Abfaelle', _(u'sonstige spezielle Reststoffe und Abfaelle')),
            (u'Reststoffe aus der Trinkwasseraufbereitung', _(u'Reststoffe aus der Trinkwasseraufbereitung')),
            (u'Bauschutt', _(u'Bauschutt')),
            (u'Boden', _(u'Boden')),
            (u'Boden in-situ (flaechenbezogene Aktivitaet)', _(u'Boden in-situ (flaechenbezogene Aktivitaet)')),
            (u'Boden in-situ (flaechenbezogene Aktivitaet); Boden unversiegelt', _(u'Boden in-situ (flaechenbezogene Aktivitaet); Boden unversiegelt')),
            (u'Boden in-situ (flaechenbezogene Aktivitaet); Boden versiegelt', _(u'Boden in-situ (flaechenbezogene Aktivitaet); Boden versiegelt')),
            (u'Bodenauflage', _(u'Bodenauflage')),
            (u'Boden in-situ (nuklidspezifische Dosisleistung)', _(u'Boden in-situ (nuklidspezifische Dosisleistung)')),
            (u'Boden in-situ (nuklidspez. Dosisleistung),Boden unversiegelt', _(u'Boden in-situ (nuklidspez. Dosisleistung),Boden unversiegelt')),
            (u'Boden in-situ (nuklidspez. Dosisleistung),Boden versiegelt', _(u'Boden in-situ (nuklidspez. Dosisleistung),Boden versiegelt')),
            (u'Weide-/ Acker-/ Wald-/ Freizeitflaechen-/ oedland- und Gartenboeden', _(u'Weide-/ Acker-/ Wald-/ Freizeitflaechen-/ oedland- und Gartenboeden')),
            (u'Weideboeden', _(u'Weideboeden')),
            (u'Ackerboeden', _(u'Ackerboeden')),
            (u'Waldboeden', _(u'Waldboeden')),
            (u'Freizeitflaechenboeden', _(u'Freizeitflaechenboeden')),
            (u'oedlandboeden, Brachen', _(u'oedlandboeden, Brachen')),
            (u'Gartenboeden', _(u'Gartenboeden')),
            (u'Futtermittel', _(u'Futtermittel')),
            (u'Gruenfutter (einschl. Weide- und Wiesenbewuchs)', _(u'Gruenfutter (einschl. Weide- und Wiesenbewuchs)')),
            (u'Weide- u. Wiesenbewuchs', _(u'Weide- u. Wiesenbewuchs')),
            (u'Gruenfutterpflanzen (ausser Weide- u. Wiesenbewuchs)', _(u'Gruenfutterpflanzen (ausser Weide- u. Wiesenbewuchs)')),
            (u'Mais', _(u'Mais')),
            (u'Mais (ganze Pflanze)', _(u'Mais (ganze Pflanze)')),
            (u'Futtergetreide', _(u'Futtergetreide')),
            (u'Futtergetreide (einschl. Maiskoerner)', _(u'Futtergetreide (einschl. Maiskoerner)')),
            (u'Hackfruechte', _(u'Hackfruechte')),
            (u'Futterkartoffeln und Futterrueben', _(u'Futterkartoffeln und Futterrueben')),
            (u'Heu, Stroh, Cobs, Trockenmehle', _(u'Heu, Stroh, Cobs, Trockenmehle')),
            (u'Heu', _(u'Heu')),
            (u'Stroh, Cobs, Trockenmehle', _(u'Stroh, Cobs, Trockenmehle')),
            (u'Sonstige Futtermittel', _(u'Sonstige Futtermittel')),
            (u'Mischfuttermittelrohstoffe', _(u'Mischfuttermittelrohstoffe')),
            (u'Maisprodukte', _(u'Maisprodukte')),
            (u'Schrote', _(u'Schrote')),
            (u'Maniok und Tapioka', _(u'Maniok und Tapioka')),
            (u'Mischfuttermittel', _(u'Mischfuttermittel')),
            (u'Kraftfuttermischungen', _(u'Kraftfuttermischungen')),
            (u'Gewaesser', _(u'Gewaesser')),
            (u'Fliessgewaesser', _(u'Fliessgewaesser')),
            (u'Wasser in Fliessgewaessern', _(u'Wasser in Fliessgewaessern')),
            (u'Schwebstoff in Fliessgewaessern', _(u'Schwebstoff in Fliessgewaessern')),
            (u'Sediment in Fliessgewaessern', _(u'Sediment in Fliessgewaessern')),
            (u'Stehende Gewaesser', _(u'Stehende Gewaesser')),
            (u'Wasser in stehenden Gewaessern', _(u'Wasser in stehenden Gewaessern')),
            (u'Schwebstoffe in stehenden Gewaessern', _(u'Schwebstoffe in stehenden Gewaessern')),
            (u'Sedimente in stehenden Gewaessern', _(u'Sedimente in stehenden Gewaessern')),
            (u'Meer', _(u'Meer')),
            (u'Meerwasser', _(u'Meerwasser')),
            (u'Schwebstoffe im Meerwasser', _(u'Schwebstoffe im Meerwasser')),
            (u'Sedimente im Meerwasser', _(u'Sedimente im Meerwasser')),
            (u'Grundwasser', _(u'Grundwasser')),
            (u'Grundwasser (nicht zur Trinkwassergewinnung)', _(u'Grundwasser (nicht zur Trinkwassergewinnung)')),
            (u'Rohwasser zur Trinkwassergewinnung', _(u'Rohwasser zur Trinkwassergewinnung')),
            (u'Rohwasser, geschuetzt, aus Grund- und Tiefenwasser', _(u'Rohwasser, geschuetzt, aus Grund- und Tiefenwasser')),
            (u'Rohwasser, ungeschuetzt, aus Oberflaechenwasser', _(u'Rohwasser, ungeschuetzt, aus Oberflaechenwasser')),
            (u'Zisternenwasser', _(u'Zisternenwasser')),
            (u'Sonstige Waesser', _(u'Sonstige Waesser')),
            (u'Wasser zur Viehtraenke', _(u'Wasser zur Viehtraenke')),
            (u'Bio-Indikatoren, Tabak und Arzneimittel', _(u'Bio-Indikatoren, Tabak und Arzneimittel')),
            (u'Pflanzliche Indikatoren', _(u'Pflanzliche Indikatoren')),
            (u'Blaetter', _(u'Blaetter')),
            (u'Nadeln', _(u'Nadeln')),
            (u'Gras', _(u'Gras')),
            (u'Moose, Farne, Flechten u. Heidekraut', _(u'Moose, Farne, Flechten u. Heidekraut')),
            (u'Wasserpflanzen', _(u'Wasserpflanzen')),
            (u'Gras (REI)', _(u'Gras (REI)')),
            (u'Tabak', _(u'Tabak')),
            (u'Tabakblaetter', _(u'Tabakblaetter')),
            (u'Zigaretten, Zigarren', _(u'Zigaretten, Zigarren')),
            (u'Arzneimittel', _(u'Arzneimittel')),
            (u'Ausgangsstoffe fuer Arzneimittel', _(u'Ausgangsstoffe fuer Arzneimittel')),
            (u'Arzneimittelprodukte', _(u'Arzneimittelprodukte')),
            (u'Luft und Niederschlag', _(u'Luft und Niederschlag')),
            (u'Luft/Gammastrahlung', _(u'Luft/Gammastrahlung')),
            (u'Gamma-Ortsdosis', _(u'Gamma-Ortsdosis')),
            (u'Gamma-Ortsdosisleistung', _(u'Gamma-Ortsdosisleistung')),
            (u'Luft/Neutronenstrahlung', _(u'Luft/Neutronenstrahlung')),
            (u'Neutronen-Ortsdosis', _(u'Neutronen-Ortsdosis')),
            (u'Neutronen-Ortsdosisleistung', _(u'Neutronen-Ortsdosisleistung')),
            (u'Luft/Aerosole', _(u'Luft/Aerosole')),
            (u'Aerosole', _(u'Aerosole')),
            (u'Bilanzierungsmessung Aerosole', _(u'Bilanzierungsmessung Aerosole')),
            (u'Luft/gasfoermige Komponenten (einschl. Iod)', _(u'Luft/gasfoermige Komponenten (einschl. Iod)')),
            (u'Luft/gasfoermiges Iod', _(u'Luft/gasfoermiges Iod')),
            (u'Luft/Edelgase', _(u'Luft/Edelgase')),
            (u'andere gasfoermige Komponenten (ausser Iod u. Edelgase)', _(u'andere gasfoermige Komponenten (ausser Iod u. Edelgase)')),
            (u'Bilanzierungsmessung Luft/Iod', _(u'Bilanzierungsmessung Luft/Iod')),
            (u'Bilanzierungsmessung Luft/Edelgase', _(u'Bilanzierungsmessung Luft/Edelgase')),
            (u'Bilanzierungsmessung andere gasfoermige Komponenten (ausser Iod und Edelgase)', _(u'Bilanzierungsmessung andere gasfoermige Komponenten (ausser Iod und Edelgase)')),
            (u'Niederschlag', _(u'Niederschlag')),
            (u'Niederschlag (Aktivitaetskonzentration)', _(u'Niederschlag (Aktivitaetskonzentration)')),
            (u'nasse Niederschlaege (Deposition)', _(u'nasse Niederschlaege (Deposition)')),
            (u'trockene Niederschlaege (Deposition)', _(u'trockene Niederschlaege (Deposition)')),
            (u'Niederschlagsmenge', _(u'Niederschlagsmenge')),
            (u'Spurenmessung Luft', _(u'Spurenmessung Luft')),
            (u'Spurenmessung Luft - Aerosole', _(u'Spurenmessung Luft - Aerosole')),
            (u'Spurenmessung Luft - gasfoermige Komponenten (einschl. Iod)', _(u'Spurenmessung Luft - gasfoermige Komponenten (einschl. Iod)')),
            (u'Spurenmessung Luft - Edelgase', _(u'Spurenmessung Luft - Edelgase')),
            (u'Meteo-Umweltbereich', _(u'Meteo-Umweltbereich')),
            (u'Nahrungsmittel (einschl. Trinkwasser)', _(u'Nahrungsmittel (einschl. Trinkwasser)')),
            (u'Milch', _(u'Milch')),
            (u'Sammelmilch (Kuh-)', _(u'Sammelmilch (Kuh-)')),
            (u'Hofmilch (Kuh-)', _(u'Hofmilch (Kuh-)')),
            (u'bearbeitete Trinkmilch (Kuh-)', _(u'bearbeitete Trinkmilch (Kuh-)')),
            (u'Milch anderer Tiere (Schaf, Ziege, Stute)', _(u'Milch anderer Tiere (Schaf, Ziege, Stute)')),
            (u'Humanmilch', _(u'Humanmilch')),
            (u'Frischgemuese (einschl. Kartoffeln und Pilze)', _(u'Frischgemuese (einschl. Kartoffeln und Pilze)')),
            (u'Blattgemuese, ungeschuetzter Anbau', _(u'Blattgemuese, ungeschuetzter Anbau')),
            (u'Wurzelgemuese, ungeschuetzter Anbau', _(u'Wurzelgemuese, ungeschuetzter Anbau')),
            (u'Fruchtgemuese, ungeschuetzter Anbau', _(u'Fruchtgemuese, ungeschuetzter Anbau')),
            (u'Sprossgemuese, ungeschuetzter Anbau', _(u'Sprossgemuese, ungeschuetzter Anbau')),
            (u'Kartoffeln', _(u'Kartoffeln')),
            (u'Blattgemuese, geschuetzter Anbau', _(u'Blattgemuese, geschuetzter Anbau')),
            (u'Wurzelgemuese, geschuetzter Anbau', _(u'Wurzelgemuese, geschuetzter Anbau')),
            (u'Fruchtgemuese, geschuetzter Anbau', _(u'Fruchtgemuese, geschuetzter Anbau')),
            (u'Sprossgemuese, geschuetzter Anbau', _(u'Sprossgemuese, geschuetzter Anbau')),
            (u'Wildpilze', _(u'Wildpilze')),
            (u'Kulturpilze', _(u'Kulturpilze')),
            (u'Sonstige Wildpilze', _(u'Sonstige Wildpilze')),
            (u'Sonstiges Gemuese, ungeschuetzter Anbau', _(u'Sonstiges Gemuese, ungeschuetzter Anbau')),
            (u'Sonstiges Gemuese, geschuetzter Anbau', _(u'Sonstiges Gemuese, geschuetzter Anbau')),
            (u'Getreide', _(u'Getreide')),
            (u'Getreidekoerner (Weizen-,Roggen-, Gersten-, Hafer-, Mais-, Triticalenkoerner)', _(u'Getreidekoerner (Weizen-,Roggen-, Gersten-, Hafer-, Mais-, Triticalenkoerner)')),
            (u'Sonstige Getreidearten', _(u'Sonstige Getreidearten')),
            (u'Obst', _(u'Obst')),
            (u'Schalenobst (Nuesse)', _(u'Schalenobst (Nuesse)')),
            (u'Kernobst', _(u'Kernobst')),
            (u'Steinobst', _(u'Steinobst')),
            (u'Beerenobst, ungeschuetzter Anbau (ausser Wald-/Wildbeeren)', _(u'Beerenobst, ungeschuetzter Anbau (ausser Wald-/Wildbeeren)')),
            (u'Beerenobst, geschuetzter Anbau', _(u'Beerenobst, geschuetzter Anbau')),
            (u'Wald-/Wildbeeren', _(u'Wald-/Wildbeeren')),
            (u'Sonstige Obstarten', _(u'Sonstige Obstarten')),
            (u'Fleisch', _(u'Fleisch')),
            (u'Rindfleisch', _(u'Rindfleisch')),
            (u'Kalbfleisch', _(u'Kalbfleisch')),
            (u'Schweinefleisch', _(u'Schweinefleisch')),
            (u'Gefluegelfleisch', _(u'Gefluegelfleisch')),
            (u'Lammfleisch', _(u'Lammfleisch')),
            (u'Haarwildfleisch', _(u'Haarwildfleisch')),
            (u'Sonstiges Fleisch', _(u'Sonstiges Fleisch')),
            (u'Fisch und Meeresfruechte', _(u'Fisch und Meeresfruechte')),
            (u'Suesswasserfisch', _(u'Suesswasserfisch')),
            (u'Seefisch', _(u'Seefisch')),
            (u'Meeresfruechte', _(u'Meeresfruechte')),
            (u'Fischerzeugnisse', _(u'Fischerzeugnisse')),
            (u'Wasserpflanzen, Trockenprodukte', _(u'Wasserpflanzen, Trockenprodukte')),
            (u'Trinkwasser', _(u'Trinkwasser')),
            (u'Reinwasser aus geschuetzten Rohwasservorkommen', _(u'Reinwasser aus geschuetzten Rohwasservorkommen')),
            (u'Reinwasser aus ungeschuetzten Rohwasservorkommen', _(u'Reinwasser aus ungeschuetzten Rohwasservorkommen')),
            (u'Reinwasser aus Mischrohwasser', _(u'Reinwasser aus Mischrohwasser')),
            (u'Rohwasser, geschuetzt, aus Grund- und Tiefenwasser (ungueltig)', _(u'Rohwasser, geschuetzt, aus Grund- und Tiefenwasser (ungueltig)')),
            (u'Rohwasser, ungeschuetzt, aus Oberflaechenwasser (ungueltig)', _(u'Rohwasser, ungeschuetzt, aus Oberflaechenwasser (ungueltig)')),
            (u'Zisternenwasser (ungueltig)', _(u'Zisternenwasser (ungueltig)')),
            (u'Gesamtnahrung, Fertiggerichte und Getraenke', _(u'Gesamtnahrung, Fertiggerichte und Getraenke')),
            (u'Gesamtnahrung', _(u'Gesamtnahrung')),
            (u'Saeuglings- und Kleinkindernahrung', _(u'Saeuglings- und Kleinkindernahrung')),
            (u'Fertiggerichte, verzehrsfertig (einschl. Suppen)', _(u'Fertiggerichte, verzehrsfertig (einschl. Suppen)')),
            (u'Fertiggerichte, Trockensubstanz (einschl. Suppen)', _(u'Fertiggerichte, Trockensubstanz (einschl. Suppen)')),
            (u'Getraenke, trinkfertig, nicht alkoholisch (einschl. Tee und Kaffee)', _(u'Getraenke, trinkfertig, nicht alkoholisch (einschl. Tee und Kaffee)')),
            (u'Getraenke, Trockensubstanz, nicht alkoholisch (einschl. Tee und Kaffee)', _(u'Getraenke, Trockensubstanz, nicht alkoholisch (einschl. Tee und Kaffee)')),
            (u'Getraenke, alkoholisch', _(u'Getraenke, alkoholisch')),
            (u'Nahrungsmittelprodukte', _(u'Nahrungsmittelprodukte')),
            (u'Kaese aus Kuhmilch', _(u'Kaese aus Kuhmilch')),
            (u'Kaese aus Milch anderer Tiere', _(u'Kaese aus Milch anderer Tiere')),
            (u'Milchprodukte ausser Kaese, Frischprodukte', _(u'Milchprodukte ausser Kaese, Frischprodukte')),
            (u'Milchprodukte ausser Kaese, Trockenprodukte', _(u'Milchprodukte ausser Kaese, Trockenprodukte')),
            (u'Milchprodukte ausser Kaese, haltbar gemacht', _(u'Milchprodukte ausser Kaese, haltbar gemacht')),
            (u'Gemueseprodukte einschl. Kartoffeln, Frischprodukte auch tiefgefroren', _(u'Gemueseprodukte einschl. Kartoffeln, Frischprodukte auch tiefgefroren')),
            (u'Gemueseprodukte einschl. Kartoffeln, Trockenprodukte', _(u'Gemueseprodukte einschl. Kartoffeln, Trockenprodukte')),
            (u'Gemueseprodukte einschl. Kartoffeln, haltbar gemacht', _(u'Gemueseprodukte einschl. Kartoffeln, haltbar gemacht')),
            (u'Wildpilzprodukte, Frischprodukte auch tiefgefroren', _(u'Wildpilzprodukte, Frischprodukte auch tiefgefroren')),
            (u'Wildpilzprodukte, Trockenprodukte', _(u'Wildpilzprodukte, Trockenprodukte')),
            (u'Wildpilzprodukte, haltbar gemacht', _(u'Wildpilzprodukte, haltbar gemacht')),
            (u'Kulturpilzprodukte, Frischprodukte auch tiefgefroren', _(u'Kulturpilzprodukte, Frischprodukte auch tiefgefroren')),
            (u'Kulturpilzprodukte, Trockenprodukte', _(u'Kulturpilzprodukte, Trockenprodukte')),
            (u'Kulturpilzprodukte, haltbar gemacht', _(u'Kulturpilzprodukte, haltbar gemacht')),
            (u'Getreideprodukte ausser Brot', _(u'Getreideprodukte ausser Brot')),
            (u'Brote und Gebaecke', _(u'Brote und Gebaecke')),
            (u'Obstprodukte, Frischprodukte auch tiefgefroren', _(u'Obstprodukte, Frischprodukte auch tiefgefroren')),
            (u'Obstprodukte, Trockenprodukte', _(u'Obstprodukte, Trockenprodukte')),
            (u'Obstprodukte, haltbar gemacht', _(u'Obstprodukte, haltbar gemacht')),
            (u'Fleischprodukte u. Wurstwaren, ohne Wild, Frischprod. auch tiefgefr.', _(u'Fleischprodukte u. Wurstwaren, ohne Wild, Frischprod. auch tiefgefr.')),
            (u'Fleischprodukte u. Wurstwaren, ohne Wild, haltbar gemacht', _(u'Fleischprodukte u. Wurstwaren, ohne Wild, haltbar gemacht')),
            (u'Wildfleischprodukte u. -wurstwaren, Frischprod. auch tiefgefr.', _(u'Wildfleischprodukte u. -wurstwaren, Frischprod. auch tiefgefr.')),
            (u'Wildfleischprodukte u. -wurstwaren, haltbar gemacht', _(u'Wildfleischprodukte u. -wurstwaren, haltbar gemacht')),
            (u'Fischprodukte, Frischprod. auch tiefgefr.', _(u'Fischprodukte, Frischprod. auch tiefgefr.')),
            (u'Fischprodukte, haltbar gemacht', _(u'Fischprodukte, haltbar gemacht')),
            (u'Meeresfruechteprodukte, Frischprod. auch tiefgefr.', _(u'Meeresfruechteprodukte, Frischprod. auch tiefgefr.')),
            (u'Meeresfruechteprodukte, haltbar gemacht', _(u'Meeresfruechteprodukte, haltbar gemacht')),
            (u'Sonstige Nahrungsmittel', _(u'Sonstige Nahrungsmittel')),
            (u'Huehnereier', _(u'Huehnereier')),
            (u'Honig', _(u'Honig')),
            (u'weitere Nahrungsmittel', _(u'weitere Nahrungsmittel')),
            (u'Umweltbereiche fuer Stoerfall', _(u'Umweltbereiche fuer Stoerfall')),
            (u'Luft - Stoerfall', _(u'Luft - Stoerfall')),
            (u'Luft/aeussere Strahlung (Gamma-ODL) - Stoerfall', _(u'Luft/aeussere Strahlung (Gamma-ODL) - Stoerfall')),
            (u'Luft/Aerosole - Stoerfall', _(u'Luft/Aerosole - Stoerfall')),
            (u'Luft/gasfoermiges Iod - Stoerfall', _(u'Luft/gasfoermiges Iod - Stoerfall')),
            (u'Luft/aeussere Strahlung (Gamma-OD) -Stoerfall', _(u'Luft/aeussere Strahlung (Gamma-OD) -Stoerfall')),
            (u'Boden/-Oberflaeche - Stoerfall', _(u'Boden/-Oberflaeche - Stoerfall')),
            (u'Bodenoberflaeche (unversiegelt, in-situ, flaechenbezogene Aktivitaet) - Stoerfall', _(u'Bodenoberflaeche (unversiegelt, in-situ, flaechenbezogene Aktivitaet) - Stoerfall')),
            (u'Boden - Stoerfall', _(u'Boden - Stoerfall')),
            (u'Bodenoberflaeche (versiegelt, in-situ, flaechenbezogene Aktivitaet) - Stoerfall', _(u'Bodenoberflaeche (versiegelt, in-situ, flaechenbezogene Aktivitaet) - Stoerfall')),
            (u'Pflanzen/Bewuchs - Stoerfall', _(u'Pflanzen/Bewuchs - Stoerfall')),
            (u'Weide- und Wiesenbewuchs - Stoerfall', _(u'Weide- und Wiesenbewuchs - Stoerfall')),
            (u'Gruenfutterpflanzen (ausser Weide- und Wiesenbewuchs) - Stoerfall', _(u'Gruenfutterpflanzen (ausser Weide- und Wiesenbewuchs) - Stoerfall')),
            (u'Oberirdische Gewaesser - Stoerfall', _(u'Oberirdische Gewaesser - Stoerfall')),
            (u'Oberflaechenwasser (Fliessgewaesser) - Stoerfall', _(u'Oberflaechenwasser (Fliessgewaesser) - Stoerfall')),
            (u'Oberflaechenwasser (stehende Gewaesser) - Stoerfall', _(u'Oberflaechenwasser (stehende Gewaesser) - Stoerfall')),
            (u'Oberflaechenwasser (Viehtraenke) - Stoerfall', _(u'Oberflaechenwasser (Viehtraenke) - Stoerfall')),
            (u'Rindfleisch - Stoerfall', _(u'Rindfleisch - Stoerfall')),
            (u'Kalbfleisch - Stoerfall', _(u'Kalbfleisch - Stoerfall')),
            (u'Schweinefleisch - Stoerfall', _(u'Schweinefleisch - Stoerfall')),
            (u'Gefluegelfleisch - Stoerfall', _(u'Gefluegelfleisch - Stoerfall')),
            (u'Lammfleisch - Stoerfall', _(u'Lammfleisch - Stoerfall')),
            (u'Blattgemuese, ungeschuetzter Anbau - Stoerfall', _(u'Blattgemuese, ungeschuetzter Anbau - Stoerfall')),
            (u'Wurzelgemuese, ungeschuetzter Anbau - Stoerfall', _(u'Wurzelgemuese, ungeschuetzter Anbau - Stoerfall')),
            (u'Fruchtgemuese, ungeschuetzter Anbau - Stoerfall', _(u'Fruchtgemuese, ungeschuetzter Anbau - Stoerfall')),
            (u'Sprossgemuese, ungeschuetzter Anbau - Stoerfall', _(u'Sprossgemuese, ungeschuetzter Anbau - Stoerfall')),
            (u'Kartoffeln - Stoerfall', _(u'Kartoffeln - Stoerfall')),
            (u'Getreidekoerner (Weizen, Roggen, Gerste, Hafer, Mais, Triticale) - Stoerfall', _(u'Getreidekoerner (Weizen, Roggen, Gerste, Hafer, Mais, Triticale) - Stoerfall')),
            (u'Schalenobst (Nuesse) - Stoerfall', _(u'Schalenobst (Nuesse) - Stoerfall')),
            (u'Kernobst - Stoerfall', _(u'Kernobst - Stoerfall')),
            (u'Steinobst - Stoerfall', _(u'Steinobst - Stoerfall')),
            (u'Beerenobst (ausser Wald-/Wildbeeren) - Stoerfall', _(u'Beerenobst (ausser Wald-/Wildbeeren) - Stoerfall')),
            (u'Sonstige Obstarten - Stoerfall', _(u'Sonstige Obstarten - Stoerfall')),
            (u'Sonstige Mediengruppen', _(u'Sonstige Mediengruppen')),
            (u'Baustoffe', _(u'Baustoffe')),
            (u'mineralische Ausgangsstoffe fuer Baustoffe', _(u'mineralische Ausgangsstoffe fuer Baustoffe')),
            (u'verarbeitete mineralische Baustoffe', _(u'verarbeitete mineralische Baustoffe')),
            (u'organische Ausgangsstoffe fuer Baustoffe', _(u'organische Ausgangsstoffe fuer Baustoffe')),
            (u'verarbeitete organische Baustoffe', _(u'verarbeitete organische Baustoffe')),
            (u'Bodenschaetze', _(u'Bodenschaetze')),
            (u'Rohgas', _(u'Rohgas')),
            (u'Reingas', _(u'Reingas')),
            (u'Bedarfsgegenstaende und Kosmetische Mittel', _(u'Bedarfsgegenstaende und Kosmetische Mittel')),
            (u'Bedarfsgegenstaende mit Lebensmittelkontakt', _(u'Bedarfsgegenstaende mit Lebensmittelkontakt')),
            (u'Bedarfsgegenstaende zur Verpackung von Tabakerz. und kosmet. Mitteln', _(u'Bedarfsgegenstaende zur Verpackung von Tabakerz. und kosmet. Mitteln')),
            (u'Bedarfsgegenstaende mit Koerperkontakt/ Spielwaren/ Kleidung', _(u'Bedarfsgegenstaende mit Koerperkontakt/ Spielwaren/ Kleidung')),
            (u'Bedarfsgegenstaende zur Reinigung und Pflege', _(u'Bedarfsgegenstaende zur Reinigung und Pflege')),
            (u'Kosmetische Mittel und Stoffe zu deren Herstellung', _(u'Kosmetische Mittel und Stoffe zu deren Herstellung')),
        ]
        terms = [SimpleTerm(value, safe_encode(value), title)
                 for value, title in items]
        return SimpleVocabulary(terms)


SampleTypeFactory = SampleType()
