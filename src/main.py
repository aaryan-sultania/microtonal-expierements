import music21
import harmony_generator

mainscore = music21.stream.Score()

righthandpart = music21.stream.Part()
lefthandpart = music21.stream.Part()

ts = music21.meter.TimeSignature('4/4')
mm = music21.tempo.MetronomeMark(number=120) # 120 bpm

righthandpart.append(ts)
righthandpart.append(mm)

lefthandpart.append(ts)
lefthandpart.append(mm)

mainscore.insert(0, righthandpart)
mainscore.insert(0, lefthandpart)

print(harmony_generator.genM21ChordArray(*harmony_generator.genFuncHarmony(0, 0)))

mainscore.write("musicxml", "stuff.xml")