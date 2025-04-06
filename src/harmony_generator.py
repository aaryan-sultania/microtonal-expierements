import chords
from transitions import major_transitions
import random

def genRandomIndex(array):
    if len(array) == 1:
        return 0
    print(len(array))
    return random.randint(0, len(array) - 1)

def genFuncHarmony(maj_or_min, flavor):
    harmony_array = []
    harmony_array.append((chords.major_chord_I, 0))
    next_chord = (chords.major_chord_I, 0)
    while len(harmony_array) < 8:
        possible_transitions = []
        for transition in major_transitions:
            if (next_chord[0] == transition.chord1 and next_chord[1] in transition.inv1):
                possible_transitions.append(transition)

        if len(possible_transitions) == 0:
            print("Warning!")
            print(next_chord)

        next_transition = possible_transitions[genRandomIndex(possible_transitions)]
        next_inversion = next_transition.inv2[genRandomIndex(next_transition.inv2)]
        next_chord = (next_transition.chord2, next_inversion)
        harmony_array.append(next_chord)

        #for transition in possible_transitions:
        #   100 - abs(flavor - transition.flavor)
    return harmony_array

