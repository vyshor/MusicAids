import os
from mido import MidiFile


def convert_mp3_to_midi(audio_name, bpm=60, smooth=0.15, minduration=0.15):
<<<<<<< HEAD
    cmd = "python27-32 audio_to_melodia.py ./Audio/" + audio_name + ".wav " + audio_name + ".mid "
=======
    cmd = "python27-32 audio_to_melodia.py ./Audio/" + audio_name + ".wav ./Audio/" + audio_name + ".mid "
>>>>>>> 5ba5039d7535d518ddf70d36553702db48f9c606
    cmd += str(bpm) + " --smooth " + str(smooth) + " --minduration " + str(0.15)
    print("Execturing " + cmd)
    os.system(cmd)

<<<<<<< HEAD
def convert_midi_to_mp3(audio_name):
    cmd = "timidity " + audio_name + ".mid -Ow -o " + audio_name + ".mp3"
    print("Execturing " + cmd)
=======

def convert_midi_to_mp3(full_path, file_name):
    cmd = "timidity " + full_path + " -Ow -o ./telegram_generated/" + file_name + ".mp3"
>>>>>>> 5ba5039d7535d518ddf70d36553702db48f9c606
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