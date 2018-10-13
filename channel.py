from music21 import converter, corpus, instrument, midi, note, chord, pitch


def open_midi(midi_path, remove_drums):
    # There is an one-line method to read MIDIs
    # but to remove the drums we need to manipulate some
    # low level MIDI events.
    mf = midi.MidiFile()
    mf.open(midi_path)
    mf.read()
    mf.close()
    if (remove_drums):
        for i in range(len(mf.tracks)):
            mf.tracks[i].events = [ev for ev in mf.tracks[i].events if ev.channel != 10]

    return midi.translate.midiFileToStream(mf)


mf1 = music21.midi.MidiFile()
mf1.open(filename='./test1.mid', attrib="rb")
mf1.read()
mf1.close()

mf2 = music21.midi.MidiFile()
mf2.open(filename='./test2.mid', attrib="rb")
mf2.read()
mf2.close()

# mf.readstr(midistr)

for track in mf.tracks:
    chnl = track.getChannels()
    if chnl[-1] != None:
        track.setChannel(chnl[1] + 1)
    print(track.getChannels())

midistr = mf.writestr()
mf.open(filename='./test.mid', attrib="wb")
mf.readstr(midistr)
mf.write()
mf.close()

# s = converter.parse('./old.mid')

# for p in s.parts:
#    p.insert(0, instrument.Woodblock())
#
# s.write('midi', './new.mid')
