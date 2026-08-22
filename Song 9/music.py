from pathlib import Path

from scamp import Session

from utilities.music_structs import Scales, N, C, R
from utilities.scamp_utils import PlayPart, MusicSeq, repeat

key = N("D#3")
scale = Scales.NaturalScales.Minor(key)


# PATTERN
harmony_pattern = MusicSeq(*[
    *repeat(C("B2", "F#3", "D#4"), [1/8]*8),
    *repeat(C("C#3", "G#3", "F4"), [1/8]*8),
    *repeat(C("D#3", "A#3", "F#4"), [1/8]*8),
    *repeat(C("F#3", "C#4", "A#4"), [1/8]*4),
    *repeat(C("C#3", "G#3", "F4"), [1/8]*3),
    (C("D#3", "A#3", "F#4"), 1/8),
])
melody_pattern = MusicSeq(*[
    *repeat(C("B0", "B1", "B2"), [1/8]*8),
    *repeat(C("C#1", "C#2", "C#3"), [1/8]*8),
    *repeat(C("D#1", "D#2", "D#3"), [1/8]*8),
    *repeat(C("F#1", "F#2", "F#3"), [1/8]*4),
    *repeat(C("C#1", "C#2", "C#3"), [1/8]*3),
    (C("D#1", "D#2", "D#3"), 1/8),
])
smooth_bass_pattern = MusicSeq(*[
    (C("B0", "B1"), 1/1),
    (C("C#1", "C#2"), 1/1),
    (C("D#1", "D#2"), 1/1),
    (C("F#1", "F#2"), 1/2),
    (C("C#1", "C#2"), 1/2),
])
drum_pattern = MusicSeq(*[
    (C("C2", "C2", "C2"), 1/4), (C("C2", "C2", "C2"), 1/4),
    (N("D2"), 1/4), (C("C2", "C2", "C2"), 1/8), (N("D2"), 1/8),

    (C("C2", "C2", "C2"), 1 / 4), (C("C2", "C2", "C2"), 1 / 4),
    (N("D2"), 1 / 4), (C("C2", "C2", "C2"), 1 / 8), (N("D2"), 1 / 8),

    (C("C2", "C2", "C2"), 1 / 4), (C("C2", "C2", "C2"), 1 / 4),
    (N("D2"), 1 / 4), (C("C2", "C2", "C2"), 1 / 8), (N("D2"), 1 / 8),

    (C("C2", "C2", "C2"), 1/8), (N("D2"), 1/8), (N("D2"), 1/8),
    (C("C2", "C2", "C2"), 1/8), (N("D2"), 1/8), (N("D2"), 1/8),
    (C("C2", "C2", "C2"), 1/8), (N("D2"), 1/8),
])
cmelody_pattern = MusicSeq(*[
    *repeat(C("F#5", "F#6"), [1/8]*8),
    *repeat(C("F5", "F6"), [1/8]*7), (C("F#5", "F#6"), 1/8),
    *repeat(C("D#5", "D#6"), [1/8]*8),
    *repeat(C("C#5", "C#6"), [1/8]*4),
    *repeat(C("F5", "F6"), [1/8]*3), (C("F#5", "F#6"), 1/8),
])

# INTRO
harmony_intro = MusicSeq(*[
    *repeat(C("D#3", "A#3", "F#4"), [1/8]*4),
    *repeat(C("C#3", "G#3", "F4"), [1/8]*2),
    (C("C#3", "G#3", "F4"), 1/8), (C("D#3", "A#3", "F#4"), 1/8),
])

# LINE
harmony_line = MusicSeq(*[
    harmony_intro,
    harmony_pattern * 5,
])
melody_line = MusicSeq(*[
    (R(), harmony_intro.duration()),
    (R(), 8/1),
    melody_pattern * 3,
])
smooth_bass_line = MusicSeq(*[
    (R(), harmony_intro.duration()),
    (R(), 4/1),
    smooth_bass_pattern * 4,
])
drum_line = MusicSeq(*[
    (R(), harmony_intro.duration()),
    (R(), 4/1),
    drum_pattern * 4,
])
cmelody_line = MusicSeq(*[
    (R(), harmony_intro.duration()),
    (R(), 12/1),
    cmelody_pattern * 2,
]) << 1


s = Session(tempo=32, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))
harmony_inst = s.new_part("Square Lead")
melody_inst = s.new_part("Synth Bass 2")
star_bass_inst = s.new_part("Star Theme")
pad_bass_inst = s.new_part("Warm Pad")
drum_inst = s.new_part("Electronic Kit")
cmelody_inst = s.new_part("Doctor Solo")


def play():
    s.fork(PlayPart(harmony_line, harmony_inst))
    s.fork(PlayPart(melody_line, melody_inst))
    s.fork(PlayPart(smooth_bass_line, star_bass_inst))
    s.fork(PlayPart(smooth_bass_line, pad_bass_inst))
    s.fork(PlayPart(drum_line, drum_inst))
    s.fork(PlayPart(cmelody_line, cmelody_inst, vol=0.6))

    s.wait_for_children_to_finish()


if __name__ == "__main__":
    play()