# -*- coding: utf-8 -*-
#
# Module containing Finnish grammar rules to generate
# conjugations from basic forms (verbs in infinitive etc.).

import base_structures_fi as base_fi
import kpt_fi

# Returns True if for the specified verb the suffix vowel is doubled
# in third person singular. This is the case for most verbityyppit,
# except for vt2, and for vt4 ini case the vartalo ends with
# an 'a' or 'ä'.
def is_double_3ps(verb):
    return (verb[-2:] not in ['da', 'dä'] and
            verb[-3:] not in ['ata', 'ätä'])

# Generic verb conjugator for present tense. This works
# for all verbityyppit with some preprocessing:
#  inf:     The original infinitive of the verb.
#  vartalo: The vartalo after removing the infinitive
#           suffix.
#  connector: Any connector to add between vartalo and
#             person suffix
#  strength_map: for each conjugation, specifies
#                 'h': Convert the vartalo to heikko form
#                 'v': Convert the vartalo to vahva form
#                 '-': Leave the vartalo unmodified
#  vowel_group: Configure vokaaliharmonia by specifying either
#               'a' or 'ä' here. This is used for the 3pp ending.
def conjugate_present(inf, vartalo, connector, strength_map, vowel_group):
    double_3ps = is_double_3ps(inf)
    endings = ['n', 't', (vartalo+connector)[-1] if double_3ps else '',
               'mme', 'tte', 'v' + vowel_group + 't']
    conjugations = []
    for i in range(0, len(endings)):
        conjugations.append(
            ('{x}p{m} present'.format(x=i % 3 + 1,
                                      m='s' if i < 3 else 'p'),
             (kpt_fi.apply_kpt_vaihtelu(vartalo) if strength_map[i]=='h'
             else (kpt_fi.apply_inverse_kpt_vaihtelu(vartalo) if strength_map[i]=='v'
                   else vartalo)) + connector + endings[i]))
    return conjugations

# Return the verbityyppi of word as a number between 1 and 6.
# If the function can't positively determine the verb type, it will return 0.
def get_verbityyppi(word):
    if not word[-1] in ['a', 'ä']:
        # We're not a verb.
        return 0
    if word[-3:-1] == 'et':
        # Signature property of vt6 is eta/etä.
        return 6
    elif word[-3:-1] == 'it':
        # Signature property of vt5 is ita/itä.
        return 5
    elif word[-2] == 't' and base_fi.is_vowel(word[-3]):
        # Signature property of vt4 is a vowel + ta/tä where
        # vowel is not 'i' or 'e' (with exceptions that we don't
        # deal with here)
        return 4
    elif word[-2] in ['l', 'n', 'r'] or word[-3:-1] == 'st':
        # Signature property of vt3 is a la/lä/s-ta/s-tä/na/nä/ra/rä
        # suffix.
        return 3
    elif word[-2] == 'd':
        # Signature property of vt2 is a da/dä suffix.
        return 2
    elif base_fi.is_vowel(word[-2]):
        # Signature property of vt1 is vowel followed by a or ä.
        return 1
    # Unknown
    return 0

# Apply vt1 conjugation rules if applicable. Otherwise,
# returns an empty array.
def apply_present_vt1(word):
    if get_verbityyppi(word) != 1:
        return []
    # Remove the a/ä suffix.
    vartalo = word[:-1]
    # TODO: This is very incomplete.
    return conjugate_present(word, vartalo, connector='',
                             strength_map='hh-hh-',
                             vowel_group=word[-1])

# Apply vt2 conjugation rules if applicable. Otherwise,
# returns an empty array.
def apply_present_vt2(word):
    if get_verbityyppi(word) != 2:
        return []
    # Remove the da/dä suffix.
    vartalo = word[:-2]
    # TODO: This is very incomplete.
    return conjugate_present(word, vartalo, connector='',
                             strength_map='------',
                             vowel_group=word[-1])

# Apply vt3 conjugation rules if applicable. Otherwise,
# returns an empty array.
def apply_present_vt3(word):
    if get_verbityyppi(word) != 3:
        return []
    # Remove the Xa/Xä suffix
    vartalo = word[:-2]
    # TODO: This is very incomplete.
    return conjugate_present(word, vartalo, connector='e',
                             strength_map='vvvvvv',
                             vowel_group=word[-1])

# Apply vt4 conjugation rules if applicable. Otherwise,
# returns an empty array.
def apply_present_vt4(word):
    if get_verbityyppi(word) != 4:
        return []
    
    # Remove the ta/tä suffix.
    vartalo = word[:-2]
    # TODO: This is very incomplete.
    return conjugate_present(word, vartalo, connector=word[-1],
                             strength_map='vvvvvv',
                             vowel_group=word[-1])

# Apply vt5 conjugation rules if applicable. Otherwise,
# returns an empty array.
def apply_present_vt5(word):
    if get_verbityyppi(word) != 5:
        return []
    
    # Remove the ta/tä suffix
    vartalo = word[:-2]
    # TODO: This is very incomplete.
    return conjugate_present(word, vartalo, connector='tse',
                             strength_map='------',
                             vowel_group=word[-1])

# Apply vt6 conjugation rules if applicable. Otherwise,
# returns an empty array.
def apply_present_vt6(word):
    if get_verbityyppi(word) != 6:
        return []
    
    # Remove the ta/tä suffix
    vartalo = word[:-2]
    # TODO: This is very incomplete.
    return conjugate_present(word, vartalo, connector='ne',
                             strength_map='vvvvvv', vowel_group=word[-1])

# Conjugate a verb in the present tense. This function internally
# detects the correct verbityyppi (vt1 - vt6) and applies the corresponding
# rules.
def apply_present_tense(word):
    return (apply_present_vt1(word) +
            apply_present_vt2(word) +
            apply_present_vt3(word) +
            apply_present_vt4(word) +
            apply_present_vt5(word) +
            apply_present_vt6(word))

# Expects the present tense conjugation in c, and applies a transform
# to imperfekti.
def apply_imperfekti_add_i_cases(verb, c):
    last_vowel = c[0][-2]
    # We insert an i after the last vowel if it is o/ö/u/y and
    # it is not doubled.
    if (last_vowel not in ['o', 'ö', 'u', 'y'] or
        last_vowel == c[0][-3]):
        return []

    endings = ['n', 't', '', 'mme', 'tte', 'v' + c[5][-2] + 't']
    imperfekti = []
    num_3ps = 2 if is_double_3ps(verb) else 1
    
    for i in range(0, 6):
        imperfekti.append(
            ('{x}p{m} imperfekti'.format(x=i % 3 + 1,
                                      m='s' if i < 3 else 'p'),
            c[i][:-len(endings[i])] + 'i' + endings[i] if i != 2
            else c[i][:-(num_3ps - 1)] + 'i'))
    
    return imperfekti

# Expects the present tense conjugation in c, and applies a transform
# to imperfekti.
def apply_imperfekti_replace_by_i_cases(verb, c):    
    last_vowel = c[0][-2]
    # We replace the last vowel by i if it is a/ä/e/i or
    # if it is doubled.
    if not (last_vowel in ['a', 'ä', 'e', 'i'] or
            last_vowel == c[0][-3]):
        return []

    endings = ['n', 't', '', 'mme', 'tte', 'v' + c[5][-2] + 't']
    imperfekti = []
    num_3ps = 2 if is_double_3ps(verb) else 1
    
    for i in range(0, 6):
        imperfekti.append(
            ('{x}p{m} imperfekti'.format(x=i % 3 + 1,
                                      m='s' if i < 3 else 'p'),
            c[i][:-len(endings[i])-1] + 'i' + endings[i] if i != 2
            else c[i][:-num_3ps] + 'i'))
    
    return imperfekti

# Conjugate a verb in imperfekti. This function is based on present tense
# conjugations and doesn't care much about verbityyppit (with exceptions).
def apply_imperfekti(word):
    # Start with the present tense and apply a set of transformation rules.
    c = [w[1] for w in apply_present_tense(word)]
    if not c:
        print("Doesn't seem to be a verb: {word}".format(word=word))
        return []

    # Check for ie->ei/yö->öi/uo->oi transformations.
    vv = c[0][-3:-1]
    replacements = {'ie': 'ei', 'yö' : 'öi', 'uo' : 'oi'}
    if vv in replacements.keys():
        # Reverse the vowels and their replacement
        rev_rep = replacements[vv][::-1]
        rev_vv = vv[::-1]
        for i in range(0, len(c)):
            c[i] = c[i][::-1].replace(rev_vv, rev_rep, 1)[::-1]

    # Some vt1 verbs build the imperfekti like vt4 verbs.
    v1_exception_list = ['huutaa', 'kieltää', 'kääntää', 'lentää', 'löytää',
                         'piirtää', 'pyytää', 'rakentaa', 'siirtä', 'tietää',
                         'tuntea', 'työntää', 'ymmärtää']

    vt = get_verbityyppi(word)
    if vt == 4 or (vt == 1 and word in v1_exception_list):
        # a/ä -> si for vt 4 or xa/xä -> si when in v1_exception_list
        len_stem = len(c[0]) - (2 if vt == 4 else 3)
        for i in range(0, len(c)):
            c[i] = c[i][:len_stem] + 'si' + c[i][len_stem + (1 if vt == 4 else 2):]
            
    # Check for a->o transformation. This happens as the last transformation,
    # because otherwise it might break some of the ones above.
    syllables = base_fi.split_syllables(c[2])
    # kpt-vaihtelu might collapse the second syllable into the first one.
    # If so, the replacement has to happen for the last 'a' of the first
    # syllable.
    has_collapsed_syllables = len(base_fi.split_syllables(c[0])) < len(syllables)

    if len(syllables) == 2 and 'a' in syllables[0] and 'a' in syllables[1]:
        for i in range(0, len(c)):
            # Replace a->o in the second syllable
            # (the suffix might have generated more).
            s = base_fi.split_syllables(c[i])
            # We have collapsed syllables in the heikko form, but that doesn't matter
            # for 3ps and 3pp, which are always vahva.
            rep_index = 0 if (has_collapsed_syllables and i != 2 and i != 5) else 1
            # Apply only to the final 'a', except for 3ps if the final
            # 'a' doubles.
            if s[rep_index][-2:] == 'aa':
                # The second 'o' will just be dropped for 3ps forms where
                # the vowel suffix is doubled.
                s[rep_index] = s[rep_index][:-2] + 'oo'
            else:
                s[rep_index] = s[rep_index][::-1].replace('a', 'o', 1)[::-1]
            c[i] = "".join(s)
            
    return (apply_imperfekti_add_i_cases(word, c) +
            apply_imperfekti_replace_by_i_cases(word, c))

# Produce conjugations and other inflections of the specified verb.
def get_conjugations(word):
    return (apply_present_tense(word) +
            apply_imperfekti(word))
