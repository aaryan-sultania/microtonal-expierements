import music21
import harmony_generator
import random
import motif_generator
from copy import deepcopy

semitone_key = int(input("Please enter a key (0 for C, 1 for C#, etc): "))
tonality = int(input("Please enter a tonality (0 for Major, 1 for Minor): "))
texture = int(input("Please enter a style (0 for Waltz, 1 for March, 2 for Sonataina): "))
seed = int(input("Please enter a random number seed: "))

interval_of_transposition = music21.interval.Interval(0)

meter = 0
if texture == 0:
    meter = 3
if texture == 1:
    meter = 2
if texture == 2:
    meter = 4
random.seed(seed)

mainscore = music21.stream.Score()

def genLeftHandMeasures(note_array):
    lefthandphrase = []
    for chor in note_array:
        lefthand = music21.stream.Measure()
        low_note = min(chor, key=lambda obj: obj.pitch.ps)
        low_note.transpose(interval_of_transposition, inPlace=True)

        if texture == 0 or texture == 1:
            base_note = low_note.transpose(-12)
            base_note.duration.quarterLength = 1
            chord_note = music21.chord.Chord(notes=chor)
            chord_note.duration.quarterLength = 1
            chord_note.transpose(interval_of_transposition, inPlace=True)
            if texture == 1:
                lefthand.append(base_note)
                lefthand.append(chord_note)
            if texture == 0:
                other_chord_note = music21.chord.Chord(notes=chor)
                other_chord_note.transpose(interval_of_transposition, inPlace=True)
                chord_note.duration.quarterLength = 1
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
            not1.transpose(interval_of_transposition, inPlace=True)
            not1.pitch.octave = 5
            not1.duration.quarterLength = movement/4
            righthand.append(not1)
            
        righthandphrase.append(righthand)
    return righthandphrase

righthandpart = music21.stream.Part()
lefthandpart = music21.stream.Part()



note_array_1 = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony(tonality, 0), tonality))
note_array_2 = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony(tonality, 0), tonality))
note_array_3 = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony(int(not tonality), 0), int(not tonality)))
note_array_4 = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony(int(not tonality), 0), int(not tonality)))


ts = music21.meter.TimeSignature(str(meter) + '/4')
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

rhv1 = genRightHandMeasures(note_array_1, motif_generator.genRhythmicMotif(meter, (2, 4, 6, 8)))
rhv2 = genRightHandMeasures(note_array_2, motif_generator.genRhythmicMotif(meter, (2, 4, 6, 8)))
rhv3 = genRightHandMeasures(note_array_3, motif_generator.genRhythmicMotif(meter, (2, 4, 6, 8)))
rhv4 = genRightHandMeasures(note_array_4, motif_generator.genRhythmicMotif(meter, (2, 4, 6, 8)))

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