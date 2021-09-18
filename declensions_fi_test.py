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
                ('partitiivi', 'museota')
            ]),
            # No kpt, because not applicable to last syllable.
            ('makkara', [
                ('genetiivi', 'makkaran'),
                ('monikko', 'makkarat'),
                ('partitiivi', 'makkaraa')
            ]),
            # TODO(aeckleder): genetiivi vartalo isn't implemented yet.
            ('osoite', [
                ('partitiivi', 'osoitetta')
            ]),
            # TODO(aeckleder): genetiivi vartalo isn't implemented yet.
            ('puhelin', [
                ('partitiivi', 'puhelinta')
            ]),
            # kpt applied (except for partitiivi, of course).
            ('pöytä', [
                ('genetiivi', 'pöydän'),
                ('monikko', 'pöydät'),
                ('partitiivi', 'pöytää')
            ]),
            # kpt applied (except for partitiivi, of course).
            ('kenkä', [
                ('genetiivi', 'kengän'),
                ('monikko', 'kengät'),
                ('partitiivi', 'kenkää')
            ])
        ]
        for w in golden_declensions:
            self.assertEqual(dec_fi.get_declensions(w[0]), w[1])
            
if __name__ == '__main__':
    unittest.main()
