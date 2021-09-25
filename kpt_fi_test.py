#!/bin/python3
# -*- coding: utf-8 -*-
#
# Test cases for Finnish grammar rules.

import unittest
import kpt_fi

class TestKPTRules(unittest.TestCase):

    def test_kpt(self):
        golden_kpt_pairs = [
            # Pairs of vahva and heikko

            # Consonant gradation expected.
            ('nukku', 'nuku'),
            ('anta', 'anna'),
            ('kirjoitta', 'kirjoita'),
            ('luke', 'lue'),
            ('onki', 'ongi'),
            ('tietä', 'tiedä'),
            ('ymmärtä', 'ymmärrä'),
            ('odotta', 'odota'),
            
            # No consonant gradation expected.
            ('etsi', 'etsi')
        ]
        
        for p in golden_kpt_pairs:
            self.assertGreaterEqual(set(kpt_fi.apply_kpt_vaihtelu(p[0])),
                                    set(p[1]))
            
if __name__ == '__main__':
    unittest.main()
