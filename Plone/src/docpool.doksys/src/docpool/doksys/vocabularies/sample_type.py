# -*- coding: utf-8 -*-
from Products.CMFPlone.utils import safe_encode
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class SampleType(object):

    def __call__(self, context=None):
        items = [
            (u'A', u'Abwasser, Reststoffe und Abfälle'),
            (u'A1', u'Kläranlage'),
            (u'A11', u'Abwasser aus Kläranlagenablauf'),
            (u'A12', u'Wasser aus Kanalisation, Kläranlagenzulauf, Regenrückhaltebecken'),
            (u'A13', u'Klärschlamm'),
            (u'A2', u'Verbrennungsanlage'),
            (u'A21', u'Filterstaub, Filterasche'),
            (u'A22', u'Kesselasche, Schlacke'),
            (u'A23', u'Feste Rückstände aus Rauchgaswäsche'),
            (u'A24', u'Flüssige Rückstände aus Rauchgaswäsche'),
            (u'A3', u'Mülldeponie'),
            (u'A31', u'Sicker- und Grundwasser'),
            (u'A32', u'Deponieoberfläche'),
            (u'A4', u'Kompostierungsanlage'),
            (u'A41', u'Kompost'),
            (u'A42', u'organische Düngemittel (aus landwirtschaftlichen Abfällen)'),
            (u'A5', u'Spezielle Reststoffe und Abfälle'),
            (u'A51', u'Luftfilter'),
            (u'A52', u'Gartenabfälle'),
            (u'A53', u'Folien'),
            (u'A54', u'sonstige spezielle Reststoffe und Abfälle'),
            (u'A55', u'Reststoffe aus der Trinkwasseraufbereitung'),
            (u'A56', u'Bauschutt'),
            (u'B', u'Boden'),
            (u'B1', u'Boden in-situ (flächenbezogene Aktivität)'),
            (u'B11', u'Boden in-situ (flächenbezogene Aktivität); Boden unversiegelt'),
            (u'B12', u'Boden in-situ (flächenbezogene Aktivität); Boden versiegelt'),
            (u'B13', u'Bodenauflage'),
            (u'B2', u'Boden in-situ (nuklidspezifische Dosisleistung)'),
            (u'B21', u'Boden in-situ (nuklidspez. Dosisleistung),Boden unversiegelt'),
            (u'B22', u'Boden in-situ (nuklidspez. Dosisleistung),Boden versiegelt'),
            (u'B3', u'Weide-/ Acker-/ Wald-/ Freizeitflächen-/ Ödland- und Gartenböden'),
            (u'B31', u'Weideböden'),
            (u'B32', u'Ackerböden'),
            (u'B33', u'Waldböden'),
            (u'B34', u'Freizeitflächenböden'),
            (u'B35', u'Ödlandböden, Brachen'),
            (u'B36', u'Gartenböden'),
            (u'F', u'Futtermittel'),
            (u'F1', u'Grünfutter (einschl. Weide- und Wiesenbewuchs)'),
            (u'F11', u'Weide- u. Wiesenbewuchs'),
            (u'F12', u'Grünfutterpflanzen (außer Weide- u. Wiesenbewuchs)'),
            (u'F2', u'Mais'),
            (u'F21', u'Mais (ganze Pflanze)'),
            (u'F3', u'Futtergetreide'),
            (u'F31', u'Futtergetreide (einschl. Maiskörner)'),
            (u'F4', u'Hackfrüchte'),
            (u'F41', u'Futterkartoffeln und Futterrüben'),
            (u'F5', u'Heu, Stroh, Cobs, Trockenmehle'),
            (u'F51', u'Heu'),
            (u'F52', u'Stroh, Cobs, Trockenmehle'),
            (u'F5Z', u'Sonstige Futtermittel'),
            (u'F6', u'Mischfuttermittelrohstoffe'),
            (u'F61', u'Maisprodukte'),
            (u'F62', u'Schrote'),
            (u'F63', u'Maniok und Tapioka'),
            (u'F7', u'Mischfuttermittel'),
            (u'F71', u'Kraftfuttermischungen'),
            (u'G', u'Gewässer'),
            (u'G1', u'Fließgewässer'),
            (u'G11', u'Wasser in Fließgewässern'),
            (u'G12', u'Schwebstoff in Fließgewässern'),
            (u'G13', u'Sediment in Fließgewässern'),
            (u'G2', u'Stehende Gewässer'),
            (u'G21', u'Wasser in stehenden Gewässern'),
            (u'G22', u'Schwebstoffe in stehenden Gewässern'),
            (u'G23', u'Sedimente in stehenden Gewässern'),
            (u'G3', u'Meer'),
            (u'G31', u'Meerwasser'),
            (u'G32', u'Schwebstoffe im Meerwasser'),
            (u'G33', u'Sedimente im Meerwasser'),
            (u'G4', u'Grundwasser'),
            (u'G41', u'Grundwasser (nicht zur Trinkwassergewinnung)'),
            (u'G5', u'Rohwasser zur Trinkwassergewinnung'),
            (u'G51', u'Rohwasser, geschützt, aus Grund- und Tiefenwasser'),
            (u'G52', u'Rohwasser, ungeschützt, aus Oberflächenwasser'),
            (u'G53', u'Zisternenwasser'),
            (u'GZ', u'Sonstige Wässer'),
            (u'GZ1', u'Wasser zur Viehtränke'),
            (u'I', u'Bio-Indikatoren, Tabak und Arzneimittel'),
            (u'I1', u'Pflanzliche Indikatoren'),
            (u'I11', u'Blätter'),
            (u'I12', u'Nadeln'),
            (u'I13', u'Gras'),
            (u'I14', u'Moose, Farne, Flechten u. Heidekraut'),
            (u'I15', u'Wasserpflanzen'),
            (u'I19', u'Gras (REI)'),
            (u'I2', u'Tabak'),
            (u'I21', u'Tabakblätter'),
            (u'I22', u'Zigaretten, Zigarren'),
            (u'I3', u'Arzneimittel'),
            (u'I31', u'Ausgangsstoffe für Arzneimittel'),
            (u'I32', u'Arzneimittelprodukte'),
            (u'L', u'Luft und Niederschlag'),
            (u'L1', u'Luft/Gammastrahlung'),
            (u'L11', u'Gamma-Ortsdosis'),
            (u'L12', u'Gamma-Ortsdosisleistung'),
            (u'L2', u'Luft/Neutronenstrahlung'),
            (u'L21', u'Neutronen-Ortsdosis'),
            (u'L22', u'Neutronen-Ortsdosisleistung'),
            (u'L3', u'Luft/Aerosole'),
            (u'L31', u'Aerosole'),
            (u'L32', u'Bilanzierungsmessung Aerosole'),
            (u'L4', u'Luft/gasförmige Komponenten (einschl. Iod)'),
            (u'L41', u'Luft/gasförmiges Iod'),
            (u'L42', u'Luft/Edelgase'),
            (u'L43', u'andere gasförmige Komponenten (außer Iod u. Edelgase)'),
            (u'L44', u'Bilanzierungsmessung Luft/Iod'),
            (u'L45', u'Bilanzierungsmessung Luft/Edelgase'),
            (u'L46', u'Bilanzierungsmessung andere gasförmige Komponenten (außer Iod und Edelgase)'),
            (u'L5', u'Niederschlag'),
            (u'L51', u'Niederschlag (Aktivitätskonzentration)'),
            (u'L52', u'nasse Niederschläge (Deposition)'),
            (u'L53', u'trockene Niederschläge (Deposition)'),
            (u'L54', u'Niederschlagsmenge'),
            (u'L6', u'Spurenmessung Luft'),
            (u'L61', u'Spurenmessung Luft - Aerosole'),
            (u'L62', u'Spurenmessung Luft - gasförmige Komponenten (einschl. Iod)'),
            (u'L63', u'Spurenmessung Luft - Edelgase'),
            (u'M', u'Meteo-Umweltbereich'),
            (u'N', u'Nahrungsmittel (einschl. Trinkwasser)'),
            (u'N1', u'Milch'),
            (u'N11', u'Sammelmilch (Kuh-)'),
            (u'N12', u'Hofmilch (Kuh-)'),
            (u'N13', u'bearbeitete Trinkmilch (Kuh-)'),
            (u'N14', u'Milch anderer Tiere (Schaf, Ziege, Stute)'),
            (u'N15', u'Humanmilch'),
            (u'N2', u'Frischgemüse (einschl. Kartoffeln und Pilze)'),
            (u'N21', u'Blattgemüse, ungeschützter Anbau'),
            (u'N22', u'Wurzelgemüse, ungeschützter Anbau'),
            (u'N23', u'Fruchtgemüse, ungeschützter Anbau'),
            (u'N24', u'Sprossgemüse, ungeschützter Anbau'),
            (u'N25', u'Kartoffeln'),
            (u'N26', u'Blattgemüse, geschützter Anbau'),
            (u'N27', u'Wurzelgemüse, geschützter Anbau'),
            (u'N28', u'Fruchtgemüse, geschützter Anbau'),
            (u'N29', u'Sprossgemüse, geschützter Anbau'),
            (u'N2A', u'Wildpilze'),
            (u'N2B', u'Kulturpilze'),
            (u'N2C', u'Sonstige Wildpilze'),
            (u'N2Y', u'Sonstiges Gemüse, ungeschützter Anbau'),
            (u'N2Z', u'Sonstiges Gemüse, geschützter Anbau'),
            (u'N3', u'Getreide'),
            (u'N31', u'Getreidekörner (Weizen-,Roggen-, Gersten-, Hafer-, Mais-, Triticalenkörner)'),
            (u'N3Z', u'Sonstige Getreidearten'),
            (u'N4', u'Obst'),
            (u'N41', u'Schalenobst (Nüsse)'),
            (u'N42', u'Kernobst'),
            (u'N43', u'Steinobst'),
            (u'N44', u'Beerenobst, ungeschützter Anbau (außer Wald-/Wildbeeren)'),
            (u'N45', u'Beerenobst, geschützter Anbau'),
            (u'N46', u'Wald-/Wildbeeren'),
            (u'N4Z', u'Sonstige Obstarten'),
            (u'N5', u'Fleisch'),
            (u'N51', u'Rindfleisch'),
            (u'N52', u'Kalbfleisch'),
            (u'N53', u'Schweinefleisch'),
            (u'N54', u'Geflügelfleisch'),
            (u'N55', u'Lammfleisch'),
            (u'N56', u'Haarwildfleisch'),
            (u'N5Z', u'Sonstiges Fleisch'),
            (u'N6', u'Fisch und Meeresfrüchte'),
            (u'N61', u'Süßwasserfisch'),
            (u'N62', u'Seefisch'),
            (u'N63', u'Meeresfrüchte'),
            (u'N64', u'Fischerzeugnisse'),
            (u'N65', u'Wasserpflanzen, Trockenprodukte'),
            (u'N7', u'Trinkwasser'),
            (u'N71', u'Reinwasser aus geschützten Rohwasservorkommen'),
            (u'N72', u'Reinwasser aus ungeschützten Rohwasservorkommen'),
            (u'N73', u'Reinwasser aus Mischrohwasser'),
            (u'N74', u'Rohwasser, geschützt, aus Grund- und Tiefenwasser (ungültig)'),
            (u'N75', u'Rohwasser, ungeschützt, aus Oberflächenwasser (ungültig)'),
            (u'N76', u'Zisternenwasser (ungültig)'),
            (u'N8', u'Gesamtnahrung, Fertiggerichte und Getränke'),
            (u'N81', u'Gesamtnahrung'),
            (u'N82', u'Säuglings- und Kleinkindernahrung'),
            (u'N83', u'Fertiggerichte, verzehrsfertig (einschl. Suppen)'),
            (u'N84', u'Fertiggerichte, Trockensubstanz (einschl. Suppen)'),
            (u'N85', u'Getränke, trinkfertig, nicht alkoholisch (einschl. Tee und Kaffee)'),
            (u'N86', u'Getränke, Trockensubstanz, nicht alkoholisch (einschl. Tee und Kaffee)'),
            (u'N87', u'Getränke, alkoholisch'),
            (u'N9', u'Nahrungsmittelprodukte'),
            (u'N91', u'Käse aus Kuhmilch'),
            (u'N92', u'Käse aus Milch anderer Tiere'),
            (u'N93', u'Milchprodukte außer Käse, Frischprodukte'),
            (u'N94', u'Milchprodukte außer Käse, Trockenprodukte'),
            (u'N95', u'Milchprodukte außer Käse, haltbar gemacht'),
            (u'N96', u'Gemüseprodukte einschl. Kartoffeln, Frischprodukte auch tiefgefroren'),
            (u'N97', u'Gemüseprodukte einschl. Kartoffeln, Trockenprodukte'),
            (u'N98', u'Gemüseprodukte einschl. Kartoffeln, haltbar gemacht'),
            (u'N99', u'Wildpilzprodukte, Frischprodukte auch tiefgefroren'),
            (u'N9A', u'Wildpilzprodukte, Trockenprodukte'),
            (u'N9B', u'Wildpilzprodukte, haltbar gemacht'),
            (u'N9C', u'Kulturpilzprodukte, Frischprodukte auch tiefgefroren'),
            (u'N9D', u'Kulturpilzprodukte, Trockenprodukte'),
            (u'N9E', u'Kulturpilzprodukte, haltbar gemacht'),
            (u'N9F', u'Getreideprodukte außer Brot'),
            (u'N9G', u'Brote und Gebäcke'),
            (u'N9H', u'Obstprodukte, Frischprodukte auch tiefgefroren'),
            (u'N9I', u'Obstprodukte, Trockenprodukte'),
            (u'N9J', u'Obstprodukte, haltbar gemacht'),
            (u'N9K', u'Fleischprodukte u. Wurstwaren, ohne Wild, Frischprod. auch tiefgefr.'),
            (u'N9L', u'Fleischprodukte u. Wurstwaren, ohne Wild, haltbar gemacht'),
            (u'N9M', u'Wildfleischprodukte u. -wurstwaren, Frischprod. auch tiefgefr.'),
            (u'N9N', u'Wildfleischprodukte u. -wurstwaren, haltbar gemacht'),
            (u'N9O', u'Fischprodukte, Frischprod. auch tiefgefr.'),
            (u'N9P', u'Fischprodukte, haltbar gemacht'),
            (u'N9Q', u'Meeresfrüchteprodukte, Frischprod. auch tiefgefr.'),
            (u'N9R', u'Meeresfrüchteprodukte, haltbar gemacht'),
            (u'NZ', u'Sonstige Nahrungsmittel'),
            (u'NZ1', u'Hühnereier'),
            (u'NZ2', u'Honig'),
            (u'NZ3', u'weitere Nahrungsmittel'),
            (u'S', u'Umweltbereiche für Störfall'),
            (u'S1', u'Luft - Störfall'),
            (u'S11', u'Luft/äußere Strahlung (Gamma-ODL) - Störfall'),
            (u'S12', u'Luft/Aerosole - Störfall'),
            (u'S13', u'Luft/gasförmiges Iod - Störfall'),
            (u'S14', u'Luft/äußere Strahlung (Gamma-OD) -Störfall'),
            (u'S2', u'Boden/-Oberfläche - Störfall'),
            (u'S21', u'Bodenoberfläche (unversiegelt, in-situ, flächenbezogene Aktivität) - Störfall'),
            (u'S22', u'Boden - Störfall'),
            (u'S23', u'Bodenoberfläche (versiegelt, in-situ, flächenbezogene Aktivität) - Störfall'),
            (u'S3', u'Pflanzen/Bewuchs - Störfall'),
            (u'S31', u'Weide- und Wiesenbewuchs - Störfall'),
            (u'S32', u'Grünfutterpflanzen (außer Weide- und Wiesenbewuchs) - Störfall'),
            (u'S4', u'Oberirdische Gewässer - Störfall'),
            (u'S41', u'Oberflächenwasser (Fließgewässer) - Störfall'),
            (u'S42', u'Oberflächenwasser (stehende Gewässer) - Störfall'),
            (u'S43', u'Oberflächenwasser (Viehtränke) - Störfall'),
            (u'SF1', u'Rindfleisch - Störfall'),
            (u'SF2', u'Kalbfleisch - Störfall'),
            (u'SF3', u'Schweinefleisch - Störfall'),
            (u'SF4', u'Geflügelfleisch - Störfall'),
            (u'SF5', u'Lammfleisch - Störfall'),
            (u'SG1', u'Blattgemüse, ungeschützter Anbau - Störfall'),
            (u'SG2', u'Wurzelgemüse, ungeschützter Anbau - Störfall'),
            (u'SG3', u'Fruchtgemüse, ungeschützter Anbau - Störfall'),
            (u'SG4', u'Sprossgemüse, ungeschützter Anbau - Störfall'),
            (u'SG5', u'Kartoffeln - Störfall'),
            (u'SG6', u'Getreidekörner (Weizen, Roggen, Gerste, Hafer, Mais, Triticale) - Störfall'),
            (u'SO1', u'Schalenobst (Nüsse) - Störfall'),
            (u'SO2', u'Kernobst - Störfall'),
            (u'SO3', u'Steinobst - Störfall'),
            (u'SO4', u'Beerenobst (außer Wald-/Wildbeeren) - Störfall'),
            (u'SO5', u'Sonstige Obstarten - Störfall'),
            (u'Z', u'Sonstige Mediengruppen'),
            (u'Z1', u'Baustoffe'),
            (u'Z11', u'mineralische Ausgangsstoffe für Baustoffe'),
            (u'Z12', u'verarbeitete mineralische Baustoffe'),
            (u'Z13', u'organische Ausgangsstoffe für Baustoffe'),
            (u'Z14', u'verarbeitete organische Baustoffe'),
            (u'Z2', u'Bodenschätze'),
            (u'Z21', u'Rohgas'),
            (u'Z22', u'Reingas'),
            (u'Z3', u'Bedarfsgegenstände und Kosmetische Mittel'),
            (u'Z31', u'Bedarfsgegenstände mit Lebensmittelkontakt'),
            (u'Z32', u'Bedarfsgegenstände zur Verpackung von Tabakerz. und kosmet. Mitteln'),
            (u'Z33', u'Bedarfsgegenstände mit Körperkontakt/ Spielwaren/ Kleidung'),
            (u'Z34', u'Bedarfsgegenstände zur Reinigung und Pflege'),
            (u'Z35', u'Kosmetische Mittel und Stoffe zu deren Herstellung'),
        ]
        terms = [SimpleTerm(value,
                            safe_encode(value),
                            u'{} {}'.format(value, title))
                 for value, title in items]
        return SimpleVocabulary(terms)


SampleTypeFactory = SampleType()
