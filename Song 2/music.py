from pathlib import Path

from scamp import Session

from utilities.music_structs import Scales, N, C, R
from utilities.scamp_utils import PlayPart, MusicSeq


key = N("C5")
scale = Scales.NaturalScales.Major(key)

# PATTERN
drum_pattern = MusicSeq(*[
    (C("D2", "C2"), 1/4), (N("F#2"), 1/8),
    (N("F#2"), 1/8),

    (C("F#2", "C2"), 1/4), (N("F#2"), 1/4),

    (C("D2", "C2"), 1/8), (N("F#2"), 1/8),
    (N("F#2"), 1/8), (N("F#2"), 1/8),

    (C("D2", "C2"), 1/4), (N("D2"), 1/4),

    (C("D2", "C2"), 1/8), (N("F#2"), 1/8),
    (N("F#2"), 1/8), (N("D2"), 1/8),

    (C("F#2", "C2"), 1/8), (N("F#2"), 1/8),
    (N("D2"), 1/8), (N("F#2"), 1/8),

    (C("F#2", "C2"), 1/8), (N("D2"), 1/8),
    (N("F#2"), 1/8), (N("F#2"), 1/8),

    (C("D2", "C2"), 1/4), (C("D2", "C2"), 1/4)
])
harmony_pattern = MusicSeq(*[
    (C("A3", "C4", "E4"), 1/1),
    (C("G3", "B3", "D4"), 1/1),
    (C("G3", "C4", "E4"), 1/1),
    (C("F3", "A3", "C4"), 1/1),
])
bass_pattern = MusicSeq(*[
    (C("A1", "A2"), 1/1),
    (C("G1", "G2"), 1/1),
    (C("C1", "C2"), 1/1),
    (C("F1", "F2"), 1/1),
])
melody_pattern = MusicSeq(*[
    (N("C5"), 1/4), (N("D5"), 1/8),
    (N("E5"), 1/8), (N("E5"), 1/4),
])

# INTRO
drum_intro = MusicSeq(*[
    (R(), 4/1), *drum_pattern,
])
harmony_intro = MusicSeq(*[
    *harmony_pattern*2,
])
bass_intro = MusicSeq(*[
    (R(), 4/1), *bass_pattern,
])
melody_intro = MusicSeq(*[
    (R(), 8/1),
])

# SECTION 1
melody_sec1 = MusicSeq(*[
    *melody_pattern, (N("G5"), 1/4),
    (N("F5"), 3/8), (N("E5"), 1/8), (N("D5"), 1/4), (N("F5"), 1/4),
    (N("E5"), 3/8), (N("D5"), 1/8), (N("C5"), 1/4), (N("E5"), 1/4),
    (N("C5"), 1/1),
])

# SECTION 2
melody_sec2 = MusicSeq(*[
    *melody_pattern, (N("G5"), 1/4),
    (N("C6"), 3/8), (N("G5"), 1/8), (N("F5"), 1/4), (N("E5"), 1/4),
    (N("C5"), 3/8), (N("E5"), 3/8), (N("F5"), 3/8), (N("E5"), 3/8),
    (N("C5"), 1/4), (N("B4"), 1/4),
])

# ENDING
melody_end = MusicSeq(*[
    *melody_pattern, (N("D5"), 1/4),
    *melody_pattern, (N("D5"), 1/4),
    *melody_pattern, (N("D5"), 1/4),
    (C("C5", "E5"), 1/2)
])

# All Together
drum_line = MusicSeq(*[
    drum_intro,
    *drum_pattern*4,
])
harmony_line = MusicSeq(*[
    harmony_intro,
    *harmony_pattern*4,
])
bass_line = MusicSeq(*[
    bass_intro,
    *bass_pattern*4,
])
melody_line = MusicSeq(*[
    melody_intro,
    melody_sec1,
    melody_sec2,
    melody_sec1,
    melody_end
])


s = Session(tempo=38, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))
drum_inst = s.new_part("Electronic Kit")
harmony_inst = s.new_part("Grand Piano")
star_bass_inst = s.new_part("Star Theme")
pad_bass_inst = s.new_part("Warm Pad")
synth_bass_inst = s.new_part("Synth Bass 2")
melody_inst = s.new_part("Grand Piano")


def play():
    s.fork(PlayPart(drum_line, drum_inst, vol=0.5))
    s.fork(PlayPart(harmony_line, harmony_inst, vol=0.7))
    s.fork(PlayPart(bass_line, star_bass_inst, 0.7))
    s.fork(PlayPart(bass_line, pad_bass_inst, 0.8))
    s.fork(PlayPart(bass_line, synth_bass_inst, 0.7))
    s.fork(PlayPart(melody_line, melody_inst))

    s.wait_for_children_to_finish()


if __name__ == '__main__':
    play()