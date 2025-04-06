import music21
import harmony_generator
import random
import motif_generator
from copy import deepcopy

mainscore = music21.stream.Score()

def genLeftHandMeasures(note_array):
    lefthandphrase = []
    for chor in note_array:
        lefthand = music21.stream.Measure()
        low_note = min(chor, key=lambda obj: obj.pitch.ps)
        base_note = low_note.transpose(-12)
        base_note.duration.quarterLength = 1
        chord_note = music21.chord.Chord(notes=chor)
        chord_note.duration.quarterLength = 1
        other_chord_note = music21.chord.Chord(notes=chor)
        other_chord_note.duration.quarterLength = 1
        lefthand.append(base_note)
        lefthand.append(chord_note)
        lefthand.append(other_chord_note)
        lefthandphrase.append(lefthand)
    return lefthandphrase

def genRightHandMeasures(note_array, rhythm):
    righthandphrase = []
    for chor in note_array:
        righthand = music21.stream.Measure()
        for movement in rhythm:
            not1 = deepcopy(random.choice(chor))
            not1.pitch.octave = 5
            not1.duration.quarterLength = movement/4
            righthand.append(not1)
            
        righthandphrase.append(righthand)
    return righthandphrase

righthandpart = music21.stream.Part()
lefthandpart = music21.stream.Part()

random.seed(42)

note_array_1 = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony("m", 0), "m"))
note_array_2 = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony("m", 0), "m"))
note_array_3 = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony("M", 0), "M"))
note_array_4 = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony("M", 0), "M"))


ts = music21.meter.TimeSignature('3/4')
mm = music21.tempo.MetronomeMark(number=120) # 120 bpm
tc = music21.clef.TrebleClef()
bc = music21.clef.BassClef()

righthandpart.append(ts)
righthandpart.append(mm)
righthandpart.append(tc)

lefthandpart.append(ts)
lefthandpart.append(mm)
lefthandpart.append(bc)

mainscore.insert(0, righthandpart)
mainscore.insert(0, lefthandpart)

lhv1 = genLeftHandMeasures(note_array_1)
lhv2 = genLeftHandMeasures(note_array_2)
lhv3 = genLeftHandMeasures(note_array_3)
lhv4 = genLeftHandMeasures(note_array_4)

rhv1 = genRightHandMeasures(note_array_1, motif_generator.genRhythmicMotif(3, (1, 2, 3, 4)))
rhv2 = genRightHandMeasures(note_array_2, motif_generator.genRhythmicMotif(3, (1, 2, 3, 4)))
rhv3 = genRightHandMeasures(note_array_3, motif_generator.genRhythmicMotif(3, (1, 2, 3, 4)))
rhv4 = genRightHandMeasures(note_array_4, motif_generator.genRhythmicMotif(3, (1, 2, 3, 4)))

for meas in lhv1:
    lefthandpart.append(meas)
for meas in lhv2:
    lefthandpart.append(meas)
for meas in lhv3:
    lefthandpart.append(meas)
for meas in lhv4:
    lefthandpart.append(meas)
for meas in lhv1:
    make_copy = deepcopy(meas)
    lefthandpart.append(make_copy)
for meas in lhv2:
    make_copy = deepcopy(meas)
    lefthandpart.append(make_copy)

for meas in rhv1:
    righthandpart.append(meas)
for meas in rhv2:
    righthandpart.append(meas)
for meas in rhv3:
    righthandpart.append(meas)
for meas in rhv4:
    righthandpart.append(meas)
for meas in rhv1:
    make_copy = deepcopy(meas)
    righthandpart.append(make_copy)
for meas in rhv2:
    make_copy = deepcopy(meas)
    righthandpart.append(make_copy)

mainscore.write("musicxml", "output.xml")
mainscore.write("midi", "output.midi")