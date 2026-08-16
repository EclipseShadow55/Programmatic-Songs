from pathlib import Path

from scamp import Session

from utilities.music_structs import Scales, N, C
from utilities.scamp_utils import PlayPart, MusicSeq


key = N("A5")
scale = Scales.NaturalScales.Phrygian(key)

# PATTERN
harmony_pattern = MusicSeq(*[
    (C('A3', 'C4', 'E4'), 1/1),
    (C('A#3', 'D4', 'F4'), 1/1),
    (C('G3', 'A#3', 'D4'), 1/1),
    (C('A3', 'C4', 'E4'), 1/1),
])
bass_pattern = MusicSeq(*[
    (C("A1", "A2"), 1/1),
    (C("A#1", "A#2"), 1/1),
    (C("G1", "G2"), 1/1),
    (C("A1", "A2"), 1/1),
])
drum_pattern = MusicSeq(*[
    (C("D2", "C2", "C2", "C2", "C2"), 1/4), (C("F#2", "C2", "C2"), 1/4),
    (C("C2", "C2", "C2", "C2"), 1/8),
    (N("F#2"), 1/8), (N("D2"), 1/8), (N("F#2"), 1/8),
])

# SECTION 1
melody_sec1 = MusicSeq(*[
    (N("A4"), 1/4), (N("G4"), 1/8), (N("A4"), 1/8), (N("A#4"), 1/4),
    (N("C5"), 1/4),

    (N("D5"), 1/4), (N("C5"), 1/8), (N("A#4"), 1/8), (N("C5"), 1/4),
    (N("A4"), 1/4),

    (N("G4"), 1/4), (N("A4"), 1/8), (N("A#4"), 1/8), (N("A4"), 1/8),
    (N("G4"), 1/8), (N("F4"), 1/8), (N("E4"), 1/8),

    (N("A3"), 1/4), (N("C4"), 1/4), (N("E4"), 1/4), (N("A4"), 1/4),
])

# SECTION 2
melody_sec2 = MusicSeq(*[
    (N("A4"), 1/4), (N("A4"), 1/4), (N("A4"), 1/8), (N("A#4"), 1/8),
    (N("C5"), 1/8), (N("A4"), 1/8),

    (N("A#4"), 3/8), (N("A4"), 1/8), (N("G4"), 1/2),

    (N("E4"), 3/8), (N("F4"), 1/8), (N("A4"), 1/8), (N("E4"), 1/8),
    (N("E4"), 1/8), (N("G4"), 1/8),

    (N("F4"), 3/8), (N("E4"), 1/8), (N("D4"), 1/8), (N("E4"), 1/8),
    (N("F4"), 1/8), (N("G4"), 1/8),
])

# ENDING
harmony_end = MusicSeq(*[
    (C('A3', 'C4', 'E4'), 1/1),
])
bass_end = MusicSeq(*[
    (C("A1", "A2"), 1/1),
])
drum_end = MusicSeq(*[
    (C("D2", "C2", "C2", "C2", "C2"), 1/1)
])
melody_end = MusicSeq(*[
    (N("A4"), 1/1),
])

# LINE
harmony_line = MusicSeq(*[
    harmony_pattern*2,
    harmony_end,
])
bass_line = MusicSeq(*[
    bass_pattern*2,
    bass_end,
])
drum_line = MusicSeq(*[
    drum_pattern*8,
    drum_end,
])
melody_line = MusicSeq(*[
    melody_sec1,
    melody_sec2,
    melody_end,
])

s = Session(tempo=18, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))
harmony_inst = s.new_part("Cello")
star_bass_inst = s.new_part("Star Theme")
pad_bass_inst = s.new_part("Warm Pad")
synth_bass_inst = s.new_part("Synth Bass 2")
drum_inst = s.new_part("Electronic Kit")
melody_inst = s.new_part("Clarinet")


def play():
    s.fork(PlayPart(harmony_line, harmony_inst, vol=0.1))
    s.fork(PlayPart(bass_line, star_bass_inst, vol=0.2))
    s.fork(PlayPart(bass_line, pad_bass_inst, vol=0.2))
    s.fork(PlayPart(bass_line, synth_bass_inst, vol=0.2))
    s.fork(PlayPart(drum_line, drum_inst, vol=0.1))
    s.fork(PlayPart(melody_line, melody_inst, vol=0.3))

    s.wait_for_children_to_finish()


if __name__ == '__main__':
    play()