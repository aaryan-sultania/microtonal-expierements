import music21
import func_chords
from transitions import major_transitions, minor_transitions
import random

def translateNote(in_note: tuple, key="M"):
    n1string = ""
    if key=="M":
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
    if key=="m":
        if in_note[0] == 1:
            n1string = "A2"
        elif in_note[0] == 2:
            n1string = "B2"
        elif in_note[0] == 3:
            n1string = "C3"
        elif in_note[0] == 4:
            n1string = "D3"
        elif in_note[0] == 5:
            n1string = "E3"
        elif in_note[0] == 6:
            n1string = "F3"
        elif in_note[0] == 7:
            n1string = "G3"
    
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
    return random.randint(0, len(array) - 1)

def genFuncHarmony(key, flavor):
    harmony_array = []
    transition_array = []
    harmony_array.append((func_chords.minor_chord_i, 0))
    next_chord = (func_chords.minor_chord_i, 0)

    while len(harmony_array) < 8:
        possible_transitions = []
        for transition in minor_transitions:
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

# For future refrence:
# If a varible name has "_notes" at the end, it represents a collection of tones without a specifc register

def genM21ChordArray(func_harmony, func_transition, key):
    m21ify_func_harm_notes = []
    for f_chord in func_harmony:
        m21ify_chord_notes = []
        for f_degree in f_chord[0]:
            m21ify_chord_notes.append(translateNote(f_degree, key))
        m21ify_func_harm_notes.append(m21ify_chord_notes)

    m21_chord_array = []
    for idx in range(len(m21ify_func_harm_notes)):
        if idx == 0:
            m21_chord_array.append(m21ify_func_harm_notes[idx])
            continue
        transit = func_transition[idx - 1]
        previous_chord = m21_chord_array[idx - 1]
        previous_chord_notes = m21ify_func_harm_notes[idx - 1]
        this_chord_notes = m21ify_func_harm_notes[idx]

        this_chord = []
        current_lowest_note = music21.note.Note()
        if transit.transition_rules != None:
            for rule in transit.transition_rules:
                #print(rule[0], len(previous_chord_notes))
                p1 = previous_chord_notes[rule[0]].pitch
                for anote in previous_chord:
                    new_note = previous_chord_notes[rule[1]]
                    if p1.pitchClass == anote.pitch.pitchClass:
                        moveNoteClosest(anote, new_note)
                    this_chord.append(new_note)
            current_lowest_note = min(this_chord, key=lambda obj: obj.pitch.ps)
            
        if current_lowest_note.pitch.pitchClass != this_chord_notes[func_harmony[idx][1]].pitch.pitchClass:
            new_note = this_chord_notes[func_harmony[idx][1]]
            moveNoteClosestLower(current_lowest_note, new_note)
            current_lowest_note = new_note
            this_chord.append(new_note)
            
        for cnote in this_chord_notes:
            if not any(x.pitch.pitchClass == cnote.pitch.pitchClass for x in this_chord):
                moveNoteClosestHigher(current_lowest_note, cnote)
                this_chord.append(cnote)
                m21_chord_array.append(this_chord)


    return m21ify_func_harm_notes

def moveNoteClosest(n1, n2):
    
    n2.pitch.octave = n1.pitch.octave - 1
    low_octave_int = abs(music21.interval.Interval(n1.pitch, n2.pitch).semitones)
    n2.pitch.octave = n1.pitch.octave
    same_octave_int = abs(music21.interval.Interval(n1.pitch, n2.pitch).semitones)
    n2.pitch.octave = n1.pitch.octave + 1
    high_octave_int = abs(music21.interval.Interval(n1.pitch, n2.pitch).semitones)

    closest_int = min((low_octave_int, same_octave_int, high_octave_int))
    if closest_int == low_octave_int:
        n2.pitch.octave = n1.pitch.octave - 1
    elif closest_int == same_octave_int:
        n2.pitch.octave = n1.pitch.octave
    elif closest_int == high_octave_int:
        n2.pitch.octave = n1.pitch.octave + 1
def moveNoteClosestLower(n1, n2):
    if music21.interval.Interval(n1.pitch, n2.pitch).semitones > 0:
        n2.pitch.octave -= 1
        moveNoteClosestLower(n1, n2)
    if music21.interval.Interval(n1.pitch, n2.pitch).semitones < -11:
        n2.pitch.octave += 1
        moveNoteClosestLower(n1, n2)
    else:
        pass
        #print(music21.interval.Interval(n1.pitch, n2.pitch).semitones)

def moveNoteClosestHigher(n1, n2):
    if music21.interval.Interval(n1.pitch, n2.pitch).semitones < 0:
        n2.pitch.octave += 1
        moveNoteClosestHigher(n1, n2)
    if music21.interval.Interval(n1.pitch, n2.pitch).semitones > 11:
        n2.pitch.octave -= 1
        moveNoteClosestHigher(n1, n2)