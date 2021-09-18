# -*- coding: utf-8 -*-
#
# Module containing Finnish grammar rules to generate
# declensions from from perusmuoto substantiivi forms

import base_structures_fi as base_fi
import kpt_fi

# Generate genetiivi form for -a/o/u/y/ä/ö suffixes (sanatyypi 1).
# Essentially, this applies kpt vaihtelu only, no suffix modifications.
def get_gen_st_1(word):
    return kpt_fi.apply_kpt_vaihtelu(word)

# Generate the genetiivi vartalo for the specified substantive.
# This will apply kpt vaihtelu as appropriate and perform any
# other applicable suffix transformation according to the
# sanatyypi of the word.
# May return None if the correct vartalo couldn't be identified.
# TODO(aeckleder): Check whether we should default of st1 in this case.
def get_genetiivivartalo(word):
    if word[-1] in base_fi.FRONT_VOWELS + base_fi.BACK_VOWELS:
        return get_gen_st_1(word)
    return None

# Generate the partitiivi of the specified word.
# TODO(aeckleder): While the current rules are comprehensive, they're
# not always correct. We need to deal explicitly with some sanatyypit.
def get_partitiivi(word):
    suffix_vowel = 'a' if base_fi.is_back_word(word) else 'ä'
    if word[-1] == 'e':
        return word + 'tt' + suffix_vowel
    elif (not base_fi.is_vowel(word[-1]) or
          len(word) > 1 and base_fi.is_vowel(word[-2])):
        return word + 't' + suffix_vowel
    else:
        return word + suffix_vowel

# Produce declensions of the specified substantive
def get_declensions(word):
    results = []
    gen_vartalo = get_genetiivivartalo(word)
    if gen_vartalo:
        # If we could build the genetiivi vartalo correctly,
        # we can generate several forms from it.
        results.append(('genetiivi', gen_vartalo + 'n'))
        results.append(('monikko', gen_vartalo + 't'))
        
    results.append(('partitiivi', get_partitiivi(word)))
    
    return results