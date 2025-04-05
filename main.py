import music21

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

mainscore.write("musicxml", "stuff.xml")