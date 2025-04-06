import music21
import harmony_generator

mainscore = music21.stream.Score()

righthandpart = music21.stream.Part()
lefthandpart = music21.stream.Part()

ts = music21.meter.TimeSignature('4/4')
mm = music21.tempo.MetronomeMark(number=120) # 120 bpm

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
    n1.transpose(in_note[1], inPlace=True)
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
righthandpart.append(ts)
righthandpart.append(mm)

lefthandpart.append(ts)
lefthandpart.append(mm)

harmony = harmony_generator.genFuncHarmony(0, 0)
for i_har in harmony:
    print(i_har)
    print(convertChord(i_har).notes)
    lefthandpart.append(convertChord(i_har))

mainscore.insert(0, righthandpart)
mainscore.insert(0, lefthandpart)

mainscore.write("musicxml", "stuff.xml")