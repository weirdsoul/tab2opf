# -*- coding: utf-8 -*-
#
# Module containing Finnish grammar rules to generate
# inflections from basic forms (verbs in infinitive etc.).

import base_structures_fi as base_fi
import conjugations_fi
import declensions_fi

# Trivially, ko/kö can be appended to almost every conceivable
# word, so calling this will extend inflections by the appropriate ko/kö
# suffix being added to every single entry.
def apply_ko_suffix(word, inflections):    
    suffix = 'ko' if base_fi.is_back_word(word) else 'kö'
    
    new_list = [ (i[0] + ' + ' + suffix, i[1] + suffix) for i in inflections ]
    inflections.extend(new_list)
    inflections.append(('perusmuoto + ' + suffix, word + suffix))

# get all inflections of word (which is of word_type).
# returns a list of tuples ("form", "value").
def getinflections(word, word_type):
    inflections = []
    if word_type == 'verb':
        inflections = conjugations_fi.get_conjugations(word)
    elif word_type == 'noun':
        inflections = declensions_fi.get_declensions(word)
    apply_ko_suffix(word, inflections)
    return inflections
