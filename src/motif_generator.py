# Chord-tone [0]
# Diatonic-step (Up [1] or down [2])
# Chromatic-Step (Up [3] or down [4])
# Leap to chord tone [5]

import random
import music21
import harmony_generator

def genRhythmicMotif(num_beats, possible_durations):
    rhythm = []
    counter = num_beats*4
    while counter > 0:
        randomSubtract = random.choice(possible_durations)
        rhythm.append(min(randomSubtract, counter))
        counter -= randomSubtract
    return rhythm

def genMelodicMotif(num_notes):
    mel_motif = []
    mel_motif.append(0)
    prev_val = 0

    while len(mel_motif) < num_notes:
        randomness = random.randint(0, 7)
        next_note = 0
        if prev_val == 0:
            next_note = random.randint(0, 5)
        if prev_val == 1:
            if 0 <= randomness <= 3:
                next_note = 2
            elif 4 <= randomness <= 6:
                next_note = 1
            elif randomness == 7:
                next_note = 5
        if prev_val == 2:
            if 0 <= randomness <= 3:
                next_note = 1
            elif 4 <= randomness <= 6:
                next_note = 2
            elif randomness == 7:
                next_note = 5
        if prev_val == 3:
            if 0 <= randomness <= 3:
                next_note = 4
            elif 5 <= randomness <= 7:
                next_note = 5
        if prev_val == 4:
            if 0 <= randomness <= 3:
                next_note = 3
            elif 5 <= randomness <= 7:
                next_note = 5
        if prev_val == 5:
            if 0 <= randomness <= 3:
                next_note = 1
            elif 5 <= randomness <= 7:
                next_note = 3
        mel_motif.append(next_note)
    return mel_motif

def genMelodyMeasure(chord, rhythm, melody):
    musicArray = music21.stream.Stream()
    startTone = random.choice(chord)

    for idx, (r, m) in enumerate(zip(rhythm, melody)):
        new_note = music21.note.Note('C5')
        if idx == 0:
            new_note = startTone
        else:
            if m == 1:
                new_note = musicArray[idx-1].transpose(2)
            elif m == 2:
                new_note = musicArray[idx-1].transpose(-2)
            elif m == 3:
                new_note = musicArray[idx-1].transpose(1)
            elif m == 4:
                new_note = musicArray[idx-1].transpose(-1)
            elif m == 5:
                random_chord_tone = random.choice(chord)
                harmony_generator.moveNoteClosestHigher(musicArray[idx-1], random_chord_tone)
                new_note = random_chord_tone
        new_note.duration.quarterLength = r/4
        musicArray.append(new_note)
    return musicArray