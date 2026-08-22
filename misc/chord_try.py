from pathlib import Path

from scamp import Session
from utilities.music_structs import Scales, Chord, N, C
from utilities.scamp_utils import PlayPart, MusicSeq, repeat

# START CHORD HERE
key = N("F#3")
scale = Scales.NaturalScales.Major(key)

chords = MusicSeq(*[
    *repeat(C("B2", "F#3", "D#4"), [1/8]*8),
    *repeat(C("C#3", "G#3", "F4"), [1/8]*8),
    *repeat(C("D#3", "A#3", "F#4"), [1/8]*8),
    *repeat(C("F#3", "C#4", "A#4"), [1/8]*4),
    *repeat(C("C#3", "G#3", "F4"), [1/8]*3),
    (C("D#3", "A#3", "F#4"), 1/8),
])
# END CHORD HERE

# D# + F# + B
# F + G# + C#
# F# + A# + D#

s = Session(tempo=32, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))
inst = s.new_part("square lead")

print(chords)

PlayPart(chords, inst)()