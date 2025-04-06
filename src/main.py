import music21
import harmony_generator
import random
import motif_generator

mainscore = music21.stream.Score()

righthandpart = music21.stream.Part()
lefthandpart = music21.stream.Part()

ts = music21.meter.TimeSignature('3/4')
mm = music21.tempo.MetronomeMark(number=120) # 120 bpm
tc = music21.clef.TrebleClef()
bc = music21.clef.BassClef()

righthandpart.append(ts)
righthandpart.append(mm)
righthandpart.append(tc)

lefthandpart.append(ts)
lefthandpart.append(mm)
righthandpart.append(bc)

mainscore.insert(0, righthandpart)
mainscore.insert(0, lefthandpart)

note_array = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony(0, 0), "m"))
rhythm = motif_generator.genRhythmicMotif(3, (1, 2, 3, 4))
melody = motif_generator.genMelodicMotif(len(rhythm))

for chor in note_array:
    low_note = min(chor, key=lambda obj: obj.pitch.ps)
    base_note = low_note.transpose(-12)
    lefthandpart.append(base_note)
    lefthandpart.append(music21.chord.Chord(notes=chor))
    lefthandpart.append(music21.chord.Chord(notes=chor))

    melody_note = random.choice(chor).transpose(12)
    melody_note.duration = music21.duration.Duration(quarterLength=2)
    next_note = melody_note.transpose(-2)
    next_note.duration = music21.duration.Duration(quarterLength=1)
    righthandpart.append(motif_generator.genMelodyMeasure(chor, rhythm, melody))

print(zip(rhythm, melody))
mainscore.write("musicxml", "stuff.xml")