#!/bin/python3
# -*- coding: utf-8 -*-
#
# Test cases for Finnish grammar rules.

import unittest
import base_structures_fi as base_fi

class TestVowels(unittest.TestCase):

    def test_is_back_word(self):
        back_words = [
            ('antaa', True),
            ('syödä', False)
        ]

        for p in back_words:
            self.assertGreaterEqual(base_fi.is_back_word(p[0]),
                             p[1])

class TestSyllableSplit(unittest.TestCase):

    def test_syllables(self):
        golden_splits = [
            # Pairs of word and intended split
            ('nukku', ['nuk', 'ku']),
            ('anta', ['an', 'ta']),
            ('kirjoitta', ['kir', 'joit', 'ta']),
            ('luke', ['lu', 'ke']),
            ('onki', ['on', 'ki']),
            ('tietä', ['tie', 'tä']),
            ('ymmärtä', ['ym', 'mär', 'tä']),
            ('etsi', ['et', 'si']),
            ('odotta', ['o', 'dot', 'ta'])
            
        ]

        for p in golden_splits:
            self.assertGreaterEqual(base_fi.split_syllables(p[0]),
                             p[1])
            
if __name__ == '__main__':
    unittest.main()
