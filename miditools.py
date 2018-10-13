import os
from mido import MidiFile


def convert_mp3_to_midi(audio_name, bpm=60, smooth=0.15, minduration=0.15):
    cmd = "python2 audio_to_melodia.py ./Audio/" + audio_name + ".wav " + audio_name + ".mid "
    cmd += str(bpm) + " --smooth " + str(smooth) + " --minduration " + str(0.15)
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
