#!/bin/python3
# -*- coding: utf-8 -*-
#
# Test cases for Finnish grammar rules.

import unittest
import conjugations_fi as co_fi

class TestVTRules(unittest.TestCase):

    def test_present_vt1(self):
        golden_conjugations = [
            ('antaa', [
                ('1ps present', 'annan'),
                ('2ps present', 'annat'),
                ('3ps present', 'antaa'),
                ('1pp present', 'annamme'),
                ('2pp present', 'annatte'),
                ('3pp present', 'antavat')]),
            ('jakaa', [
                ('1ps present', 'jaan'),
                ('2ps present', 'jaat'),
                ('3ps present', 'jakaa'),
                ('1pp present', 'jaamme'),
                ('2pp present', 'jaatte'),
                ('3pp present', 'jakavat')])]
        for w in golden_conjugations:
            self.assertGreaterEqual(co_fi.apply_present_tense(w[0]), w[1])        

    def test_present_vt2(self):
        golden_conjugations = [
            ('syödä', [
                ('1ps present', 'syön'),
                ('2ps present', 'syöt'),
                ('3ps present', 'syö'),
                ('1pp present', 'syömme'),
                ('2pp present', 'syötte'),
                ('3pp present', 'syövät')])]
        for w in golden_conjugations:
            self.assertGreaterEqual(co_fi.apply_present_tense(w[0]), w[1])

    def test_present_vt3(self):
        golden_conjugations = [
            ('tulla', [
                ('1ps present', 'tulen'),
                ('2ps present', 'tulet'),
                ('3ps present', 'tulee'),
                ('1pp present', 'tulemme'),
                ('2pp present', 'tulette'),
                ('3pp present', 'tulevat')]),
            ('nousta', [
                ('1ps present', 'nousen'),
                ('2ps present', 'nouset'),
                ('3ps present', 'nousee'),
                ('1pp present', 'nousemme'),
                ('2pp present', 'nousette'),
                ('3pp present', 'nousevat')]),
            ('mennä', [
                ('1ps present', 'menen'),
                ('2ps present', 'menet'),
                ('3ps present', 'menee'),
                ('1pp present', 'menemme'),
                ('2pp present', 'menette'),
                ('3pp present', 'menevät')]),
            ('purra', [
                ('1ps present', 'puren'),
                ('2ps present', 'puret'),
                ('3ps present', 'puree'),
                ('1pp present', 'puremme'),
                ('2pp present', 'purette'),
                ('3pp present', 'purevat')]),
            ('jutella', [
                ('1ps present', 'juttelen'),
                ('2ps present', 'juttelet'),
                ('3ps present', 'juttelee'),
                ('1pp present', 'juttelemme'),
                ('2pp present', 'juttelette'),
                ('3pp present', 'juttelevat')])]
        for w in golden_conjugations:
            self.assertGreaterEqual(co_fi.apply_present_tense(w[0]), w[1])

    def test_present_vt4(self):
        golden_conjugations = [
            ('haluta', [
                ('1ps present', 'haluan'),
                ('2ps present', 'haluat'),
                ('3ps present', 'haluaa'),
                ('1pp present', 'haluamme'),
                ('2pp present', 'haluatte'),
                ('3pp present', 'haluavat')]),
            ('herätä', [
                ('1ps present', 'herään'),
                ('2ps present', 'heräät'),
                ('3ps present', 'herää'),
                ('1pp present', 'heräämme'),
                ('2pp present', 'heräätte'),
                ('3pp present', 'heräävät')]),
            ('tavata', [
                ('1ps present', 'tapaan'),
                ('2ps present', 'tapaat'),
                ('3ps present', 'tapaa'),
                ('1pp present', 'tapaamme'),
                ('2pp present', 'tapaatte'),
                ('3pp present', 'tapaavat')])]
            # TODO: _->'k' reverse kpt vaihtelu is unsupported.
            #('maata', [
            #    ('1ps present', 'makaan'),
            #    ('2ps present', 'makaat'),
            #    ('3ps present', 'makaa'),
            #    ('1pp present', 'makaamme'),
            #    ('2pp present', 'makaatte'),
            #    ('3pp present', 'makaavat')])]
        for w in golden_conjugations:
            self.assertGreaterEqual(co_fi.apply_present_tense(w[0]), w[1])

    def test_present_vt5(self):
        golden_conjugations = [
            ('tarvita', [
                ('1ps present', 'tarvitsen'),
                ('2ps present', 'tarvitset'),
                ('3ps present', 'tarvitsee'),
                ('1pp present', 'tarvitsemme'),
                ('2pp present', 'tarvitsette'),
                ('3pp present', 'tarvitsevat')]),
            ('häiritä', [
                ('1ps present', 'häiritsen'),
                ('2ps present', 'häiritset'),
                ('3ps present', 'häiritsee'),
                ('1pp present', 'häiritsemme'),
                ('2pp present', 'häiritsette'),
                ('3pp present', 'häiritsevät')])]
        for w in golden_conjugations:
            self.assertGreaterEqual(co_fi.apply_present_tense(w[0]), w[1])

    def test_present_vt6(self):
        golden_conjugations = [
            ('vanheta', [
                ('1ps present', 'vanhenen'),
                ('2ps present', 'vanhenet'),
                ('3ps present', 'vanhenee'),
                ('1pp present', 'vanhenemme'),
                ('2pp present', 'vanhenette'),
                ('3pp present', 'vanhenevat')]),
            ('lämmetä', [
                ('1ps present', 'lämpenen'),
                ('2ps present', 'lämpenet'),
                ('3ps present', 'lämpenee'),
                ('1pp present', 'lämpenemme'),
                ('2pp present', 'lämpenette'),
                ('3pp present', 'lämpenevät')])]            
        for w in golden_conjugations:
            self.assertGreaterEqual(co_fi.apply_present_tense(w[0]), w[1])


    def test_imperfekti(self):
        golden_conjugations = [
            ('sanoa', [ # o/ö/u/y variant
                ('1ps imperfekti', 'sanoin'),
                ('2ps imperfekti', 'sanoit'),
                ('3ps imperfekti', 'sanoi'),
                ('1pp imperfekti', 'sanoimme'),
                ('2pp imperfekti', 'sanoitte'),
                ('3pp imperfekti', 'sanoivat')]),
            ('odottaa', [ # a/ä/e/i variant
                ('1ps imperfekti', 'odotin'),
                ('2ps imperfekti', 'odotit'),
                ('3ps imperfekti', 'odotti'),
                ('1pp imperfekti', 'odotimme'),
                ('2pp imperfekti', 'odotitte'),
                ('3pp imperfekti', 'odottivat')]),
            ('opiskella', [ # a/ä/e/i variant
                ('1ps imperfekti', 'opiskelin'),
                ('2ps imperfekti', 'opiskelit'),
                ('3ps imperfekti', 'opiskeli'),
                ('1pp imperfekti', 'opiskelimme'),
                ('2pp imperfekti', 'opiskelitte'),
                ('3pp imperfekti', 'opiskelivat')]),
            ('laulaa', [ # a -> o substitution
                ('1ps imperfekti', 'lauloin'),
                ('2ps imperfekti', 'lauloit'),
                ('3ps imperfekti', 'lauloi'),
                ('1pp imperfekti', 'lauloimme'),
                ('2pp imperfekti', 'lauloitte'),
                ('3pp imperfekti', 'lauloivat')]),
            ('alkaa', [ # a -> o substitution
                ('1ps imperfekti', 'aloin'),
                ('2ps imperfekti', 'aloit'),
                ('3ps imperfekti', 'alkoi'),
                ('1pp imperfekti', 'aloimme'),
                ('2pp imperfekti', 'aloitte'),
                ('3pp imperfekti', 'alkoivat')]),
            ('jakaa', [ # a -> o substitution
                ('1ps imperfekti', 'jaoin'),
                ('2ps imperfekti', 'jaoit'),
                ('3ps imperfekti', 'jakoi'),
                ('1pp imperfekti', 'jaoimme'),
                ('2pp imperfekti', 'jaoitte'),
                ('3pp imperfekti', 'jakoivat')]),
            ('saada', [ # vv -> v
                ('1ps imperfekti', 'sain'),
                ('2ps imperfekti', 'sait'),
                ('3ps imperfekti', 'sai'),
                ('1pp imperfekti', 'saimme'),
                ('2pp imperfekti', 'saitte'),
                ('3pp imperfekti', 'saivat')]),
            ('myydä', [ # vv -> v
                ('1ps imperfekti', 'myin'),
                ('2ps imperfekti', 'myit'),
                ('3ps imperfekti', 'myi'),
                ('1pp imperfekti', 'myimme'),
                ('2pp imperfekti', 'myitte'),
                ('3pp imperfekti', 'myivät')]),
            ('viedä', [ # ie -> ei
                ('1ps imperfekti', 'vein'),
                ('2ps imperfekti', 'veit'),
                ('3ps imperfekti', 'vei'),
                ('1pp imperfekti', 'veimme'),
                ('2pp imperfekti', 'veitte'),
                ('3pp imperfekti', 'veivät')]),
            ('syödä', [ # yö -> öi
                ('1ps imperfekti', 'söin'),
                ('2ps imperfekti', 'söit'),
                ('3ps imperfekti', 'söi'),
                ('1pp imperfekti', 'söimme'),
                ('2pp imperfekti', 'söitte'),
                ('3pp imperfekti', 'söivät')]),
            ('juoda', [ # uo -> oi
                ('1ps imperfekti', 'join'),
                ('2ps imperfekti', 'joit'),
                ('3ps imperfekti', 'joi'),
                ('1pp imperfekti', 'joimme'),
                ('2pp imperfekti', 'joitte'),
                ('3pp imperfekti', 'joivat')]),
            ('herätä', [ # vt4 ä -> si
                ('1ps imperfekti', 'heräsin'),
                ('2ps imperfekti', 'heräsit'),
                ('3ps imperfekti', 'heräsi'),
                ('1pp imperfekti', 'heräsimme'),
                ('2pp imperfekti', 'heräsitte'),
                ('3pp imperfekti', 'heräsivät')]),
            ('haluta', [ # vt4 a -> si
                ('1ps imperfekti', 'halusin'),
                ('2ps imperfekti', 'halusit'),
                ('3ps imperfekti', 'halusi'),
                ('1pp imperfekti', 'halusimme'),
                ('2pp imperfekti', 'halusitte'),
                ('3pp imperfekti', 'halusivat')]),
            ('tietää', [ # vt1 exception XV -> si
                ('1ps imperfekti', 'tiesin'),
                ('2ps imperfekti', 'tiesit'),
                ('3ps imperfekti', 'tiesi'),
                ('1pp imperfekti', 'tiesimme'),
                ('2pp imperfekti', 'tiesitte'),
                ('3pp imperfekti', 'tiesivät')])]

            
            
        for w in golden_conjugations:
            self.assertGreaterEqual(co_fi.apply_imperfekti(w[0]), w[1])
            
if __name__ == '__main__':
    unittest.main()
