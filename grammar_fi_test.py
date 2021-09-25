#!/bin/python3
# -*- coding: utf-8 -*-
#
# Test cases for Finnish grammar rules.

import unittest
import grammar_fi

class TestInflectionRules(unittest.TestCase):

    def test_verb_inflections(self):
        golden_inflections = [
            ('antaa', [
                ('1ps present', 'annan'),
                ('2ps present', 'annat'),
                ('3ps present', 'antaa'),
                ('1pp present', 'annamme'),
                ('2pp present', 'annatte'),
                ('3pp present', 'antavat'),
                ('1ps imperfekti', 'annoin'),
                ('2ps imperfekti', 'annoit'),
                ('3ps imperfekti', 'antoi'),
                ('1pp imperfekti', 'annoimme'),
                ('2pp imperfekti', 'annoitte'),
                ('3pp imperfekti', 'antoivat'),
                
                ('negatiivinen imperfekti', 'antanut'),
                ('monikon negatiivinen imperfekti', 'antaneet'),

                ('1ps present + ko', 'annanko'),
                ('2ps present + ko', 'annatko'),
                ('3ps present + ko', 'antaako'),
                ('1pp present + ko', 'annammeko'),
                ('2pp present + ko', 'annatteko'),
                ('3pp present + ko', 'antavatko'),
                ('1ps imperfekti + ko', 'annoinko'),
                ('2ps imperfekti + ko', 'annoitko'),
                ('3ps imperfekti + ko', 'antoiko'),
                ('1pp imperfekti + ko', 'annoimmeko'),
                ('2pp imperfekti + ko', 'annoitteko'),
                ('3pp imperfekti + ko', 'antoivatko'),

                ('perusmuoto + ko', 'antaako'),
            ])
        ]
        for w in golden_inflections:
            self.assertGreaterEqual(set(grammar_fi.getinflections(w[0], 'verb')), set(w[1]))

    def test_noun_inflections(self):
        golden_inflections = [
            ('pöytä', [
                ('genetiivi', 'pöydän'),
                ('monikko', 'pöydät'),
                ('inessiivi', 'pöydässä'),
                ('elatiivi', 'pöydästä'),
                ('allatiivi', 'pöydälle'),
                ('adessiivi', 'pöydällä'),
                ('ablatiivi', 'pöydältä'),                
                ('partitiivi', 'pöytää'),
                ('genetiivi + kö', 'pöydänkö'),
                ('monikko + kö', 'pöydätkö'),
                ('inessiivi + kö', 'pöydässäkö'),
                ('elatiivi + kö', 'pöydästäkö'),
                ('allatiivi + kö', 'pöydällekö'),
                ('adessiivi + kö', 'pöydälläkö'),
                ('ablatiivi + kö', 'pöydältäkö'),                
                ('partitiivi + kö', 'pöytääkö'),
                ('perusmuoto + kö', 'pöytäkö')])
        ]
        for w in golden_inflections:
            self.assertGreaterEqual(set(grammar_fi.getinflections(w[0], 'noun')), set(w[1]))

    def test_adjective_inflections(self):
        golden_inflections = [
            ('kuuma', [
                ('genetiivi', 'kuuman'),
                ('monikko', 'kuumat'),
                ('inessiivi', 'kuumassa'),
                ('elatiivi', 'kuumasta'),
                ('allatiivi', 'kuumalle'),
                ('adessiivi', 'kuumalla'),
                ('ablatiivi', 'kuumalta'),                
                ('partitiivi', 'kuumaa'),
                ('genetiivi + ko', 'kuumanko'),
                ('monikko + ko', 'kuumatko'),
                ('inessiivi + ko', 'kuumassako'),
                ('elatiivi + ko', 'kuumastako'),
                ('allatiivi + ko', 'kuumalleko'),
                ('adessiivi + ko', 'kuumallako'),
                ('ablatiivi + ko', 'kuumaltako'),                
                ('partitiivi + ko', 'kuumaako'),
                ('perusmuoto + ko', 'kuumako')])
        ]
        for w in golden_inflections:
            self.assertGreaterEqual(set(grammar_fi.getinflections(w[0], 'adj')), set(w[1]))

if __name__ == '__main__':
    unittest.main()
