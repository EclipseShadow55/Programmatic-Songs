from utilities.music_structs import Scales, N
from utilities.scamp_utils import MusicSeq


# HEARTFELT - Major - 1-5-6-4
key = N("C4")
scale = Scales.NaturalScales.Major(key)

chords = MusicSeq(*[
    (scale.chord(1), 1/1),
    (scale.chord(5), 1/1),
    (scale.chord(6), 1/1),
    (scale.chord(4), 1/1),
])


# REFLECTIVE - Minor - 6-7-1-7
key = N("A3")
scale = Scales.NaturalScales.Minor(key)

chords = MusicSeq(*[
    (scale.chord(6), 1/1),
    (scale.chord(7), 1/1),
    (scale.chord(1) >> 1, 1/1),
    (scale.chord(7), 1/1),
])

# SAD - Minor - 1-7-4-3
key = N("A3")
scale = Scales.NaturalScales.Minor(key)

chords = MusicSeq(*[
    (scale.chord(1), 1/1),
    (scale.chord(7) << 1, 1/1),
    (scale.chord(4), 1/1),
    (scale.chord(3), 1/1),
])

# EXPRESSIVE - Minor - 6-3-7-1
key = N("A3")
scale = Scales.NaturalScales.Minor(key)

chords = MusicSeq(*[
    (scale.chord(6), 1/1),
    (scale.chord(3), 1/1),
    (scale.chord(7), 1/1),
    (scale.chord(1) >> 1, 1/1),
])

# DARK - Minor - 1-6-4-5
key = N("A3")
scale = Scales.NaturalScales.Minor(key)

chords = MusicSeq(*[
    (scale.chord(1) >> 1, 1/1),
    (scale.chord(6), 1/1),
    (scale.chord(4), 1/1),
    (scale.chord(5), 1/1),
])