import music21
import func_chords
from transitions import major_transitions
import random

def translateNote(in_note: tuple):
    n1string = ""
    if in_note[0] == 1:
        n1string = "C3"
    elif in_note[0] == 2:
        n1string = "D3"
    elif in_note[0] == 3:
        n1string = "E3"
    elif in_note[0] == 4:
        n1string = "F3"
    elif in_note[0] == 5:
        n1string = "G3"
    elif in_note[0] == 6:
        n1string = "A3"
    elif in_note[0] == 7:
        n1string = "B3"
    
    n1 = music21.note.Note(n1string);

    if (in_note[1] == -1) :
        n1.pitch.accidental = music21.pitch.Accidental('flat')
    if (in_note[1] == 1) :
        n1.pitch.accidental = music21.pitch.Accidental('sharp')
    
    #n1.transpose(in_note[1], inPlace=True)
    #n1.pitch.accidental.alter = in_note[1]
    return n1

def convertChord(in_chord: tuple):
    note_index = in_chord[1]
    num_notes = 0
    note_list = []
    transpose_up = False
    while (num_notes < len(in_chord[0])):
        n1 = translateNote(in_chord[0][note_index % len(in_chord[0])])
        if in_chord[0][(note_index-1) % len(in_chord[0])][0] > in_chord[0][(note_index) % len(in_chord[0])][0] and num_notes > 0:
            transpose_up = True
        if transpose_up:
            n1.octave += 1
        note_list.append(n1)
        num_notes += 1
        note_index += 1
    return music21.chord.Chord(note_list)

#for i_har in harmony:
#    print(i_har)
#    print(convertChord(i_har).notes)
#    lefthandpart.append(convertChord(i_har))

def genRandomIndex(array):
    if len(array) == 1:
        return 0
    print(len(array))
    return random.randint(0, len(array) - 1)

def genFuncHarmony(maj_or_min, flavor):
    harmony_array = []
    transition_array = []
    harmony_array.append((func_chords.major_chord_I, 0))
    next_chord = (func_chords.major_chord_I, 0)
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
        transition_array.append(next_transition)

        #for transition in possible_transitions:
        #   100 - abs(flavor - transition.flavor)
    return (harmony_array, transition_array)

def genM21ChordArray(func_harmony, func_transition):
    m21ify_func_harm_notes = []
    for f_chord in func_harmony:
        m21ify_chord_notes = []
        for f_degree in f_chord[0]:
            m21ify_chord_notes.append(translateNote(f_degree))
        m21ify_func_harm_notes.append(m21ify_chord_notes)
    return m21ify_func_harm_notes
    