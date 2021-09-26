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
            ])
        ]    
        for w in golden_declensions:
            self.assertGreaterEqual(set(dec_fi.get_declensions(w[0])), set(w[1]))
            
if __name__ == '__main__':
    unittest.main()
