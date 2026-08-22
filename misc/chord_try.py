from pathlib import Path

from scamp import Session
from utilities.music_structs import Scales, N, C
from utilities.scamp_utils import PlayPart, MusicSeq

# START CHORD HERE
key = N("C3")
scale = Scales.NaturalScales.Major(key)

chords = MusicSeq(*[
    (chord, 1/1) for chord in [
        scale.chord(1),
        scale.chord(3),
        scale.chord(4),
        scale.chord(2),
    ]
])
# END CHORD HERE

s = Session(tempo=40, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))
inst = s.new_part("piano")

print(chords)

PlayPart(chords*2, inst)()