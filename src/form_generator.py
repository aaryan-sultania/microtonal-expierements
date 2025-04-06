import music21
import motif_generator
import harmony_generator
import random
from copy import deepcopy
def genLeftHandMeasures(note_array):
    lefthandphrase = music21.stream.Stream()
    for chor in note_array:
        lefthand = music21.stream.Measure()
        low_note = min(chor, key=lambda obj: obj.pitch.ps)
        base_note = low_note.transpose(-12)
        base_note.duration.quarterLength = 1
        chord_note = music21.chord.Chord(notes=chor)
        chord_note.duration.quarterLength = 1
        other_chord_note = deepcopy(chord_note)
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

def genPiece():
    

    return (lefthandpart, righthandpart)
    

