import argparse
import tensorflow as tf
from absl import flags
import os
from os.path import isfile, join


def reset_flags():
    for name in list(flags.FLAGS):
        delattr(flags.FLAGS, name)


# Silly, but had to, because they have overlapping flags, so I have to reset and
# initialise the flags everytime before and after I use

from melody_rnn import melody_rnn_generate, melody_rnn_config_flags
melody_rnn_generate_func = melody_rnn_generate.melody_rnn_generate
reset_flags()
from improv_rnn import improv_rnn_generate, improv_rnn_config_flags
improv_rnn_generate_func = improv_rnn_generate.improv_rnn_generate
reset_flags()
from drums_rnn import drums_rnn_generate, drums_rnn_config_flags
drums_rnn_generate_func = drums_rnn_generate.drums_rnn_generate
reset_flags()
from polyphony_rnn import polyphony_rnn_generate
polyphony_rnn_generate_func = polyphony_rnn_generate.polyphony_rnn_generate
reset_flags()
# from music_vae import music_vae_generate
# music_vae_generate_func = music_vae_generate.polyphony_rnn_generate
# reset_flags()


def generate_audio(chord_dict, midi_path, instrument='simple_piano'):
    path = './telegram_generated'
    note_type = chord_dict['on_off']
    note = chord_dict['note']
    velocity = chord_dict['velocity']

    primer = []

    for idx, note_type in enumerate(note_type):
        if note_type == 'note_on':
            primer.append(note[idx])
            primer.append(velocity[idx])
        else:
            primer.append(note[idx])
            primer.append(-1)
    primer = str(primer)

    if instrument == 'simple_melody':
        print("Running melody_rnn")
        melody_rnn_config_flags.set_flags()
        melody_rnn_generate.set_flags()
        melody_rnn_generate_func(primer=primer)

    # elif instrument == 'improv':
    #     print("Running improv_rnn")
    #     improv_rnn_config_flags.set_flags()
    #     improv_rnn_generate.set_flags()
    #     improv_rnn_generate_func(primer=primer)

    elif instrument == 'simple_piano':
        print("Running polyphony_rnn")
        polyphony_rnn_generate.set_flags()
        polyphony_rnn_generate_func(primer=primer)

    elif instrument == 'simple_drum':
        print("Running drums_rnn")
        drums_rnn_config_flags.set_flags()
        drums_rnn_generate.set_flags()
        drums_rnn_generate_func(primer_midi=midi_path)

    elif instrument == 'combined_drum':
        print("Running music_vae (combined_drum)")
        print("But using drums_rnn to generate 2 simple drums first")

        drums_rnn_config_flags.set_flags()
        drums_rnn_generate.set_flags()
        drums_rnn_generate_func(primer_midi=midi_path, outputs=2)
        reset_flags()

        midi_list = [join(path, f) for f in os.listdir(path) if isfile(join(path, f))]
        midi1 = midi_list[0]
        midi2 = midi_list[-1]
        music_vae_generate.set_flags()
        music_vae_generate_func('cat-drums_2bar_small', midi1, midi2)
        os.remove(midi1)
        os.remove(midi2)

    elif instrument == 'combined_piano':
        print("Running music_vae (combined_melody)")
        print("But using chord_pitches_improv to generate 1 progression chord first, and 1 piano melody from polyphony_rnn")

        improv_rnn_config_flags.set_flags()
        improv_rnn_generate.set_flags()
        improv_rnn_generate_func(primer=primer)
        reset_flags()

        polyphony_rnn_generate.set_flags()
        polyphony_rnn_generate_func(primer=primer)
        reset_flags()

        midi_list = [join(path, f) for f in os.listdir(path) if isfile(join(path, f))]
        midi1 = midi_list[0]
        midi2 = midi_list[-1]
        music_vae_generate.set_flags()
        music_vae_generate_func('hierdec-mel_16bar', midi1, midi2)
        os.remove(midi1)
        os.remove(midi2)

    elif instrument == 'trios':
        print("Running music_vae (combined_trios)")
        print("But generating two melody, one convert to base, another leave as melody, generating one more from drums")
        print("After that, run the function to combine all into one midi")
        print("Repeat that again, and combine the two trios together")


        improv_rnn_config_flags.set_flags()
        improv_rnn_generate.set_flags()
        improv_rnn_generate_func(primer=primer)
        reset_flags()

        polyphony_rnn_generate.set_flags()
        polyphony_rnn_generate_func(primer=primer)
        reset_flags()

        midi_list = [join(path, f) for f in os.listdir(path) if isfile(join(path, f))]
        midi1 = midi_list[0]
        midi2 = midi_list[-1]
        music_vae_generate.set_flags()
        music_vae_generate_func('hierdec-mel_16bar', midi1, midi2)
        os.remove(midi1)
        os.remove(midi2)

    reset_flags()

    full_path = next((join(path, f) for f in os.listdir(path) if isfile(join(path, f))), "")
    print(full_path)
    print(full_path.split('/')[-1])
    filename = full_path.split('\\')[-1].split('.')[0]
    print(filename)
    return full_path, filename


