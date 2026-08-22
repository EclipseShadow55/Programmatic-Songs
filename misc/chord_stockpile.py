from utilities.music_structs import Scales, N
from utilities.scamp_utils import MusicSeq


# HEARTFELT - Major - 1-5-6-4
key = N("C4")
scale = Scales.NaturalScales.Major(key)

chords = MusicSeq(*[
    (chord, 1/1) for chord in [
        scale.chord(1),
        scale.chord(5),
        scale.chord(6),
        scale.chord(4),
    ]
])


# REFLECTIVE - Minor - 6-7-1-7
key = N("A3")
scale = Scales.NaturalScales.Minor(key)

chords = MusicSeq(*[
    (chord, 1/1) for chord in [
        scale.chord(6),
        scale.chord(7),
        scale.chord(1) >> 1,
        scale.chord(7),
    ]
])

# SAD - Minor - 1-7-4-3
key = N("A3")
scale = Scales.NaturalScales.Minor(key)

chords = MusicSeq(*[
    (chord, 1/1) for chord in [
        scale.chord(1),
        scale.chord(7) << 1,
        scale.chord(4),
        scale.chord(3),
    ]
])

# EXPRESSIVE - Minor - 6-3-7-1
key = N("A3")
scale = Scales.NaturalScales.Minor(key)

chords = MusicSeq(*[
    (chord, 1/1) for chord in [
        scale.chord(6),
        scale.chord(3),
        scale.chord(7),
        scale.chord(1) >> 1,
    ]
])

# DARK - Minor - 1-6-4-5
key = N("A3")
scale = Scales.NaturalScales.Minor(key)

chords = MusicSeq(*[
    (chord, 1/1) for chord in [
        scale.chord(1) >> 1,
        scale.chord(6),
        scale.chord(4),
        scale.chord(5),
    ]
])

# ... - Major - 1-3-4-2
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