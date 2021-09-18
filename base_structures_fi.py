# -*- coding: utf-8 -*-
#
# Module containing base structures for Finnish grammar.

FRONT_VOWELS = ['ä', 'ö', 'y']
BACK_VOWELS = ['a', 'o', 'u']
NEUTRAL_VOWELS = ['e', 'i']
ALL_VOWELS = FRONT_VOWELS + BACK_VOWELS + NEUTRAL_VOWELS

def is_vowel(c):
    return c in ALL_VOWELS

# We say that a word is a 'back word' if the first vowel we find
# starting from the end is a back vowel. If the first vowel is a front
# vowel, we return false. We generally ignore neutral vowels.
def is_back_word(word):
    for c in reversed(word):
        if c in BACK_VOWELS:
            return True
        if c in FRONT_VOWELS:
            return False
    return False

# The syllable splitter below is a simple state machine with the following states:
SY_INIT = 0            # Initial state of the current syllable
SY_VOWEL = 1           # Found a vowel
SY_END_OR_START_C = 2  # Found an end or start consonant

# Split a Finnish word into syllables. This is a heuristic that
# should hopefully be good enough for using it to apply kpt
# rules. It is clearly not an exact set of rules, which are
# complicated:
# https://web.stanford.edu/~laurik/fsmbook/exercises/FinnishSyllabification.html
# Basically, we pretend that a syllable starts with every consonant
# preceeded by a vowel. If such a consonant is followed by another
# consonant, we do the syllable split between the consonants and
# attribute the first consonant to the previous syllable.
# Returns a list of syllables that when concatenated
# in order make up the original word.
def split_syllables(word):
    syllables = []
    s = ''
    current_state = SY_INIT
    last_consonant = None
    for c in word:
        if current_state == SY_INIT:
            if is_vowel(c):
                current_state = SY_VOWEL
            # Always append the character in default state
            s = s + c
        elif current_state == SY_VOWEL:
            if is_vowel(c):
                # Immediately append any vowels we find.
                s = s + c
            else:
                # We don't yet know what to do with
                # the consonant, so just remember it
                # and proceed to the next state.
                current_state = SY_END_OR_START_C
                last_consonant = c
        elif current_state == SY_END_OR_START_C:
            if is_vowel(c):
                # We got a vowel, so the remembered consonant
                # will become the first character of our
                # new syllable.
                syllables.append(s)
                s = '' + last_consonant + c
                # We already found our next vowel, so change
                # directly into the associated state.
                current_state = SY_VOWEL
            else:
                # We got another consonant, so the remembered
                # one becomes the last character of the previous
                # syllable.
                s = s + last_consonant
                syllables.append(s)
                s = '' + c
                current_state = SY_INIT
            last_consonant = None
        else:
            raise "Undefined state machine state."

    if current_state == SY_END_OR_START_C:
        # Consonants can't stand alone, flush any remaining one.
        s = s + last_consonant
    if s:
        syllables.append(s)
    return syllables
