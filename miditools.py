import os
from mido import MidiFile, MidiTrack
from music21 import converter, instrument
import time


def convert_mp3_to_midi(audio_name, bpm=60, smooth=0.15, minduration=0.15):
    cmd = "python27-32 audio_to_melodia.py ./Audio/" + audio_name + ".wav " + "./Audio/" + audio_name + ".mid "
    cmd += str(bpm) + " --smooth " + str(smooth) + " --minduration " + str(minduration)
    print("Executing " + cmd)
    os.system(cmd)

def convert_midi_to_mp3(audio_name):
    cmd = "timidity ./Audio/" + audio_name + ".mid -Ow -o ./Audio/" + audio_name + ".mp3"
    print("Executing " + cmd)
    os.system(cmd)


def get_midi_info(audio_name):
    mid = MidiFile('./Audio/'+ audio_name + ".mid")
    msg = mid.tracks[1][1]

    on_off = list()
    note = list()
    velocity = list()
    time = list()

    i = 1
    while (not msg.is_meta):
        on_off.append(msg.type)
        note.append(msg.note)
        velocity.append(msg.velocity)
        time.append(msg.time)

        i += 1
        msg = mid.tracks[1][i]
    
    return {"on_off": on_off, "note": note, "velocity": velocity, "time": time}

def get_meta():
    mid = MidiFile("./Audio/C1.mid")
    return mid.tracks[0]

def to_bass(input_filename, output_filename): ## Use the midi for drum as input to get desirable outcome
    s = converter.parse('./telegram_generated/' + input_filename + ".mid")
    for p in s.parts:
        p.insert(0, instrument.AcousticBass())
    s.write('midi', './telegram_generated/' + output_filename + '.mid')


def clean_bass(bass):
<<<<<<< HEAD
=======
    while bass + ".mid" not in os.listdir('./telegram_generated'):
        time.sleep(1)
>>>>>>> 07b4f5749149cae12295c6afb396fa12500c9ab1
    bass = MidiFile('./telegram_generated/' + bass + '.mid')
    new_bass = MidiFile()
    new_track = MidiTrack()
    new_bass.tracks.append(get_meta())
    new_bass.tracks.append(new_track)

    new_track.append(MidiFile("./Audio/C1.mid").tracks[2][0])
    for i in range(5, len(bass.tracks[0])-20):
        if hasattr(bass.tracks[0][i], "channel"):
            # if bass.tracks[0][i].type == 'note_on':
            bass.tracks[0][i].channel = 1
            bass.tracks[0][i].time = int(bass.tracks[0][i].time/2)
            new_track.append(bass.tracks[0][i])
    new_track.append(MidiFile("./Audio/C1.mid").tracks[2][-1])
    return new_bass

def clean_melody(melody):
<<<<<<< HEAD
=======
    while melody + ".mid" not in os.listdir('./telegram_generated'):
        time.sleep(1)
>>>>>>> 07b4f5749149cae12295c6afb396fa12500c9ab1
    melody = MidiFile('./telegram_generated/' + melody + '.mid')
    new_melody = MidiFile()
    new_track = MidiTrack()
    new_melody.tracks.append(get_meta())
    new_melody.tracks.append(new_track)

    new_track.append(MidiFile("./Audio/C1.mid").tracks[1][0])
    for i in melody.tracks[1]:
        if i.type == 'note_on':
            i.channel = 0
            i.time = int(i.time*2)
            new_track.append(i)
    new_track.append(MidiFile("./Audio/C1.mid").tracks[1][-1])
    return new_melody


def clean_drum(drum):
<<<<<<< HEAD
=======
    while drum + ".mid" not in os.listdir('./telegram_generated'):
        time.sleep(1)
>>>>>>> 07b4f5749149cae12295c6afb396fa12500c9ab1
    drum = MidiFile('./telegram_generated/' + drum + ".mid")
    new_drum = MidiFile()
    new_track = MidiTrack()
    new_drum.tracks.append(get_meta())
    new_drum.tracks.append(new_track)

    new_track.append(MidiFile("./Audio/C1.mid").tracks[3][0])
    for i in drum.tracks[2]:
        if i.type == 'note_on':
            i.channel = 9
            i.time = int(i.time*2)
            new_track.append(i)
    new_track.append(MidiFile("./Audio/C1.mid").tracks[3][-1])
    return new_drum

def get_trio(drum, melody, bass):
    trio = MidiFile()

    trio.tracks.append(get_meta())
    print(drum, melody, bass)
    print(os.listdir('./telegram_generated'))
    trio.tracks.append(clean_drum(drum).tracks[1])
    trio.tracks.append(clean_melody(melody).tracks[1])
    trio.tracks.append(clean_bass(bass).tracks[1])

    return trio


def print_midi(midi):
    for i, track in enumerate(midi.tracks):
        print("Track {}: {}".format(i, track.name))
        for msg in track:
            print(msg)


def save_midi(midi, output_filename):
<<<<<<< HEAD
    midi.save('./telegram_generated/' + output_filename + '.mid')

# for i, track in enumerate(MidiFile('composite0.mid').tracks):
    # print("Track {}: {}".format(i, track.name))
    # for msg in track:
    #     print(msg)
save_midi(get_trio('drum', 'piano', 'bass'), "combined")
=======
    midi.save('./telegram_generated/' + output_filename + '.mid')
>>>>>>> 07b4f5749149cae12295c6afb396fa12500c9ab1
