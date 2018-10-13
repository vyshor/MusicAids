import argparse
import tensorflow as tf
from absl import flags
import os
from os.path import isfile, join

def reset_flags():
    for name in list(flags.FLAGS):
        delattr(flags.FLAGS, name)


from melody_rnn import melody_rnn_generate
melody_rnn_generate = melody_rnn_generate.melody_rnn_generate
reset_flags()
from improv_rnn import improv_rnn_generate
improv_rnn_generate = improv_rnn_generate.improv_rnn_generate
reset_flags()
from drums_rnn import drums_rnn_generate
drums_rnn_generate = drums_rnn_generate.drums_rnn_generate
reset_flags()
# from polyphony_rnn import polyphony_rnn_generate
# reset_flags()


def generate_audio(chord_dict, instrument='melody'):
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

    if instrument == 'melody':
        melody_rnn_generate(primer=primer)
        reset_flags()

    # return next((join(path, f) for f in os.listdir(path) if isfile(join(path, f))), "")


