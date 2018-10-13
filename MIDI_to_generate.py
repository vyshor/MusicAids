import argparse
import tensorflow as tf
from absl import flags

def reset_flags():
    for name in list(flags.FLAGS):
        delattr(flags.FLAGS, name)

from melody_rnn import melody_rnn_generate
melody_rnn_generate = melody_rnn_generate.melody_rnn_generate()
reset_flags()
from improv_rnn import improv_rnn_generate
reset_flags()
# from drums_rnn import drums_rnn_generate
# from polyphony_rnn import polyphony_rnn_generate


def generate_audio(chord_dict, instrument='melody'):
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

