# Each note is represented with a tuple, (scale degree, accidental)
# A sharp is represented with a 1, natural with a 0, and flat with a -1
# First note is always root, the other notes are in order of inversion

# Triads in major keys.

major_chord_I = ((1, 0), (3, 0), (5, 0))
major_chord_i = ((1, 0), (3, -1), (5, 0))

major_chord_II = ((2, 0), (4, 1), (6, 0))
major_chord_ii = ((2, 0), (4, 0), (6, 0))

major_chord_III = ((3, 0), (5, 1), (7, 0))
major_chord_iii = ((4, 0), (6, 0), (1, 0))

major_chord_IV = ((4, 0), (6, 0), (1, 0))
major_chord_iv = ((4, 0), (6, -1), (1, 0))

major_chord_V = ((5, 0), (7, 0), (2, 0))
major_chord_v = ((5, 0), (7, -1), (2, 0)) 

major_chord_VI = ((6, 0), (1, 1), (3, 0))
major_chord_vi = ((6, 0), (1, 0), (3, 0))

major_chord_vii = ((7, 0), (2, 0), (4, 1))
major_chord_vii = ((7, 0), (2, 1), (4, 1))
major_chord_viio = ((7, 0), (2, 0), (4, 0))

# Common Seventh Chords in Major Keys
major_chord_V7 = ((5, 0), (7, 0), (2, 0), (4, 0)) # Dominant 7th Chord
major_chord_V7_V = ((2, 0), (4, 1), (6, 0), (1, 0)) # Secondary Dominant 7th Chord
major_chord_viio7 = ((7, 0), (2, 0), (4, 0), (1, -1)) # Diminished 7th Chord
major_chord_viihalfo7 = ((7, 0), (2, 0), (4, 0), (1, 0)) # Half Diminished 7th Chord

# Augmented 6th Chords in Major Keys
major_chord_itaug6 = ((6, -1), (1, 0), (4, 1)) 
major_chord_fraug6 = ((6, -1), (1, 0), (2, 0),  (4, 1))
major_chord_graug6 = ((6, -1), (1, 0), (3, -1), (4, 1))

# Other Cool Chords in Major Keys
major_chord_bII = ((2, -1), (4, 0), (6, -1)) 