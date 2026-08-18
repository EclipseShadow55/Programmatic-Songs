from pathlib import Path

from scamp import Session

from utilities.music_structs import Scales, N, C, R
from utilities.scamp_utils import PlayPart, MusicSeq, TempoManager, AutoSeq, AutoCurve, CurveType

key = N("D5")
scale = Scales.NaturalScales.Minor(key)

# PATTERN
harmony_pattern = MusicSeq(*[
    (C("D3", "F3", "A3"), 1/1),
    (C("E3", "A3", "C4"), 1/1),
    (C("G3", "C4", "E4"), 1/1),
    (C("G3", "A#3", "D4"), 1/1)
])
bass_pattern = MusicSeq(*[
    (C("D1", "D2"), 1/1),
    (C("A1", "A2"), 1/1),
    (C("C2", "C3"), 1/1),
    (C("G1", "G2"), 1/1)
])
bass_harm_pattern = MusicSeq(*[
    (C("A1", "A2"), 1/1),
    (C("E1", "E2"), 1/1),
    (C("G1", "G2"), 1/1),
    (C("D1", "D2"), 1/1),
])

# LINE
harmony_line = MusicSeq(*[
    (R(), 3/8),
    harmony_pattern,
    harmony_pattern,
    (R(), 1/1),
])
double_bass_line = MusicSeq(*[
    (R(), 3/8),
    (R(), 1/1),
    bass_pattern[1:],
    bass_pattern,
    (R(), 1/1),
])
star_bass_line = MusicSeq(*[
    (R(), 3/8),
    (R(), 2/1),
    bass_pattern[2:],
    bass_pattern,
    (R(), 1/1),
])
pad_bass_line = MusicSeq(*[
    (R(), 3/8),
    (R(), 3/1),
    bass_pattern[3:],
    bass_pattern,
    (R(), 1/1),
])
double_bass_harm_line = MusicSeq(*[
    (R(), 3/8),
    (R(), 4/1),
    bass_harm_pattern[4:],
    bass_harm_pattern,
    (R(), 1/1),
])
melody_line = MusicSeq(*[
    (N("F5"), 1/8), (N("A5"), 1/8), (N("C6"), 1/8),

    (N("D6"), 1/2), (N("C6"), 1/4), (N("D6"), 1/8), (N("A5"), 1/4),

    (N("G5"), 1/8), (N("F5"), 5/8), (N("F5"), 1/8), (N("C6"), 1/2),

    (N("G5"), 1/4), (N("A5"), 1/8), (N("A#5"), 3/4),

    (N("A#5"), 1/8), (N("A#5"), 1/8), (N("A5"), 1/8), (N("G5"), 1/2), (N("F5"), 1/4),

    (N("E5"), 1/8), (N("D5"), 3/4), (N("C5"), 1/8),

    (N("C5"), 1/8), (N("A4"), 1/8), (N("A#4"), 1/2), (N("D5"), 1/4),

    (N("C5"), 1/8), (N("D5"), 9/8),

    (R(), 1/1),
])
automation_line = AutoSeq(*[
    (R(), 3/8 + 3/1),
    AutoCurve(17, 2/1),
    AutoCurve(13, 1/1, CurveType.EASE_BOTH, strength=2)
])


s = Session(tempo=20, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))
harmony_inst = s.new_part("Cello")
double_bass_inst = s.new_part("Double Bass")
double_bass_harm_inst = s.new_part("Double Bass")
star_bass_inst = s.new_part("Star Theme")
pad_bass_inst = s.new_part("Warm Pad")
melody_inst = s.new_part("Flute", soundfont=str(Path(__file__).parent.parent / "FluteSusNV.sf2"))


def play():
    s.fork(PlayPart(harmony_line, harmony_inst, vol=0.6))
    s.fork(PlayPart(double_bass_line, double_bass_inst, vol=0.6))
    s.fork(PlayPart(star_bass_line, star_bass_inst, vol=0.6))
    s.fork(PlayPart(pad_bass_line, pad_bass_inst, vol=0.6))
    s.fork(PlayPart(double_bass_harm_line, double_bass_harm_inst, vol=0.6))
    s.fork(PlayPart(melody_line, melody_inst, vol=0.7))

    s.fork(TempoManager(s, automation_line))

    s.wait_for_children_to_finish()

if __name__ == "__main__":
    play()