import music21
import harmony_generator

mainscore = music21.stream.Score()

righthandpart = music21.stream.Part()
lefthandpart = music21.stream.Part()

ts = music21.meter.TimeSignature('3/4')
mm = music21.tempo.MetronomeMark(number=120) # 120 bpm

righthandpart.append(ts)
righthandpart.append(mm)

lefthandpart.append(ts)
lefthandpart.append(mm)

mainscore.insert(0, righthandpart)
mainscore.insert(0, lefthandpart)

note_array = (harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony(0, 0)))
print(note_array)
for chor in note_array:
    low_note = min(chor, key=lambda obj: obj.pitch.ps)
    base_note = low_note.transpose(-12)
    lefthandpart.append(base_note)
    lefthandpart.append(music21.chord.Chord(notes=chor))
    lefthandpart.append(music21.chord.Chord(notes=chor))

mainscore.write("musicxml", "stuff.xml")