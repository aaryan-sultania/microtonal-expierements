# Chord-tone [0]
# Diatonic-step (Up [1] or down [2])
# Chromatic-Step (Up [3] or down [4])
# Leap to chord tone [5]

# Give up on that above heres smth simpler
# Chord-tone Up [0] Down [1]
# Non Chord Tone Up [2] Down [3] 
# Appogitura on next note From Up [4] From Down [5]


import random
import music21
import harmony_generator
import copy

def genRhythmicMotif(num_beats, possible_durations):
    rhythm = []
    counter = num_beats*4
    while counter > 0:
        randomSubtract = random.choice(possible_durations)
        rhythm.append(min(randomSubtract, counter))
        counter -= randomSubtract
    return rhythm

def genMelodicMotif(num_notes, poss_stuff):
    mel_motif = []
    mel_motif.append(0)
    counter = num_notes - 1
    while counter > 0:
        randomSubtract = min(random.randint(1, 2), counter)
        if randomSubtract == 1:
            mel_motif.append(random.randint(0, 1))
        if randomSubtract == 2:
            mel_motif.append(random.randint(2, 5))
        counter -= randomSubtract

def genMelodicMeasure(start_tone, chord_notes, rhythm, mel_motif):
    melody_notes = [chord_notes[start_tone]]
    

def genMelodyMeasure(chord, rhythm, melody):
    musicArray = music21.stream.Stream()
    startTone = random.choice(chord)
    startTone.octave = 5

    for idx, (r, m) in enumerate(zip(rhythm, melody)):
        new_note = music21.note.Note('C5')
        if idx == 0:
            new_note = startTone
        else:
            if m == 1:
                #print("A")
                new_note = diatonic_transpose(musicArray[idx-1], 1)
            elif m == 2:
                #print("B")
                new_note = diatonic_transpose(musicArray[idx-1], -1)
            elif m == 3:
                #print("C")
                new_note = diatonic_transpose(musicArray[idx-1], 1)
            elif m == 4:
                #print("D")
                new_note = diatonic_transpose(musicArray[idx-1], -1)
            elif m == 5:
                #print("E")
                random_chord_tone = random.choice(chord)
                harmony_generator.moveNoteClosestHigher(musicArray[idx-1], random_chord_tone)
                new_note = copy.deepcopy(random_chord_tone)
            
        new_note.duration.quarterLength = r/4
        test_thingy = new_note
        musicArray.append(test_thingy)
    return musicArray

def diatonic_transpose(note, dirrection):
    if note.pitch.pitchClass == 11 and dirrection == 1:
        return note.transpose(1)      
    elif note.pitch.pitchClass == 0 and dirrection == -1:
        return note.transpose(-1)
    elif note.pitch.pitchClass == 4 and dirrection == 1:
        return note.transpose(1)
    elif note.pitch.pitchClass == 5 and dirrection == -1:
        return note.transpose(-1)
    else:
        return note.transpose(2*dirrection)