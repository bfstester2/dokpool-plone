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
class Dom(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(
                u'74 _deposition_ground_gamma surface activity_2 h',
                _(u'74 _deposition_ground_gamma surface activity_2 h'),
            ),
            VocabItem(
                u'75 _deposition_ground_gamma surface activity_1 d',
                _(u'75 _deposition_ground_gamma surface activity_1 d'),
            ),
            VocabItem(
                u'76 _deposition_ground_gamma surface activity_1 week',
                _(u'76 _deposition_ground_gamma surface activity_1 week'),
            ),
            VocabItem(
                u'77 _deposition_ground_gamma surface activity_1 month',
                _(u'77 _deposition_ground_gamma surface activity_1 month'),
            ),
            VocabItem(
                u'81 _deposition_ground_beta surface activity, long lived_1 d',
                _(u'81 _deposition_ground_beta surface activity, long lived_1 d'),
            ),
            VocabItem(
                u'82 _deposition_ground_beta surface activity, after 24h_1 d',
                _(u'82 _deposition_ground_beta surface activity, after 24h_1 d'),
            ),
            VocabItem(
                u'84 _deposition_ground_beta surface activity_2 h',
                _(u'84 _deposition_ground_beta surface activity_2 h'),
            ),
            VocabItem(
                u'85 _deposition_ground_beta surface activity_1 d',
                _(u'85 _deposition_ground_beta surface activity_1 d'),
            ),
            VocabItem(
                u'86 _deposition_ground_beta surface activity_1 week',
                _(u'86 _deposition_ground_beta surface activity_1 week'),
            ),
            VocabItem(
                u'87 _deposition_ground_beta surface activity_1 month',
                _(u'87 _deposition_ground_beta surface activity_1 month'),
            ),
            VocabItem(
                u'94 _deposition_ground_alpha surface activity_2 h',
                _(u'94 _deposition_ground_alpha surface activity_2 h'),
            ),
            VocabItem(
                u'95 _deposition_ground_alpha surface activity_1 d',
                _(u'95 _deposition_ground_alpha surface activity_1 d'),
            ),
            VocabItem(
                u'96 _deposition_ground_alpha surface activity_1 week',
                _(u'96 _deposition_ground_alpha surface activity_1 week'),
            ),
            VocabItem(
                u'97 _deposition_ground_alpha surface activity_1 month',
                _(u'97 _deposition_ground_alpha surface activity_1 month'),
            ),
            VocabItem(
                u'100 ___gross dose rate_1 min', _(u'100 ___gross dose rate_1 min')
            ),
            VocabItem(
                u'101 ___gross dose rate_10 min', _(u'101 ___gross dose rate_10 min')
            ),
            VocabItem(
                u'102 ___gross dose rate_30 min', _(u'102 ___gross dose rate_30 min')
            ),
            VocabItem(u'103 ___gross dose rate_1 h', _(u'103 ___gross dose rate_1 h')),
            VocabItem(u'104 ___gross dose rate_2 h', _(u'104 ___gross dose rate_2 h')),
            VocabItem(u'105 ___gross dose rate_1 d', _(u'105 ___gross dose rate_1 d')),
            VocabItem(
                u'107 ___gross dose rate_1 month', _(u'107 ___gross dose rate_1 month')
            ),
            VocabItem(
                u'109 ___gross dose rate_1 year', _(u'109 ___gross dose rate_1 year')
            ),
            VocabItem(
                u'110 ___high gross dose rate_', _(u'110 ___high gross dose rate_')
            ),
            VocabItem(
                u'111 ___high gross dose rate_10 min',
                _(u'111 ___high gross dose rate_10 min'),
            ),
            VocabItem(u'120 ___net dose rate_', _(u'120 ___net dose rate_')),
            VocabItem(
                u'121 ___net dose rate_10 min', _(u'121 ___net dose rate_10 min')
            ),
            VocabItem(u'123 ___net dose rate_1 h', _(u'123 ___net dose rate_1 h')),
            VocabItem(u'124 ___net dose rate_2 h', _(u'124 ___net dose rate_2 h')),
            VocabItem(u'125 ___net dose rate_1 d', _(u'125 ___net dose rate_1 d')),
            VocabItem(u'130 ___cosmic dose rate_', _(u'130 ___cosmic dose rate_')),
            VocabItem(
                u'131 ___cosmic dose rate_10 min', _(u'131 ___cosmic dose rate_10 min')
            ),
            VocabItem(
                u'134 ___cosmic dose rate_2 h', _(u'134 ___cosmic dose rate_2 h')
            ),
            VocabItem(
                u'135 ___cosmic dose rate_1 d', _(u'135 ___cosmic dose rate_1 d')
            ),
            VocabItem(
                u'140 ___terrestrial dose rate_', _(u'140 ___terrestrial dose rate_')
            ),
            VocabItem(
                u'141 ___terrestrial dose rate_10 min',
                _(u'141 ___terrestrial dose rate_10 min'),
            ),
            VocabItem(
                u'144 ___terrestrial dose rate_2 h',
                _(u'144 ___terrestrial dose rate_2 h'),
            ),
            VocabItem(
                u'145 ___terrestrial dose rate_1 d',
                _(u'145 ___terrestrial dose rate_1 d'),
            ),
            VocabItem(
                u'150 __ground_nuclide-spec. dose rate_',
                _(u'150 __ground_nuclide-spec. dose rate_'),
            ),
            VocabItem(
                u'152 __ground_nuclide-spec. dose rate_30 min',
                _(u'152 __ground_nuclide-spec. dose rate_30 min'),
            ),
            VocabItem(
                u'153 __ground_nuclide-spec. dose rate_1 h',
                _(u'153 __ground_nuclide-spec. dose rate_1 h'),
            ),
            VocabItem(
                u'154 __ground_nuclide-spec. dose rate_2 h',
                _(u'154 __ground_nuclide-spec. dose rate_2 h'),
            ),
            VocabItem(u'155 ___dose rate_', _(u'155 ___dose rate_')),
            VocabItem(
                u'156 ___dose rate low energy _', _(u'156 ___dose rate low energy _')
            ),
            VocabItem(
                u'157 ___dose rate intermediate energy _',
                _(u'157 ___dose rate intermediate energy _'),
            ),
            VocabItem(
                u'160 _in situ_ground_gamma surface activity wet_',
                _(u'160 _in situ_ground_gamma surface activity wet_'),
            ),
            VocabItem(
                u'161 _in situ_ground_gamma surface activity wet_10 min',
                _(u'161 _in situ_ground_gamma surface activity wet_10 min'),
            ),
            VocabItem(
                u'162 _in situ_ground_gamma surface activity wet_30 min',
                _(u'162 _in situ_ground_gamma surface activity wet_30 min'),
            ),
            VocabItem(
                u'163 _in situ_ground_gamma surface activity wet_1 h',
                _(u'163 _in situ_ground_gamma surface activity wet_1 h'),
            ),
            VocabItem(
                u'164 _in situ_ground_gamma surface activity wet_2 h',
                _(u'164 _in situ_ground_gamma surface activity wet_2 h'),
            ),
            VocabItem(
                u'167 _in situ_ground_gamma surface activity wet_1 month',
                _(u'167 _in situ_ground_gamma surface activity wet_1 month'),
            ),
            VocabItem(
                u'170 _in situ_ground_gamma surface activity_',
                _(u'170 _in situ_ground_gamma surface activity_'),
            ),
            VocabItem(
                u'171 _in situ_ground_gamma surface activity_10 min',
                _(u'171 _in situ_ground_gamma surface activity_10 min'),
            ),
            VocabItem(
                u'172 _in situ_ground_gamma surface activity_30 min',
                _(u'172 _in situ_ground_gamma surface activity_30 min'),
            ),
            VocabItem(
                u'173 _in situ_ground_gamma surface activity_1 h',
                _(u'173 _in situ_ground_gamma surface activity_1 h'),
            ),
            VocabItem(
                u'174 _in situ_ground_gamma surface activity_2 h',
                _(u'174 _in situ_ground_gamma surface activity_2 h'),
            ),
            VocabItem(
                u'177 _in situ_ground_gamma surface activity_1 month',
                _(u'177 _in situ_ground_gamma surface activity_1 month'),
            ),
            VocabItem(
                u'180 _in situ_ground_gamma surface act. Net_',
                _(u'180 _in situ_ground_gamma surface act. Net_'),
            ),
            VocabItem(
                u'181 _in situ_ground_gamma surface act. Net_10 min',
                _(u'181 _in situ_ground_gamma surface act. Net_10 min'),
            ),
            VocabItem(
                u'182 _in situ_ground_gamma surface act. Net_30 min',
                _(u'182 _in situ_ground_gamma surface act. Net_30 min'),
            ),
            VocabItem(
                u'183 _in situ_ground_gamma surface act. Net_1 h',
                _(u'183 _in situ_ground_gamma surface act. Net_1 h'),
            ),
            VocabItem(
                u'184 _in situ_ground_gamma surface act. Net_2 h',
                _(u'184 _in situ_ground_gamma surface act. Net_2 h'),
            ),
            VocabItem(
                u'187 _in situ_ground_gamma surface act. Net_1 month',
                _(u'187 _in situ_ground_gamma surface act. Net_1 month'),
            ),
            VocabItem(
                u'191 __ground_gamma surface activity_',
                _(u'191 __ground_gamma surface activity_'),
            ),
            VocabItem(
                u'192 _calculated_ground_gamma surface activity_',
                _(u'192 _calculated_ground_gamma surface activity_'),
            ),
            VocabItem(
                u'195 __ground_gamma surface activity concent._',
                _(u'195 __ground_gamma surface activity concent._'),
            ),
            VocabItem(u'199 __ground__', _(u'199 __ground__')),
            VocabItem(
                u'200 _air_aerosol particles_gamma activity concent._',
                _(u'200 _air_aerosol particles_gamma activity concent._'),
            ),
            VocabItem(
                u'201 _air_aerosol particles_gamma activity concent._10 min',
                _(u'201 _air_aerosol particles_gamma activity concent._10 min'),
            ),
            VocabItem(
                u'202 _air_aerosol particles_gamma activity concent._30 min',
                _(u'202 _air_aerosol particles_gamma activity concent._30 min'),
            ),
            VocabItem(
                u'203 _air_aerosol particles_gamma activity concent._1 h',
                _(u'203 _air_aerosol particles_gamma activity concent._1 h'),
            ),
            VocabItem(
                u'204 _air_aerosol particles_gamma activity concent._2 h',
                _(u'204 _air_aerosol particles_gamma activity concent._2 h'),
            ),
            VocabItem(
                u'205 _air_aerosol particles_gamma activity concent._1 d',
                _(u'205 _air_aerosol particles_gamma activity concent._1 d'),
            ),
            VocabItem(
                u'206 _air_aerosol particles_gamma activity concent._1 week',
                _(u'206 _air_aerosol particles_gamma activity concent._1 week'),
            ),
            VocabItem(
                u'207 _air_aerosol particles_gamma activity concent._1 month',
                _(u'207 _air_aerosol particles_gamma activity concent._1 month'),
            ),
            VocabItem(
                u'210 _air_aerosol particles_gamma activity concent._2 weeks',
                _(u'210 _air_aerosol particles_gamma activity concent._2 weeks'),
            ),
            VocabItem(
                u'211 _air_aerosol particles_total gamma act. concent._10 min',
                _(u'211 _air_aerosol particles_total gamma act. concent._10 min'),
            ),
            VocabItem(
                u'212 _air_aerosol particles_total gamma act. concent._30 min',
                _(u'212 _air_aerosol particles_total gamma act. concent._30 min'),
            ),
            VocabItem(
                u'213 _air_aerosol particles_total gamma act. concent._1 h',
                _(u'213 _air_aerosol particles_total gamma act. concent._1 h'),
            ),
            VocabItem(
                u'214 _air_aerosol particles_total gamma act. Concent._2 h',
                _(u'214 _air_aerosol particles_total gamma act. Concent._2 h'),
            ),
            VocabItem(
                u'220 _air_aerosol particles_artificial beta activity concent._',
                _(u'220 _air_aerosol particles_artificial beta activity concent._'),
            ),
            VocabItem(
                u'221 _air_aerosol particles_artificial beta activity concent._10 min',
                _(
                    u'221 _air_aerosol particles_artificial beta activity concent._10 min'
                ),
            ),
            VocabItem(
                u'222 _air_aerosol particles_artificial beta activity concent._30 min',
                _(
                    u'222 _air_aerosol particles_artificial beta activity concent._30 min'
                ),
            ),
            VocabItem(
                u'223 _air_aerosol particles_artificial beta activity concent._1 h',
                _(u'223 _air_aerosol particles_artificial beta activity concent._1 h'),
            ),
            VocabItem(
                u'224 _air_aerosol particles_artificial beta activity concent._2 h',
                _(u'224 _air_aerosol particles_artificial beta activity concent._2 h'),
            ),
            VocabItem(
                u'225 _air_aerosol particles_artificial beta activity concent._1 d',
                _(u'225 _air_aerosol particles_artificial beta activity concent._1 d'),
            ),
            VocabItem(
                u'230 _air_aerosol particles_beta activity concent._',
                _(u'230 _air_aerosol particles_beta activity concent._'),
            ),
            VocabItem(
                u'231 _air_aerosol particles_beta activity concent._10 min',
                _(u'231 _air_aerosol particles_beta activity concent._10 min'),
            ),
            VocabItem(
                u'232 _air_aerosol particles_beta activity concent._30 min',
                _(u'232 _air_aerosol particles_beta activity concent._30 min'),
            ),
            VocabItem(
                u'233 _air_aerosol particles_beta activity concent._1 h',
                _(u'233 _air_aerosol particles_beta activity concent._1 h'),
            ),
            VocabItem(
                u'234 _air_aerosol particles_beta activity concent._2 h',
                _(u'234 _air_aerosol particles_beta activity concent._2 h'),
            ),
            VocabItem(
                u'235 _air_aerosol particles_beta activity concent._1 d',
                _(u'235 _air_aerosol particles_beta activity concent._1 d'),
            ),
            VocabItem(
                u'237 _air_aerosol particles_beta activity concent._1 month',
                _(u'237 _air_aerosol particles_beta activity concent._1 month'),
            ),
            VocabItem(
                u'241 _air_aerosol particles_total beta act.concent._10 min',
                _(u'241 _air_aerosol particles_total beta act.concent._10 min'),
            ),
            VocabItem(
                u'242 _air_aerosol particles_total beta act.concent._30 min',
                _(u'242 _air_aerosol particles_total beta act.concent._30 min'),
            ),
            VocabItem(
                u'243 _air_aerosol particles_total beta act.concent._1 h',
                _(u'243 _air_aerosol particles_total beta act.concent._1 h'),
            ),
            VocabItem(
                u'244 _air_aerosol particles_total beta act.concent._2 h',
                _(u'244 _air_aerosol particles_total beta act.concent._2 h'),
            ),
            VocabItem(
                u'245 _air_aerosol particles_total beta act.concent._1 d',
                _(u'245 _air_aerosol particles_total beta act.concent._1 d'),
            ),
            VocabItem(
                u'252 _air_aerosol particles_artificial alpha activity concent._30 min',
                _(
                    u'252 _air_aerosol particles_artificial alpha activity concent._30 min'
                ),
            ),
            VocabItem(
                u'253 _air_aerosol particles_artificial alpha activity concent._1 h',
                _(u'253 _air_aerosol particles_artificial alpha activity concent._1 h'),
            ),
            VocabItem(
                u'254 _air_aerosol particles_artificial alpha activity concent._2 h',
                _(u'254 _air_aerosol particles_artificial alpha activity concent._2 h'),
            ),
            VocabItem(
                u'255 _air_aerosol particles_artificial alpha activity concent._1 d',
                _(u'255 _air_aerosol particles_artificial alpha activity concent._1 d'),
            ),
            VocabItem(
                u'262 _air_aerosol particles_alpha activity concent._30 min',
                _(u'262 _air_aerosol particles_alpha activity concent._30 min'),
            ),
            VocabItem(
                u'264 _air_aerosol particles_alpha activity concent._2 h',
                _(u'264 _air_aerosol particles_alpha activity concent._2 h'),
            ),
            VocabItem(
                u'265 _air_aerosol particles_alpha activity concent._1 d',
                _(u'265 _air_aerosol particles_alpha activity concent._1 d'),
            ),
            VocabItem(
                u'267 _air_aerosol particles_alpha activity concent._1 month',
                _(u'267 _air_aerosol particles_alpha activity concent._1 month'),
            ),
            VocabItem(
                u'272 _air_aerosol particles_total alpha act.concent._30 min',
                _(u'272 _air_aerosol particles_total alpha act.concent._30 min'),
            ),
            VocabItem(
                u'274 _air_aerosol particles_total alpha act.concent._2 h',
                _(u'274 _air_aerosol particles_total alpha act.concent._2 h'),
            ),
            VocabItem(
                u'275 _air_aerosol particles_total alpha act.concent._1 d',
                _(u'275 _air_aerosol particles_total alpha act.concent._1 d'),
            ),
            VocabItem(
                u'281 _air_aerosol particles_beta activity concent., long lived_10 min',
                _(
                    u'281 _air_aerosol particles_beta activity concent., long lived_10 min'
                ),
            ),
            VocabItem(
                u'282 _air_aerosol particles_beta activity concent., long lived_30 min',
                _(
                    u'282 _air_aerosol particles_beta activity concent., long lived_30 min'
                ),
            ),
            VocabItem(
                u'283 _air_aerosol particles_beta activity concent., long lived_1 h',
                _(u'283 _air_aerosol particles_beta activity concent., long lived_1 h'),
            ),
            VocabItem(
                u'284 _air_aerosol particles_beta activity concent., long lived_2 h',
                _(u'284 _air_aerosol particles_beta activity concent., long lived_2 h'),
            ),
            VocabItem(
                u'285 _air_aerosol particles_beta activity concent., long lived_1 d',
                _(u'285 _air_aerosol particles_beta activity concent., long lived_1 d'),
            ),
            VocabItem(
                u'287 _air_aerosol particles_beta activity concent., long lived_1 month',
                _(
                    u'287 _air_aerosol particles_beta activity concent., long lived_1 month'
                ),
            ),
            VocabItem(
                u'289 _air_aerosol particles_beta activity concent., 10h later_2h',
                _(u'289 _air_aerosol particles_beta activity concent., 10h later_2h'),
            ),
            VocabItem(
                u'291 _air_aerosol particles_total emission_10 min',
                _(u'291 _air_aerosol particles_total emission_10 min'),
            ),
            VocabItem(
                u'292 _air_aerosol particles_total emission_30 min',
                _(u'292 _air_aerosol particles_total emission_30 min'),
            ),
            VocabItem(
                u'300 _air_iodine_activity concentration_',
                _(u'300 _air_iodine_activity concentration_'),
            ),
            VocabItem(
                u'301 _air_iodine_activity concentration_10 min',
                _(u'301 _air_iodine_activity concentration_10 min'),
            ),
            VocabItem(
                u'302 _air_iodine_activity concentration_30 min',
                _(u'302 _air_iodine_activity concentration_30 min'),
            ),
            VocabItem(
                u'304 _air_iodine_activity concentration_2 h',
                _(u'304 _air_iodine_activity concentration_2 h'),
            ),
            VocabItem(
                u'305 _air_iodine_activity concentration_1 d',
                _(u'305 _air_iodine_activity concentration_1 d'),
            ),
            VocabItem(
                u'306 _air_iodine_activity concentration_1 week',
                _(u'306 _air_iodine_activity concentration_1 week'),
            ),
            VocabItem(
                u'307 _air_iodine_activity concentration_2 weeks',
                _(u'307 _air_iodine_activity concentration_2 weeks'),
            ),
            VocabItem(
                u'309 _air_iodine_activity concentration_4 h',
                _(u'309 _air_iodine_activity concentration_4 h'),
            ),
            VocabItem(
                u'311 _air_iodine_total emission_10 min',
                _(u'311 _air_iodine_total emission_10 min'),
            ),
            VocabItem(
                u'312 _air_iodine_total emission_30 min',
                _(u'312 _air_iodine_total emission_30 min'),
            ),
            VocabItem(
                u'320 _air_noble gases_activity concentration_',
                _(u'320 _air_noble gases_activity concentration_'),
            ),
            VocabItem(
                u'321 _air_noble gases_activity concentration_10 min',
                _(u'321 _air_noble gases_activity concentration_10 min'),
            ),
            VocabItem(
                u'322 _air_noble gases_activity concentration_30 min',
                _(u'322 _air_noble gases_activity concentration_30 min'),
            ),
            VocabItem(
                u'324 _air_noble gases_activity concentration_2 h',
                _(u'324 _air_noble gases_activity concentration_2 h'),
            ),
            VocabItem(
                u'325 _air_noble gases_activity concentration_1 d',
                _(u'325 _air_noble gases_activity concentration_1 d'),
            ),
            VocabItem(
                u'327 _air_noble gases_activity concentration_1 month',
                _(u'327 _air_noble gases_activity concentration_1 month'),
            ),
            VocabItem(
                u'331 _air_noble gases_high activity concent._10 min',
                _(u'331 _air_noble gases_high activity concent._10 min'),
            ),
            VocabItem(
                u'332 _air_noble gases_high activity concent._30 min',
                _(u'332 _air_noble gases_high activity concent._30 min'),
            ),
            VocabItem(
                u'341 _air_noble gases_total emission_10 min',
                _(u'341 _air_noble gases_total emission_10 min'),
            ),
            VocabItem(
                u'342 _air_noble gases_total emission_30 min',
                _(u'342 _air_noble gases_total emission_30 min'),
            ),
            VocabItem(
                u'353 _air_aerosol particles_gamma activity_1 h',
                _(u'353 _air_aerosol particles_gamma activity_1 h'),
            ),
            VocabItem(
                u'355 _air_aerosol particles_gamma activity_1 d',
                _(u'355 _air_aerosol particles_gamma activity_1 d'),
            ),
            VocabItem(
                u'356 _air_aerosol particles_gamma activity_1 week',
                _(u'356 _air_aerosol particles_gamma activity_1 week'),
            ),
            VocabItem(
                u'357 _air_aerosol particles_gamma activity_1 month',
                _(u'357 _air_aerosol particles_gamma activity_1 month'),
            ),
            VocabItem(
                u'358 _air_aerosol particles_gamma activity_3 months',
                _(u'358 _air_aerosol particles_gamma activity_3 months'),
            ),
            VocabItem(
                u'359 _air_aerosol particles_gamma activity_1 year',
                _(u'359 _air_aerosol particles_gamma activity_1 year'),
            ),
            VocabItem(
                u'363 _air_aerosol particles_beta activity_1 h',
                _(u'363 _air_aerosol particles_beta activity_1 h'),
            ),
            VocabItem(
                u'365 _air_aerosol particles_beta activity_1 d',
                _(u'365 _air_aerosol particles_beta activity_1 d'),
            ),
            VocabItem(
                u'366 _air_aerosol particles_beta activity_1 week',
                _(u'366 _air_aerosol particles_beta activity_1 week'),
            ),
            VocabItem(
                u'367 _air_aerosol particles_beta activity_1 month',
                _(u'367 _air_aerosol particles_beta activity_1 month'),
            ),
            VocabItem(
                u'368 _air_aerosol particles_beta activity_3 months',
                _(u'368 _air_aerosol particles_beta activity_3 months'),
            ),
            VocabItem(
                u'369 _air_aerosol particles_beta activity_1 year',
                _(u'369 _air_aerosol particles_beta activity_1 year'),
            ),
            VocabItem(
                u'373 _air_aerosol particles_total beta activity_1 h',
                _(u'373 _air_aerosol particles_total beta activity_1 h'),
            ),
            VocabItem(
                u'375 _air_aerosol particles_total beta activity_1 d',
                _(u'375 _air_aerosol particles_total beta activity_1 d'),
            ),
            VocabItem(
                u'376 _air_aerosol particles_total beta activity_1 week',
                _(u'376 _air_aerosol particles_total beta activity_1 week'),
            ),
            VocabItem(
                u'377 _air_aerosol particles_total beta activity_1 month',
                _(u'377 _air_aerosol particles_total beta activity_1 month'),
            ),
            VocabItem(
                u'378 _air_aerosol particles_total beta activity_3 months',
                _(u'378 _air_aerosol particles_total beta activity_3 months'),
            ),
            VocabItem(
                u'379 _air_aerosol particles_total beta activity_1 year',
                _(u'379 _air_aerosol particles_total beta activity_1 year'),
            ),
            VocabItem(
                u'383 _air_aerosol particles_alpha activity_1 h',
                _(u'383 _air_aerosol particles_alpha activity_1 h'),
            ),
            VocabItem(
                u'385 _air_aerosol particles_alpha activity_1 d',
                _(u'385 _air_aerosol particles_alpha activity_1 d'),
            ),
            VocabItem(
                u'386 _air_aerosol particles_alpha activity_1 week',
                _(u'386 _air_aerosol particles_alpha activity_1 week'),
            ),
            VocabItem(
                u'387 _air_aerosol particles_alpha activity_1 month',
                _(u'387 _air_aerosol particles_alpha activity_1 month'),
            ),
            VocabItem(
                u'388 _air_aerosol particles_alpha activity_3 months',
                _(u'388 _air_aerosol particles_alpha activity_3 months'),
            ),
            VocabItem(
                u'389 _air_aerosol particles_alpha activity_1 year',
                _(u'389 _air_aerosol particles_alpha activity_1 year'),
            ),
            VocabItem(
                u'393 _air_aerosol particles_total alpha activity_1 h',
                _(u'393 _air_aerosol particles_total alpha activity_1 h'),
            ),
            VocabItem(
                u'395 _air_aerosol particles_total alpha activity_1 d',
                _(u'395 _air_aerosol particles_total alpha activity_1 d'),
            ),
            VocabItem(
                u'396 _air_aerosol particles_total alpha activity_1 week',
                _(u'396 _air_aerosol particles_total alpha activity_1 week'),
            ),
            VocabItem(
                u'397 _air_aerosol particles_total alpha activity_1 month',
                _(u'397 _air_aerosol particles_total alpha activity_1 month'),
            ),
            VocabItem(
                u'398 _air_aerosol particles_total alpha activity_3 months',
                _(u'398 _air_aerosol particles_total alpha activity_3 months'),
            ),
            VocabItem(
                u'399 _air_aerosol particles_total alpha activity_1 year',
                _(u'399 _air_aerosol particles_total alpha activity_1 year'),
            ),
            VocabItem(
                u'403 _air_iodine_activity_1 h', _(u'403 _air_iodine_activity_1 h')
            ),
            VocabItem(
                u'405 _air_iodine_activity_1 d', _(u'405 _air_iodine_activity_1 d')
            ),
            VocabItem(
                u'406 _air_iodine_activity_1 week',
                _(u'406 _air_iodine_activity_1 week'),
            ),
            VocabItem(
                u'407 _air_iodine_activity_1 month',
                _(u'407 _air_iodine_activity_1 month'),
            ),
            VocabItem(
                u'408 _air_iodine_activity_3 months',
                _(u'408 _air_iodine_activity_3 months'),
            ),
            VocabItem(
                u'409 _air_iodine_activity_1 year',
                _(u'409 _air_iodine_activity_1 year'),
            ),
            VocabItem(
                u'411 _air_aerosol particles_alpha activity conc., long lived_10 min',
                _(
                    u'411 _air_aerosol particles_alpha activity conc., long lived_10 min'
                ),
            ),
            VocabItem(
                u'412 _air_aerosol particles_alpha activity conc., long lived_30 min',
                _(
                    u'412 _air_aerosol particles_alpha activity conc., long lived_30 min'
                ),
            ),
            VocabItem(
                u'413 _air_aerosol particles_alpha activity conc., long lived_1 h',
                _(u'413 _air_aerosol particles_alpha activity conc., long lived_1 h'),
            ),
            VocabItem(
                u'414 _air_aerosol particles_alpha activity conc., long lived_2 h',
                _(u'414 _air_aerosol particles_alpha activity conc., long lived_2 h'),
            ),
            VocabItem(
                u'415 _air_aerosol particles_alpha activity conc., long lived_1 d',
                _(u'415 _air_aerosol particles_alpha activity conc., long lived_1 d'),
            ),
            VocabItem(
                u'417 _air_aerosol particles_alpha activity conc., long lived_1 month',
                _(
                    u'417 _air_aerosol particles_alpha activity conc., long lived_1 month'
                ),
            ),
            VocabItem(
                u'423 _air_noble gases_gamma activity_1 h',
                _(u'423 _air_noble gases_gamma activity_1 h'),
            ),
            VocabItem(
                u'425 _air_noble gases_gamma activity_1 d',
                _(u'425 _air_noble gases_gamma activity_1 d'),
            ),
            VocabItem(
                u'426 _air_noble gases_gamma activity_1 week',
                _(u'426 _air_noble gases_gamma activity_1 week'),
            ),
            VocabItem(
                u'427 _air_noble gases_gamma activity_1 month',
                _(u'427 _air_noble gases_gamma activity_1 month'),
            ),
            VocabItem(
                u'428 _air_noble gases_gamma activity_3 months',
                _(u'428 _air_noble gases_gamma activity_3 months'),
            ),
            VocabItem(
                u'429 _air_noble gases_gamma activity_1 year',
                _(u'429 _air_noble gases_gamma activity_1 year'),
            ),
            VocabItem(
                u'433 _air_noble gases_total gamma activity_1 h',
                _(u'433 _air_noble gases_total gamma activity_1 h'),
            ),
            VocabItem(
                u'435 _air_noble gases_total gamma activity_1 d',
                _(u'435 _air_noble gases_total gamma activity_1 d'),
            ),
            VocabItem(
                u'436 _air_noble gases_total gamma activity_1 week',
                _(u'436 _air_noble gases_total gamma activity_1 week'),
            ),
            VocabItem(
                u'437 _air_noble gases_total gamma activity_1 month',
                _(u'437 _air_noble gases_total gamma activity_1 month'),
            ),
            VocabItem(
                u'438 _air_noble gases_total gamma activity_3 months',
                _(u'438 _air_noble gases_total gamma activity_3 months'),
            ),
            VocabItem(
                u'439 _air_noble gases_total gamma activity_1 year',
                _(u'439 _air_noble gases_total gamma activity_1 year'),
            ),
            VocabItem(
                u'443 _air_noble gases_beta activity_1 h',
                _(u'443 _air_noble gases_beta activity_1 h'),
            ),
            VocabItem(
                u'445 _air_noble gases_beta activity_1 d',
                _(u'445 _air_noble gases_beta activity_1 d'),
            ),
            VocabItem(
                u'446 _air_noble gases_beta activity_1 week',
                _(u'446 _air_noble gases_beta activity_1 week'),
            ),
            VocabItem(
                u'447 _air_noble gases_beta activity_1 month',
                _(u'447 _air_noble gases_beta activity_1 month'),
            ),
            VocabItem(
                u'448 _air_noble gases_beta activity_3 months',
                _(u'448 _air_noble gases_beta activity_3 months'),
            ),
            VocabItem(
                u'449 _air_noble gases_beta activity_1 year',
                _(u'449 _air_noble gases_beta activity_1 year'),
            ),
            VocabItem(
                u'453 _air_noble gases_total beta activity_1 h',
                _(u'453 _air_noble gases_total beta activity_1 h'),
            ),
            VocabItem(
                u'455 _air_noble gases_total beta activity_1 d',
                _(u'455 _air_noble gases_total beta activity_1 d'),
            ),
            VocabItem(
                u'456 _air_noble gases_total beta activity_1 week',
                _(u'456 _air_noble gases_total beta activity_1 week'),
            ),
            VocabItem(
                u'457 _air_noble gases_total beta activity_1 month',
                _(u'457 _air_noble gases_total beta activity_1 month'),
            ),
            VocabItem(
                u'458 _air_noble gases_total beta activity_3 months',
                _(u'458 _air_noble gases_total beta activity_3 months'),
            ),
            VocabItem(
                u'459 _air_noble gases_total beta activity_1 year',
                _(u'459 _air_noble gases_total beta activity_1 year'),
            ),
            VocabItem(
                u'563 _air_gases_beta activity_1 h',
                _(u'563 _air_gases_beta activity_1 h'),
            ),
            VocabItem(
                u'565 _air_gases_beta activity_1 d',
                _(u'565 _air_gases_beta activity_1 d'),
            ),
            VocabItem(
                u'566 _air_gases_beta activity_1 week',
                _(u'566 _air_gases_beta activity_1 week'),
            ),
            VocabItem(
                u'567 _air_gases_beta activity_1 month',
                _(u'567 _air_gases_beta activity_1 month'),
            ),
            VocabItem(
                u'568 _air_gases_beta activity_3 months',
                _(u'568 _air_gases_beta activity_3 months'),
            ),
            VocabItem(
                u'569 _air_gases_beta activity_1 year',
                _(u'569 _air_gases_beta activity_1 year'),
            ),
            VocabItem(
                u'573 _air_aerosol particles_beta activity,  long lived_1 h',
                _(u'573 _air_aerosol particles_beta activity,  long lived_1 h'),
            ),
            VocabItem(
                u'575 _air_aerosol particles_beta activity,  long lived_1 d',
                _(u'575 _air_aerosol particles_beta activity,  long lived_1 d'),
            ),
            VocabItem(
                u'576 _air_aerosol particles_beta activity,  long lived_1 week',
                _(u'576 _air_aerosol particles_beta activity,  long lived_1 week'),
            ),
            VocabItem(
                u'577 _air_aerosol particles_beta activity,  long lived_1 month',
                _(u'577 _air_aerosol particles_beta activity,  long lived_1 month'),
            ),
            VocabItem(
                u'578 _air_aerosol particles_beta activity,  long lived_3 months',
                _(u'578 _air_aerosol particles_beta activity,  long lived_3 months'),
            ),
            VocabItem(
                u'579 _air_aerosol particles_beta activity,  long lived_1 year',
                _(u'579 _air_aerosol particles_beta activity,  long lived_1 year'),
            ),
            VocabItem(u'583 _air__volume_1 h', _(u'583 _air__volume_1 h')),
            VocabItem(u'585 _air__volume_1 d', _(u'585 _air__volume_1 d')),
            VocabItem(u'586 _air__volume_1 week', _(u'586 _air__volume_1 week')),
            VocabItem(u'587 _air__volume_1 month', _(u'587 _air__volume_1 month')),
            VocabItem(u'588 _air__volume_3 months', _(u'588 _air__volume_3 months')),
            VocabItem(u'589 _air__volume_1 year', _(u'589 _air__volume_1 year')),
            VocabItem(u' ____', _(u' ____')),
            VocabItem(
                u'591 _air__volume stream_10 min', _(u'591 _air__volume stream_10 min')
            ),
            VocabItem(
                u'592 _air__volume stream_30 min', _(u'592 _air__volume stream_30 min')
            ),
            VocabItem(
                u'593 _air_stack_temperature_10 min',
                _(u'593 _air_stack_temperature_10 min'),
            ),
            VocabItem(
                u'594 _air_stack_temperature_30 min',
                _(u'594 _air_stack_temperature_30 min'),
            ),
            VocabItem(
                u'595 _air_stack_temperature_1 h', _(u'595 _air_stack_temperature_1 h')
            ),
            VocabItem(
                u'596 _air__temperature_10 min', _(u'596 _air__temperature_10 min')
            ),
            VocabItem(
                u'597 _air__temperature_30 min', _(u'597 _air__temperature_30 min')
            ),
            VocabItem(u'598 _air__temperature_1 h', _(u'598 _air__temperature_1 h')),
            VocabItem(
                u'599 _air__overall loss factor _',
                _(u'599 _air__overall loss factor _'),
            ),
            VocabItem(
                u'606 _water__gamma activity_1 week',
                _(u'606 _water__gamma activity_1 week'),
            ),
            VocabItem(
                u'607 _water__gamma activity_1 month',
                _(u'607 _water__gamma activity_1 month'),
            ),
            VocabItem(
                u'608 _water__gamma activity_3 months',
                _(u'608 _water__gamma activity_3 months'),
            ),
            VocabItem(
                u'609 _water__gamma activity_1 year',
                _(u'609 _water__gamma activity_1 year'),
            ),
            VocabItem(
                u'623 _water__beta activity_1 h', _(u'623 _water__beta activity_1 h')
            ),
            VocabItem(
                u'625 _water__beta activity_1 d', _(u'625 _water__beta activity_1 d')
            ),
            VocabItem(
                u'626 _water__beta activity_1 week',
                _(u'626 _water__beta activity_1 week'),
            ),
            VocabItem(
                u'627 _water__beta activity_1 month',
                _(u'627 _water__beta activity_1 month'),
            ),
            VocabItem(
                u'628 _water__beta activity_3 months',
                _(u'628 _water__beta activity_3 months'),
            ),
            VocabItem(
                u'629 _water__beta activity_1 year',
                _(u'629 _water__beta activity_1 year'),
            ),
            VocabItem(
                u'646 _water__alpha activity_1 week',
                _(u'646 _water__alpha activity_1 week'),
            ),
            VocabItem(
                u'647 _water__alpha activity_1 month',
                _(u'647 _water__alpha activity_1 month'),
            ),
            VocabItem(
                u'648 _water__alpha activity_3 months',
                _(u'648 _water__alpha activity_3 months'),
            ),
            VocabItem(
                u'649 _water__alpha activity_1 year',
                _(u'649 _water__alpha activity_1 year'),
            ),
            VocabItem(
                u'656 _water__total alpha activity_1 week',
                _(u'656 _water__total alpha activity_1 week'),
            ),
            VocabItem(
                u'657 _water__total alpha activity_1 month',
                _(u'657 _water__total alpha activity_1 month'),
            ),
            VocabItem(
                u'658 _water__total alpha activity_3 months',
                _(u'658 _water__total alpha activity_3 months'),
            ),
            VocabItem(
                u'659 _water__total alpha activity_1 year',
                _(u'659 _water__total alpha activity_1 year'),
            ),
            VocabItem(
                u'661 _water__gamma act.conc._10 min',
                _(u'661 _water__gamma act.conc._10 min'),
            ),
            VocabItem(
                u'662 _water__gamma act.conc._30 min',
                _(u'662 _water__gamma act.conc._30 min'),
            ),
            VocabItem(
                u'663 _water__gamma act.conc._1 h',
                _(u'663 _water__gamma act.conc._1 h'),
            ),
            VocabItem(
                u'664 _water__gamma act.conc._2 h',
                _(u'664 _water__gamma act.conc._2 h'),
            ),
            VocabItem(
                u'665 _water__gamma act.conc._1 d',
                _(u'665 _water__gamma act.conc._1 d'),
            ),
            VocabItem(
                u'671 _water__specific act.conc._10 min',
                _(u'671 _water__specific act.conc._10 min'),
            ),
            VocabItem(
                u'672 _water__specific act.conc._30 min',
                _(u'672 _water__specific act.conc._30 min'),
            ),
            VocabItem(
                u'673 _water__specific act.conc._1 h',
                _(u'673 _water__specific act.conc._1 h'),
            ),
            VocabItem(
                u'674 _water__specific act.conc._2 h',
                _(u'674 _water__specific act.conc._2 h'),
            ),
            VocabItem(
                u'691 _air__counting rate_10 min', _(u'691 _air__counting rate_10 min')
            ),
            VocabItem(
                u'693 _air__counting rate_1 h', _(u'693 _air__counting rate_1 h')
            ),
            VocabItem(
                u'695 _air__counting rate_1 d', _(u'695 _air__counting rate_1 d')
            ),
            VocabItem(
                u'696 _air__counting rate_1 week', _(u'696 _air__counting rate_1 week')
            ),
            VocabItem(
                u'697 _air__counting rate_1 month',
                _(u'697 _air__counting rate_1 month'),
            ),
            VocabItem(
                u'698 _air__counting rate_3 months',
                _(u'698 _air__counting rate_3 months'),
            ),
            VocabItem(u'706 _water__volume_1 week', _(u'706 _water__volume_1 week')),
            VocabItem(u'707 _water__volume_1 month', _(u'707 _water__volume_1 month')),
            VocabItem(
                u'708 _water__volume_3 months', _(u'708 _water__volume_3 months')
            ),
            VocabItem(u'709 _water__volume_1 year', _(u'709 _water__volume_1 year')),
            VocabItem(
                u'711 _water__volume stream_10 min',
                _(u'711 _water__volume stream_10 min'),
            ),
            VocabItem(
                u'712 _water__volume stream_30 min',
                _(u'712 _water__volume stream_30 min'),
            ),
            VocabItem(
                u'716 _water__temperature_10 min', _(u'716 _water__temperature_10 min')
            ),
            VocabItem(
                u'717 _water__temperature_30 min', _(u'717 _water__temperature_30 min')
            ),
            VocabItem(
                u'786 _air_meteo_temperature_10 min',
                _(u'786 _air_meteo_temperature_10 min'),
            ),
            VocabItem(
                u'787 _air_meteo_temperature_30 min',
                _(u'787 _air_meteo_temperature_30 min'),
            ),
            VocabItem(
                u'788 _air_meteo_temperature_1 h', _(u'788 _air_meteo_temperature_1 h')
            ),
            VocabItem(
                u'791 __meteo_air pressure_10 min',
                _(u'791 __meteo_air pressure_10 min'),
            ),
            VocabItem(
                u'793 __meteo_air pressure_1 h', _(u'793 __meteo_air pressure_1 h')
            ),
            VocabItem(
                u'796 __meteo_rel. humidity_10 min',
                _(u'796 __meteo_rel. humidity_10 min'),
            ),
            VocabItem(
                u'797 __meteo_rel. humidity_1 h', _(u'797 __meteo_rel. humidity_1 h')
            ),
            VocabItem(u'800 __meteo_precipitation_', _(u'800 __meteo_precipitation_')),
            VocabItem(
                u'801 __meteo_precipitation_10 min',
                _(u'801 __meteo_precipitation_10 min'),
            ),
            VocabItem(
                u'802 __meteo_precipitation_30 min',
                _(u'802 __meteo_precipitation_30 min'),
            ),
            VocabItem(
                u'803 __meteo_precipitation_1 h', _(u'803 __meteo_precipitation_1 h')
            ),
            VocabItem(
                u'804 __meteo_precipitation_2 h', _(u'804 __meteo_precipitation_2 h')
            ),
            VocabItem(
                u'805 __meteo_precipitation_1 d', _(u'805 __meteo_precipitation_1 d')
            ),
            VocabItem(
                u'806 __meteo_precipitation_1 wo', _(u'806 __meteo_precipitation_1 wo')
            ),
            VocabItem(
                u'807 __meteo_precipitation_1 m', _(u'807 __meteo_precipitation_1 m')
            ),
            VocabItem(
                u'815 __meteo_precipitation snow_1 d',
                _(u'815 __meteo_precipitation snow_1 d'),
            ),
            VocabItem(
                u'818 __meteo_precipitation probability_15 min',
                _(u'818 __meteo_precipitation probability_15 min'),
            ),
            VocabItem(
                u'819 __meteo_precipitation probability_2 h',
                _(u'819 __meteo_precipitation probability_2 h'),
            ),
            VocabItem(
                u'824 __meteo_precipitation intensity_',
                _(u'824 __meteo_precipitation intensity_'),
            ),
            VocabItem(
                u'825 __meteo_precipitation intensity_',
                _(u'825 __meteo_precipitation intensity_'),
            ),
            VocabItem(
                u'827 __meteo_precipitation relativly_10 min',
                _(u'827 __meteo_precipitation relativly_10 min'),
            ),
            VocabItem(
                u'831 __meteo_wind velocity_10 min',
                _(u'831 __meteo_wind velocity_10 min'),
            ),
            VocabItem(
                u'832 __meteo_wind velocity_30 min',
                _(u'832 __meteo_wind velocity_30 min'),
            ),
            VocabItem(
                u'833 __meteo_wind velocity_1 h', _(u'833 __meteo_wind velocity_1 h')
            ),
            VocabItem(
                u'834 __meteo_wind velocity_2 h', _(u'834 __meteo_wind velocity_2 h')
            ),
            VocabItem(
                u'836 __meteo_wind veloc. fluctuation (sigma w)_10 min',
                _(u'836 __meteo_wind veloc. fluctuation (sigma w)_10 min'),
            ),
            VocabItem(
                u'837 __meteo_wind veloc. fluctuation (sigma w)_30 min',
                _(u'837 __meteo_wind veloc. fluctuation (sigma w)_30 min'),
            ),
            VocabItem(
                u'838 __meteo_wind veloc. fluctuation (sigma w)_1 h',
                _(u'838 __meteo_wind veloc. fluctuation (sigma w)_1 h'),
            ),
            VocabItem(
                u'841 __meteo_wind direction_10 min',
                _(u'841 __meteo_wind direction_10 min'),
            ),
            VocabItem(
                u'842 __meteo_wind direction_30 min',
                _(u'842 __meteo_wind direction_30 min'),
            ),
            VocabItem(
                u'843 __meteo_wind direction_1 h', _(u'843 __meteo_wind direction_1 h')
            ),
            VocabItem(
                u'844 __meteo_wind direction_2 h', _(u'844 __meteo_wind direction_2 h')
            ),
            VocabItem(
                u'851 __meteo_wind dir. fluctuation (sigma ?)_10 min',
                _(u'851 __meteo_wind dir. fluctuation (sigma ?)_10 min'),
            ),
            VocabItem(
                u'852 __meteo_wind dir. fluctuation (sigma ?)_30 min',
                _(u'852 __meteo_wind dir. fluctuation (sigma ?)_30 min'),
            ),
            VocabItem(
                u'853 __meteo_wind dir. fluctuation (sigma ?)_1 h',
                _(u'853 __meteo_wind dir. fluctuation (sigma ?)_1 h'),
            ),
            VocabItem(
                u'856 __meteo_wind dir. fluctuation (sigma ?)_10 min',
                _(u'856 __meteo_wind dir. fluctuation (sigma ?)_10 min'),
            ),
            VocabItem(
                u'857 __meteo_wind dir. fluctuation (sigma ?)_30 min',
                _(u'857 __meteo_wind dir. fluctuation (sigma ?)_30 min'),
            ),
            VocabItem(
                u'858 __meteo_wind dir. fluctuation (sigma ?)_1 h',
                _(u'858 __meteo_wind dir. fluctuation (sigma ?)_1 h'),
            ),
            VocabItem(
                u'861 __meteo_radiation balance_10 min',
                _(u'861 __meteo_radiation balance_10 min'),
            ),
            VocabItem(
                u'862 __meteo_radiation balance_30 min',
                _(u'862 __meteo_radiation balance_30 min'),
            ),
            VocabItem(
                u'863 __meteo_radiation balance_1 h',
                _(u'863 __meteo_radiation balance_1 h'),
            ),
            VocabItem(
                u'876 __meteo_stability class (1-6) (sigma w)_10 min',
                _(u'876 __meteo_stability class (1-6) (sigma w)_10 min'),
            ),
            VocabItem(
                u'877 __meteo_stability class (1-6) (sigma w)_30 min',
                _(u'877 __meteo_stability class (1-6) (sigma w)_30 min'),
            ),
            VocabItem(
                u'878 __meteo_stability class (1-6) (sigma w)_1 h',
                _(u'878 __meteo_stability class (1-6) (sigma w)_1 h'),
            ),
            VocabItem(
                u'881 __meteo_stability class (1-6) (radiation balance)_10 min',
                _(u'881 __meteo_stability class (1-6) (radiation balance)_10 min'),
            ),
            VocabItem(
                u'882 __meteo_stability class (1-6) (radiation balance)_30 min',
                _(u'882 __meteo_stability class (1-6) (radiation balance)_30 min'),
            ),
            VocabItem(
                u'883 __meteo_stability class (1-6) (radiation balance)_1 h',
                _(u'883 __meteo_stability class (1-6) (radiation balance)_1 h'),
            ),
            VocabItem(
                u'886 __meteo_stability class (1-6) (sigma ?)_10 min',
                _(u'886 __meteo_stability class (1-6) (sigma ?)_10 min'),
            ),
            VocabItem(
                u'887 __meteo_stability class (1-6) (sigma ?)_30 min',
                _(u'887 __meteo_stability class (1-6) (sigma ?)_30 min'),
            ),
            VocabItem(
                u'888 __meteo_stability class (1-6) (sigma ?)_1 h',
                _(u'888 __meteo_stability class (1-6) (sigma ?)_1 h'),
            ),
            VocabItem(
                u'891 __meteo_stability class (1-6) (sigma ?)_10 min',
                _(u'891 __meteo_stability class (1-6) (sigma ?)_10 min'),
            ),
            VocabItem(
                u'892 __meteo_stability class (1-6) (sigma ?)_30 min',
                _(u'892 __meteo_stability class (1-6) (sigma ?)_30 min'),
            ),
            VocabItem(
                u'893 __meteo_stability class (1-6) (sigma ?)_1 h',
                _(u'893 __meteo_stability class (1-6) (sigma ?)_1 h'),
            ),
            VocabItem(
                u'896 __meteo_stability class (1-6) (temp. gradient)_10 min',
                _(u'896 __meteo_stability class (1-6) (temp. gradient)_10 min'),
            ),
            VocabItem(
                u'897 __meteo_stability class (1-6) (temp. gradient)_30 min',
                _(u'897 __meteo_stability class (1-6) (temp. gradient)_30 min'),
            ),
            VocabItem(
                u'898 __meteo_stability class (1-6) (temp. gradient)_1 h',
                _(u'898 __meteo_stability class (1-6) (temp. gradient)_1 h'),
            ),
            VocabItem(
                u'951 ___electrical power_10 min', _(u'951 ___electrical power_10 min')
            ),
            VocabItem(
                u'953 ___electrical power_1 h', _(u'953 ___electrical power_1 h')
            ),
            VocabItem(
                u'955 ___electrical power_1 d', _(u'955 ___electrical power_1 d')
            ),
            VocabItem(
                u'956 ___electrical power_1 week', _(u'956 ___electrical power_1 week')
            ),
            VocabItem(
                u'957 ___electrical power_1 month',
                _(u'957 ___electrical power_1 month'),
            ),
            VocabItem(
                u'958 ___electrical power_3 months',
                _(u'958 ___electrical power_3 months'),
            ),
            VocabItem(
                u'959 ___electrical power_1 year', _(u'959 ___electrical power_1 year')
            ),
            VocabItem(u'961 ___therm. power_10 min', _(u'961 ___therm. power_10 min')),
            VocabItem(u'963 ___therm. power_1 h', _(u'963 ___therm. power_1 h')),
            VocabItem(u'965 ___therm. power_1 d', _(u'965 ___therm. power_1 d')),
            VocabItem(u'966 ___therm. power_1 week', _(u'966 ___therm. power_1 week')),
            VocabItem(
                u'967 ___therm. power_1 month', _(u'967 ___therm. power_1 month')
            ),
            VocabItem(
                u'968 ___therm. power_3 months', _(u'968 ___therm. power_3 months')
            ),
            VocabItem(u'969 ___therm. power_1 year', _(u'969 ___therm. power_1 year')),
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


DomFactory = Dom()
