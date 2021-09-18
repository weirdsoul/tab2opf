# -*- coding: utf-8 -*-
#
# Module containing kpt transformations for Finnish grammar.

import base_structures_fi as base_fi

# Apply kpt-vaihtelu to the specified word. This essentially
# converts vahva into heikko and is lossy.
def apply_kpt_vaihtelu(word):
    syllables = base_fi.split_syllables(word)
    if len(syllables) < 2:
        # The first syllable is never subject to (inverse) kpt vaihtelu.
        return word
    # We generally modify only the first character of the last syllable
    # (always a consonant), but we are also interested in the last character
    # of the previous syllable.
    last_syllable = syllables[-1]
    prev_syllable = syllables[-2] if len(syllables) > 1 else None

    # First character of a kpt tuple or None.
    first_kpt = prev_syllable[-1] if prev_syllable else None
    # This is the one we might be modifying, it always exists initially, but
    # might be set to None for a deletion.
    second_kpt = last_syllable[0]

    if second_kpt == 'k':
        if first_kpt == 'n':    # 'nk' -> 'ng' case
            second_kpt = 'g'
        elif first_kpt != 's' and first_kpt != 't': # 'k' -> '' and 'kk' -> 'k' cases
            second_kpt = None
        # If preceeded by 's' or 'k', just keep the 'k'.
    elif second_kpt == 'p':
        if first_kpt == 'm':   # 'mp' -> 'mm' case
            second_kpt = 'm'
        elif first_kpt == 'p': # 'pp' -> 'p' case
            second_kpt = None
        else:
            second_kpt = 'v'   # 'p' -> 'v'
    elif second_kpt == 't':
        if first_kpt == 'n':   # 'nt' -> 'nn'
            second_kpt = 'n'
        elif first_kpt == 'l':  # 'lt' -> 'll'
            second_kpt = 'l'
        elif first_kpt == 'r':  # 'rt' -> 'rr'
            second_kpt = 'r'
        elif first_kpt == 't':  # 'tt' -> 't'
            second_kpt = None
        elif first_kpt != 's':
            second_kpt = 'd'
        # If preceeded by 's', just keep the 't'.

    last_syllable = last_syllable[1:]
    if second_kpt:
        last_syllable = second_kpt + last_syllable
    return "".join(syllables[:-1] + [last_syllable])

# Apply inverse kpt-vaihtelu to the specified word. This essentially
# converts heikko into vahva.
def apply_inverse_kpt_vaihtelu(word):
    syllables = base_fi.split_syllables(word)
    if len(syllables) < 2:
        # The first syllable is never subject to (inverse) kpt vaihtelu.
        return word
    # We generally modify only the last syllable: We either modify its first letter
    # or insert a letter (k->kk, p->pp, t->tt, _->k). We are also interested in the
    # last character of the previous syllable.
    last_syllable = syllables[-1]
    prev_syllable = syllables[-2] if len(syllables) > 1 else None

    # First character of a kpt tuple or None.
    first_kpt = prev_syllable[-1] if prev_syllable else None
    # This is the one we might be modifying. Any insertions happen directly into
    # last_syllable.
    second_kpt = last_syllable[0]

    # TODO: _->'k' is unsupported, e.g. maata -> makaan.
    # 'sk' and 'tk' make it very unlikely that the strong form is 'skk' / 'tkk'.
    if second_kpt == 'k' and first_kpt not in ['s', 't']: 
        last_syllable = 'k' + last_syllable # 'k' -> 'kk'
    elif second_kpt == 'p':
        last_syllable = 'p' + last_syllable # 'p' -> 'pp'
    # 'st' makes it very unlikely that the strong form is 'stt'.
    elif second_kpt == 't' and first_kpt != 's':
        last_syllable = 't' + last_syllable # 't' -> 'tt'
    elif second_kpt == 'v':
        second_kpt = 'p' # 'c' -> 'p'
    elif second_kpt == 'd' and first_kpt not in ['s', 't']:
        second_kpt = 't' # 'd' -> 't'
    elif second_kpt == 'g' and first_kpt == 'n':
        second_kpt = 'k' # 'ng' -> 'nk'
    elif second_kpt == 'n' and first_kpt == 'n':
        second_kpt = 't' # 'nn' -> 'nt'
    elif second_kpt == 'm' and first_kpt == 'm':
        second_kpt = 'p' # 'mm' -> 'mp'
    elif second_kpt == 'l' and first_kpt == 'l':
        second_kpt = 't' # 'll' -> 'lt'
    elif second_kpt == 'r' and first_kpt == 'r':
        second_kpt = 't' # 'rr' -> 'rt'

    last_syllable = second_kpt + last_syllable[1:]
    return "".join(syllables[:-1] + [last_syllable])

