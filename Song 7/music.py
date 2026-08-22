from pathlib import Path

from scamp import Session

from utilities.music_structs import Scales, N, C, R
from utilities.scamp_utils import PlayPart, MusicSeq


key = N("C5")
scale = Scales.NaturalScales.Major(key)


# PATTERN
rhythm_pattern = MusicSeq(*[
    (C("D1", "D2"), 3/16), (C("D1", "D2"), 3/16), (C("D1", "D2"), 1/4), (C("D1", "D2"), 1/8),
    (C("D1", "D2"), 1/4),

    (C("A1", "A2"), 3/16), (C("A1", "A2"), 3/16), (C("A1", "A2"), 1/4), (C("A1", "A2"), 1/8),
    (C("A1", "A2"), 1/4),

    (C("C2", "C3"), 3/16), (C("C2", "C3"), 3/16), (C("C2", "C3"), 1/4), (C("C2", "C3"), 1/8),
    (C("C2", "C3"), 1/4),

    (C("G1", "G2"), 3/16), (C("G1", "G2"), 3/16), (C("G1", "G2"), 1/4), (C("G1", "G2"), 1/8),
    (C("F1", "F2"), 1/8), (C("E1", "E2"), 1/8),
])
harmony_pattern = MusicSeq(*[
    (C("F3", "A3", "D4"), 1/1),
    (C("E3", "A3", "C4"), 1/1),
    (C("G3", "C4", "E4"), 1/1),
    (C("G3", "B3", "D4"), 1/1),
])
drum_pattern = MusicSeq(*[(C("C2", "C2", "C2", "C2"), 3/16), (C("C2", "C2"), 3/16), (C("C2"), 1/8)] * 8)
upper_rhythm_pattern = MusicSeq(*[
    (N("D3"), 3/16), (N("D3"), 3/16), (N("A2"), 1/4), (N("A2"), 1/8), (N("A2"), 1/4),
    (N("D3"), 3/16), (N("D3"), 3/16), (N("A2"), 1/4), (N("A2"), 1/8), (N("A2"), 1/4),
    (N("C3"), 3/16), (N("C3"), 3/16), (N("G2"), 1/4), (N("G2"), 1/8), (N("G2"), 1/4),
    (N("B2"), 3/16), (N("B2"), 3/16), (N("B2"), 1/8), (N("C3"), 1/8), (N("B2"), 1/8), (N("C3"), 1/8), (N("B2"), 1/8),
])

# INTRO
drum_intro = MusicSeq(*[(C("C2", "C2", "C2", "C2"), 3/16), (C("C2", "C2"), 3/16), (C("C2"), 5/8)] * 4)

# LINE
rhythm_line = MusicSeq(*[
    rhythm_pattern * 5,
])
harmony_line = MusicSeq(*[
    (R(), 8/1),
    harmony_pattern * 3,
])
drum_line = MusicSeq(*[
    (R(), 4/1),
    drum_intro,
    drum_pattern * 3,
])
upper_rhythm_line = MusicSeq(*[
    (R(), 12/1),
    upper_rhythm_pattern * 2,
])


s = Session(tempo=30, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))
rhythm_inst = s.new_part("Synth Bass 2")
harmony_inst = s.new_part("Synth Strings 3")
drum_inst = s.new_part("Electronic Kit")
upper_rhythm_inst = s.new_part("Synth Bass 1")


def play():
    s.fork(PlayPart(rhythm_line, rhythm_inst))
    s.fork(PlayPart(harmony_line, harmony_inst, vol=0.8))
    s.fork(PlayPart(drum_line, drum_inst))
    s.fork(PlayPart(upper_rhythm_line, upper_rhythm_inst))

    s.wait_for_children_to_finish()


if __name__ == "__main__":
    play()