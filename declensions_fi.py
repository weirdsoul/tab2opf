# -*- coding: utf-8 -*-
#
# Module containing Finnish grammar rules to generate
# declensions from from perusmuoto substantiivi forms

import base_structures_fi as base_fi
import kpt_fi

# Generate genetiivi form for -a/o/u/y/ä/ö and consonant
# suffixes that are not any of the other sanatyypit (sanatyypi 1).
# Essentially, this applies kpt vaihtelu only, no suffix modifications.
def get_gen_st_1(word):
    v = kpt_fi.apply_kpt_vaihtelu(word)
    if not base_fi.is_vowel(v[-1]):
        # Consonants
        v = v + 'i'
    return v

# Generate genetiivi form for e-sanatyyppi words.
def get_gen_st_e(word):
    # We simply double the 'e' suffix to obtain the vartalo
    return kpt_fi.apply_kpt_vaihtelu(word) + word[-1]

# Generate genetiivi form for nen-sanatyyppi words.
def get_gen_st_nen(word):
    # Replace the -nen suffix by -se.
    return kpt_fi.apply_kpt_vaihtelu(word)[:-3] + 'se'

# Generate genetiivi form for si-sanatyyppi words.
def get_gen_st_si(word):
    # Replace the -si suffix by -de.
    return kpt_fi.apply_kpt_vaihtelu(word)[:-2] + 'de'

# Generate genetiivi vartalo candidates for the specified word.
# This will apply kpt vaihtelu as appropriate and perform any
# other applicable suffix transformation according to the
# sanatyyppi of the word.
# ** Note that this returns a *list of candidates* whenever the
#    sanatyyppi is ambiguous. This is currently the case for -i
#    suffixes. The reason is that we're using these candidates
#    to build an index. Not having a valid form in the index is
#    strictly worse than having an invalid form in it. **
def get_genetiivivartalo(word):
    # Special casing for the different sanatyyppit.
    # TODO(aeckleder): Not all sanatyyppit are implemented.
    if len(word) and word[-1] == 'e':
        return [get_gen_st_e(word)]
    
    if len(word) > 2 and word[-3:] == 'nen':
        return [get_gen_st_nen(word)]
    
    if len(word) > 1 and word[-2:] == 'si':
        return [get_gen_st_si(word)]
    
    if len(word) and word[-1] == 'i':
        # Always produce both variants here, one with i (default)
        # and one with e.
        return [get_gen_st_1(word),
                get_gen_st_1(word[:-1] + 'e')]
    
    # We default to sanatyyppi 1 if we don't find a better match.
    # if word[-1] in base_fi.FRONT_VOWELS + base_fi.BACK_VOWELS:
    return [get_gen_st_1(word)]

# Generate the partitiivi of the specified word.
# ** Note that this returns a *list of candidates* whenever the
#    sanatyyppi is ambiguous. This is currently the case for -i
#    suffixes. The reason is that we're using these candidates
#    to build an index. Not having a valid form in the index is
#    strictly worse than having an invalid form in it. **
def get_partitiivi(word):
    suffix_vowel = 'a' if base_fi.is_back_word(word) else 'ä'
    # Special casing for different sanatyyppit.
    # TODO(aeckleder): Not all sanatyyppit are implemented.
    if word[-1] == 'e':
        return [word + 'tt' + suffix_vowel]
    if len(word) > 2 and word[-3:] == 'nen':
        return [word[:-3] + 'st' + suffix_vowel]
    if len(word) > 1 and word[-2:] == 'si':
        return [word[:-2] + 'tt' + suffix_vowel]
    if len(word) and word[-1] == 'i':
        # Always produce three variants here, one with i (default),
        # one by dropping the i and one by replacing i with e.
        return [
            word + suffix_vowel,
            word[:-1] + 't' + suffix_vowel,
            word[:-1] + 'e' + suffix_vowel]
    
    if (not base_fi.is_vowel(word[-1]) or
          len(word) > 1 and base_fi.is_vowel(word[-2]) and
          not (word[-2] in base_fi.NEUTRAL_VOWELS and word[-1] in ['a', 'ä'])):
        return [word + 't' + suffix_vowel]
    else:
        return [word + suffix_vowel]

# Produce declensions of the specified substantive
def get_declensions(word):
    results = []
    gen_vartalo_candidates = get_genetiivivartalo(word)
    suffix_vowel = 'a' if base_fi.is_back_word(word) else 'ä'
    x = 0
    for gen_vartalo in gen_vartalo_candidates:

        idx = '' if x == 0 else ' (alt {idx})'.format(idx=x)
        
        # If we could build the genetiivi vartalo correctly,
        # we can generate several forms from it.
        results.append(('genetiivi' + idx, gen_vartalo + 'n'))
        results.append(('monikko' + idx, gen_vartalo + 't'))
        # Paikallissijat.
        # TODO(aeckleder): Add support for illatiivi.
        results.append(('inessiivi' + idx, gen_vartalo + 'ss' + suffix_vowel))
        results.append(('elatiivi' + idx, gen_vartalo + 'st' + suffix_vowel))
        results.append(('allatiivi' + idx, gen_vartalo + 'lle'))
        results.append(('adessiivi' + idx, gen_vartalo + 'll' + suffix_vowel))
        results.append(('ablatiivi' + idx, gen_vartalo + 'lt' + suffix_vowel))

        x = x + 1

    part_candidates = get_partitiivi(word)
    x = 0
    for part in part_candidates:
        idx = '' if x == 0 else ' (alt {idx})'.format(idx=x)        
        results.append(('partitiivi' + idx, part))
        x = x + 1
    
    return results
