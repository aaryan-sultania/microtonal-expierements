import music21
import harmony_generator
import random
import motif_generator
from copy import deepcopy

mainscore = music21.stream.Score()

def genLeftHandMeasures(note_array):
    lefthandphrase = music21.stream.Stream()
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
    
def genRightHandMeasures(note_array, rhythm1, melody1, rhythm2, melody2):
    righthandphrase = music21.stream.Stream()
    for idx, chor in enumerate(note_array):
        melody_note = random.choice(chor).transpose(12)
        melody_note.duration = music21.duration.Duration(quarterLength=2)
        next_note = melody_note.transpose(-2)
        next_note.duration = music21.duration.Duration(quarterLength=1)
        ryth = rhythm1 if idx % 2 else rhythm2
        meld = melody1 if idx % 2 else melody2
        righthandphrase.append(motif_generator.genMelodyMeasure(chor, ryth, meld))
    return righthandphrase

righthandpart = music21.stream.Part()
lefthandpart = music21.stream.Part()

random.seed(42)

note_array_1 = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony("m", 0), "m"))
note_array_2 = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony("m", 0), "m"))
note_array_3 = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony("M", 0), "M"))
note_array_4 = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony("M", 0), "M"))
rhythm11 = motif_generator.genRhythmicMotif(3, (1, 2, 3, 4))
melody11 = motif_generator.genMelodicMotif(len(rhythm11))
rhythm12 = motif_generator.genRhythmicMotif(3, (2, 4, 6, 8))
melody12 = motif_generator.genMelodicMotif(len(rhythm12))
rhythm21 = motif_generator.genRhythmicMotif(3, (1, 2, 3, 4))
melody21 = motif_generator.genMelodicMotif(len(rhythm11))
rhythm22 = motif_generator.genRhythmicMotif(3, (2, 4, 6, 8))
melody22 = motif_generator.genMelodicMotif(len(rhythm12))
rhythm31 = motif_generator.genRhythmicMotif(3, (1, 2, 3, 4))
melody31 = motif_generator.genMelodicMotif(len(rhythm11))
rhythm32 = motif_generator.genRhythmicMotif(3, (2, 4, 6, 8))
melody32 = motif_generator.genMelodicMotif(len(rhythm12))
rhythm41 = motif_generator.genRhythmicMotif(3, (1, 2, 3, 4))
melody41 = motif_generator.genMelodicMotif(len(rhythm11))
rhythm42 = motif_generator.genRhythmicMotif(3, (2, 4, 6, 8))
melody42 = motif_generator.genMelodicMotif(len(rhythm12))

ts = music21.meter.TimeSignature('3/4')
mm = music21.tempo.MetronomeMark(number=120) # 120 bpm
tc = music21.clef.TrebleClef()
bc = music21.clef.BassClef()

lefthandpart.append(ts)
lefthandpart.append(mm)
lefthandpart.append(bc)
lefthandpart.append(genLeftHandMeasures(note_array_1))
lefthandpart.append(genLeftHandMeasures(note_array_2))
lefthandpart.append(genLeftHandMeasures(note_array_3))
lefthandpart.append(genLeftHandMeasures(note_array_4))
lefthandpart.append(genLeftHandMeasures(note_array_1))
lefthandpart.append(genLeftHandMeasures(note_array_2))

righthandpart.append(ts)
righthandpart.append(mm)
righthandpart.append(tc)
righthandpart.append(genRightHandMeasures(note_array_1, rhythm11, melody11, rhythm12, melody12))
righthandpart.append(genRightHandMeasures(note_array_2, rhythm21, melody21, rhythm22, melody22))
righthandpart.append(genRightHandMeasures(note_array_3, rhythm31, melody31, rhythm32, melody32))
righthandpart.append(genRightHandMeasures(note_array_4, rhythm41, melody41, rhythm42, melody42))
righthandpart.append(genRightHandMeasures(note_array_1, rhythm11, melody11, rhythm12, melody12))
righthandpart.append(genRightHandMeasures(note_array_2, rhythm21, melody21, rhythm22, melody22))

mainscore.insert(0, righthandpart)
mainscore.insert(0, lefthandpart)

lefthandpart.write("musicxml", "output.xml")