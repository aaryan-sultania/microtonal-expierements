import func_chords

class Transition:
    def __init__(self, chord1: tuple, inv1: tuple, chord2: tuple, inv2: tuple, trans_rules, flavor: int):
        self.chord1 = chord1
        self.inv1 = inv1
        self.chord2 = chord2
        self.inv2 = inv2
        self.transition_rules = trans_rules # For voice leading rules in the future
        self.flavor = flavor
        
# Adjust Flavors to Change Composition Style!
major_transitions = (
    Transition(func_chords.major_chord_I, (0, 1), func_chords.major_chord_V, (0, 1, 2), None, 0),
    Transition(func_chords.major_chord_I, (0, 1), func_chords.major_chord_IV, (0, 1, 2), None, 5),
    Transition(func_chords.major_chord_I, (0, 1), func_chords.major_chord_iv, (0, 2), None, 20),
    Transition(func_chords.major_chord_I, (0, 1), func_chords.major_chord_ii, (0, 1), None, 10),
    Transition(func_chords.major_chord_I, (0, 1), func_chords.major_chord_bII, (1,), None, 15),
    Transition(func_chords.major_chord_I, (0, 1), func_chords.major_chord_itaug6, (0,), None, 40),
    Transition(func_chords.major_chord_I, (0, 1), func_chords.major_chord_fraug6, (0,), None, 40),
    Transition(func_chords.major_chord_I, (0, 1), func_chords.major_chord_graug6, (0,), None, 40),
    Transition(func_chords.major_chord_I, (0, 1), func_chords.major_chord_V7, (0,), None, 5),
    Transition(func_chords.major_chord_I, (0, 1), func_chords.major_chord_V7_V, (0,), None, 10),
    Transition(func_chords.major_chord_I, (0, 1), func_chords.major_chord_viihalfo7, (0, 1, 2, 3), None, 60),
    Transition(func_chords.major_chord_I, (0, 1), func_chords.major_chord_viio7, (0, 1), None, 80),

    Transition(func_chords.major_chord_V, (0, 1, 2), func_chords.major_chord_I, (0,), ((1, 0),), 0),
    Transition(func_chords.major_chord_V, (0, 1, 2), func_chords.major_chord_vi, (0, 1, 2), None, 20),  
    Transition(func_chords.major_chord_IV, (0, 1, 2), func_chords.major_chord_I, (0,), ((0, 1), (1, 2)), 0),
    Transition(func_chords.major_chord_IV, (0, 1, 2), func_chords.major_chord_V, (0, 1, 2), None, 0),
    Transition(func_chords.major_chord_IV, (0,), func_chords.major_chord_iv, (0,), ((1, 1),), 60),
    Transition(func_chords.major_chord_IV, (1,), func_chords.major_chord_iv, (1,), ((1, 1),), 60),
    Transition(func_chords.major_chord_IV, (2,), func_chords.major_chord_iv, (2,), ((1, 1),), 60),

    Transition(func_chords.major_chord_iv, (0, 1, 2), func_chords.major_chord_I, (0,), ((0, 1), (1, 2)), 0),

    Transition(func_chords.major_chord_ii, (0, 1, 2), func_chords.major_chord_V, (0, 1, 2), ((1, 0), (2, 1)), 0),
    Transition(func_chords.major_chord_bII, (0, 1, 2), func_chords.major_chord_V, (0, 1, 2), None, 0),

    Transition(func_chords.major_chord_itaug6, (0,), func_chords.major_chord_I, (2,), ((0, 2), (2, 2)), 20),
    Transition(func_chords.major_chord_itaug6, (0,), func_chords.major_chord_V, (0,), ((0, 1), (2, 1)), 20),
    Transition(func_chords.major_chord_fraug6, (0,), func_chords.major_chord_I, (2,), ((0, 2), (3, 2)), 20),
    Transition(func_chords.major_chord_fraug6, (0,), func_chords.major_chord_V, (0,), ((0, 1), (3, 1)), 20),
    Transition(func_chords.major_chord_graug6, (0,), func_chords.major_chord_I, (2,), ((0, 2), (3, 2)), 20),
    Transition(func_chords.major_chord_graug6, (0,), func_chords.major_chord_V, (0,), ((0, 1), (3, 1)), 20),

    Transition(func_chords.major_chord_V7, (0, 1, 2), func_chords.major_chord_I, (0,), None, 0),
    Transition(func_chords.major_chord_V7_V, (0, 1, 2), func_chords.major_chord_V, (0,), None, 0),

    Transition(func_chords.major_chord_viihalfo7, (0, 1, 2, 3), func_chords.major_chord_I, (0, 1, 2), None, 60),
    Transition(func_chords.major_chord_viio7, (0, 1, 2, 3), func_chords.major_chord_I, (0,), None, 80),

    Transition(func_chords.major_chord_I, (2,), func_chords.major_chord_V, (0,), None, 0),
    Transition(func_chords.major_chord_vi, (0, 1, 2), func_chords.major_chord_I, (0,), None, 0)
)