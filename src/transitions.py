import chords

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
    Transition(chords.major_chord_I, (0, 1), chords.major_chord_V, (0, 1, 2), None, 0),
    Transition(chords.major_chord_I, (0, 1), chords.major_chord_IV, (0, 1, 2), None, 5),
    Transition(chords.major_chord_I, (0, 1), chords.major_chord_iv, (0, 2), None, 20),
    Transition(chords.major_chord_I, (0, 1), chords.major_chord_ii, (0, 1), None, 10),
    Transition(chords.major_chord_I, (0, 1), chords.major_chord_bII, (1,), None, 15),
    Transition(chords.major_chord_I, (0, 1), chords.major_chord_itaug6, (0,), None, 40),
    Transition(chords.major_chord_I, (0, 1), chords.major_chord_fraug6, (0,), None, 40),
    Transition(chords.major_chord_I, (0, 1), chords.major_chord_graug6, (0,), None, 40),
    Transition(chords.major_chord_I, (0, 1), chords.major_chord_V7, (0,), None, 5),
    Transition(chords.major_chord_I, (0, 1), chords.major_chord_V7_V, (0,), None, 10),
    Transition(chords.major_chord_I, (0, 1), chords.major_chord_viihalfo7, (0, 1, 2, 3), None, 60),
    Transition(chords.major_chord_I, (0, 1), chords.major_chord_viio7, (0, 1), None, 80),

    Transition(chords.major_chord_V, (0, 1, 2), chords.major_chord_I, (0,), None, 0),
    Transition(chords.major_chord_V, (0, 1, 2), chords.major_chord_vi, (0, 1, 2), None, 20),

    Transition(chords.major_chord_IV, (0, 1, 2), chords.major_chord_I, (0,), None, 0),
    Transition(chords.major_chord_IV, (0, 1, 2), chords.major_chord_V, (0, 1, 2), None, 0),
    Transition(chords.major_chord_IV, (0,), chords.major_chord_iv, (0,), None, 60),
    Transition(chords.major_chord_IV, (1,), chords.major_chord_iv, (1,), None, 60),
    Transition(chords.major_chord_IV, (2,), chords.major_chord_iv, (2,), None, 60),

    Transition(chords.major_chord_iv, (0, 1, 2), chords.major_chord_I, (0,), None, 0),

    Transition(chords.major_chord_ii, (0, 1, 2), chords.major_chord_V, (0, 1, 2), None, 0),
    Transition(chords.major_chord_bII, (0, 1, 2), chords.major_chord_V, (0, 1, 2), None, 0),

    Transition(chords.major_chord_itaug6, (0,), chords.major_chord_I, (2,), None, 20),
    Transition(chords.major_chord_itaug6, (0,), chords.major_chord_V, (0,), None, 20),
    Transition(chords.major_chord_fraug6, (0,), chords.major_chord_I, (2,), None, 20),
    Transition(chords.major_chord_fraug6, (0,), chords.major_chord_V, (0,), None, 20),
    Transition(chords.major_chord_graug6, (0,), chords.major_chord_I, (2,), None, 20),
    Transition(chords.major_chord_graug6, (0,), chords.major_chord_V, (0,), None, 20),

    Transition(chords.major_chord_V7, (0, 1, 2), chords.major_chord_I, (0,), None, 0),
    Transition(chords.major_chord_V7_V, (0, 1, 2), chords.major_chord_V, (0,), None, 0),

    Transition(chords.major_chord_viihalfo7, (0, 1, 2, 3), chords.major_chord_I, (0, 1, 2), None, 60),
    Transition(chords.major_chord_viio7, (0, 1, 2, 3), chords.major_chord_I, (0,), None, 80),

    Transition(chords.major_chord_I, (2,), chords.major_chord_V, (0,), None, 0),
    Transition(chords.major_chord_vi, (0, 1, 2), chords.major_chord_I, (0,), None, 0)
)