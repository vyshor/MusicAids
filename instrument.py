from music21 import converter, instrument

s = converter.parse('./old.mid')

for p in s.parts:
    p.insert(0, instrument.ElectricBass())

s.write('midi', './new.mid')
