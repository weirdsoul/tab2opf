#!/bin/python3
# -*- coding: utf-8 -*-
#
# Test cases for declensions in Finnish.

import unittest
import declensions_fi as dec_fi

class TestDeclensionRules(unittest.TestCase):

    def test_st_1(self):
        golden_declensions = [
            # Double vowel.
            ('museo', [
                ('genetiivi', 'museon'),
                ('monikko', 'museot'),
                # TODO(aeckleder): No illatiivi yet.
                ('inessiivi', 'museossa'),
                ('elatiivi', 'museosta'),
                ('allatiivi', 'museolle'),
                ('adessiivi', 'museolla'),
                ('ablatiivi', 'museolta'),
                ('partitiivi', 'museota')
            ]),
            # No kpt, because not applicable to last syllable.
            ('makkara', [
                ('genetiivi', 'makkaran'),
                ('monikko', 'makkarat'),
                # TODO(aeckleder): No illatiivi yet.
                ('inessiivi', 'makkarassa'),
                ('elatiivi', 'makkarasta'),
                ('allatiivi', 'makkaralle'),
                ('adessiivi', 'makkaralla'),
                ('ablatiivi', 'makkaralta'),
                ('partitiivi', 'makkaraa')
            ]),
            ('osoite', [
                ('genetiivi', 'osoideen'),
                ('monikko', 'osoideet'),
                # TODO(aeckleder): No illatiivi yet.
                ('inessiivi', 'osoideessa'),
                ('elatiivi', 'osoideesta'),
                ('allatiivi', 'osoideelle'),
                ('adessiivi', 'osoideella'),
                ('ablatiivi', 'osoideelta'),                
                ('partitiivi', 'osoitetta')
            ]),
            # TODO(aeckleder): genetiivi vartalo is incorrect, should
            # be puhelime.
            ('puhelin', [
                ('genetiivi', 'puhelinin'),
                ('monikko', 'puhelinit'),
                # TODO(aeckleder): No illatiivi yet.
                ('inessiivi', 'puhelinissa'),
                ('elatiivi', 'puhelinista'),
                ('allatiivi', 'puhelinille'),
                ('adessiivi', 'puhelinilla'),
                ('ablatiivi', 'puhelinilta'),                
                ('partitiivi', 'puhelinta')
            ]),
            # kpt applied (except for partitiivi, of course).
            ('pöytä', [
                ('genetiivi', 'pöydän'),
                ('monikko', 'pöydät'),
                # TODO(aeckleder): No illatiivi yet.
                ('inessiivi', 'pöydässä'),
                ('elatiivi', 'pöydästä'),
                ('allatiivi', 'pöydälle'),
                ('adessiivi', 'pöydällä'),
                ('ablatiivi', 'pöydältä'),                
                ('partitiivi', 'pöytää')
            ]),
            # Consonant suffix.
            ('jazz', [
                ('genetiivi', 'jazzin'),
                ('monikko', 'jazzit'),
                # TODO(aeckleder): No illatiivi yet.
                ('inessiivi', 'jazzissa'),
                ('elatiivi', 'jazzista'),
                ('allatiivi', 'jazzille'),
                ('adessiivi', 'jazzilla'),
                ('ablatiivi', 'jazzilta'),            
                # TODO(aeckleder): This is not correct.
                ('partitiivi', 'jazzta')
            ]),
            # Partitiivi for 'eä' suffix 
            ('vihreä', [
                ('genetiivi', 'vihreän'),
                ('partitiivi', 'vihreää')
            ]),
            # e-sanatyyppi
            ('vene', [
                ('genetiivi', 'veneen'),
                ('partitiivi', 'venettä')
            ]),
            # nen-sanatyyppi
            ('valkoinen', [
                ('genetiivi', 'valkoisen'),
                ('partitiivi', 'valkoista')
            ]),
            # nen-sanatyyppi with front vowel
            ('helsinkiläinen', [
                ('genetiivi', 'helsinkiläisen'),
                ('partitiivi', 'helsinkiläistä')
            ]),
            # si-sanatyyppi
            ('uusi', [
                ('genetiivi', 'uuden'),
                ('partitiivi', 'uutta')
            ]),
            # i-sanatyyppi (variant #1: i -> i, no transformation)
            ('hotelli', [
                ('genetiivi', 'hotellin'),
                ('partitiivi', 'hotellia')
            ]),
            # i-sanatyyppi (variant #2: i -> e, drop i for partitiivi)
            # Note that i-sanatyyppit are ambiguous, so we always build
            # all form candidates here, with i -> i being the default.
            # This is ok for our use-case, because we're building an index
            # rather than a dictionary or translator.
            ('suuri', [
                ('genetiivi (alt 1)', 'suuren'),
                ('partitiivi (alt 1)', 'suurta')
            ]),
            # i-sanatyyppi (variant #3: i -> e, also in partitiivi)
            ('nimi', [
                ('genetiivi (alt 1)', 'nimen'),
                ('partitiivi (alt 2)', 'nimeä')
            ])
        ]    
        for w in golden_declensions:
            self.assertGreaterEqual(set(dec_fi.get_declensions(w[0])), set(w[1]))
            
if __name__ == '__main__':
    unittest.main()
