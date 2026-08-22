from pathlib import Path

from scamp import Session

from utilities.music_structs import Scales, N, C, R
from utilities.scamp_utils import PlayPart, MusicSeq, repeat

key = N("C5")
scale = Scales.NaturalScales.Minor(key) # [C3, D3, E3, F3, G3, A3, B3, C4]

# PATTERN
drum_pattern = MusicSeq(*[
    (N("D2"), 1/4), (N("F#2"), 1/8), (N("D2"), 1/4), (N("F#2"), 1/8),
    (N("D2"), 1/4), (N("F#2"), 1/8), (N("D2"), 1/4), (N("F#2"), 1/8),
    (N("D2"), 1/8), (N("F#2"), 1/16), (N("F#2"), 1/16), (N("D2"), 1/8), (N("D2"), 1/8),

    (N("D2"), 1/8), (N("F#2"), 1/8), (N("F#2"), 1/8), (N("D2"), 1/8),
    (N("F#2"), 1/8), (N("F#2"), 1/8), (N("D2"), 1/8), (N("F#2"), 1/8),
    (N("F#2"), 1/8), (N("D2"), 1/8), (N("F#2"), 1/8), (N("F#2"), 1/8),
    (N("D2"), 1/8), (N("D2"), 1/8), (N("D2"), 1/8), (N("D2"), 1/16), (N("D2"), 1/16),
])
bdrum_pattern = MusicSeq(*repeat(C("C2", "C2", "C2", "C2"), [3/8, 3/8, 3/8, 3/8, 1/4, 1/4])*2)
harmony_pattern = MusicSeq(*[
    *repeat(C("A3", "C4", "E4"), [1/4, 1/2, 1/8, 1/8]),
    *repeat(C("F3", "A3", "C4"), [1/4, 1/2, 1/8, 1/8]),
    *repeat(C("G3", "C4", "E4"), [1/4, 1/2, 1/8, 1/8]),
    *repeat(C("G3", "B3", "D4"), [1/4, 1/2, 1/8, 1/8]),
])
bass_pattern = MusicSeq(*[
    (C("A1", "A2"), 3/4), (C("E1", "E2"), 1/4),
    (C("F1", "F2"), 1/1),
    (C("C2", "C3"), 3/4), (C("G1", "G2"), 1/4),
    (C("D2", "D3"), 1/1),
])

# LINE
drum_line = MusicSeq(*[
    (R(), 4/1),
    drum_pattern*4,
    (N("D2"), 2/1),
])
bdrum_line = MusicSeq(*[
    (R(), 4/1),
    bdrum_pattern*4,
    (C("C2", "C2", "C2", "C2"), 2/1)
])
harmony_line = MusicSeq(*[
    harmony_pattern*5,
    (C("A3", "C4", "E4"), 2/1)
])
bass_line = MusicSeq(*[
    (R(), 4/1),
    bass_pattern*4,
    (C("C2", "C3"), 2/1),
])
melody_line = MusicSeq(*[
    (R(), 8/1),
    (N("E5"), 1/4), (N("E5"), 1/8), (N("C5"), 1/4), (N("C5"), 1/8), (N("C5"), 1/8), (N("D5"), 1/8),
    (N("F5"), 1/4), (N("F5"), 1/2), (N("C5"), 1/8), (N("D5"), 1/8),
    (N("E5"), 1/4), (N("E5"), 1/4), (N("F5"), 1/8), (N("E5"), 1/8), (N("F5"), 1/8), (N("E5"), 1/8),
    (N("D5"), 1/4), (N("D5"), 1/8), (N("D5"), 1/8), (N("C5"), 1/4), (N("B4"), 1/4),

    (N("A4"), 1/4), (N("A4"), 1/8), (N("B4"), 1/4), (N("B4"), 1/8), (N("C5"), 1/8), (N("D5"), 1/8),
    (N("E5"), 1/4), (N("E5"), 1/2), (N("C5"), 1/8), (N("C5"), 1/8),
    (N("C5"), 1/4), (N("C5"), 1/8), (N("G4"), 1/4), (N("G4"), 1/8), (N("D5"), 1/8), (N("C5"), 1/8),
    (N("C5"), 1/8), (N("B4"), 1/8), (N("B4"), 1/2), (N("G4"), 1/8), (N("G4"), 1/8),

    (N("A4"), 1/4), (N("A4"), 1/8), (N("E4"), 1/4), (N("E4"), 1/8), (N("E4"), 1/8), (N("F4"), 1/8),
    (N("A4"), 1/4), (N("A4"), 1/2), (N("A4"), 1/8), (N("A4"), 1/8),
    (N("C5"), 1/4), (N("C5"), 1/8), (N("G4"), 1/4), (N("G4"), 1/8), (N("D5"), 1/8), (N("C5"), 1/8),
    (N("C5"), 1/8), (N("B4"), 1/8), (N("B4"), 1/2), (N("G4"), 1/8), (N("B4"), 1/8),

    (N("C5"), 2/1)
])


s = Session(tempo=30, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))
drum_inst = s.new_part("Electronic Kit")
harmony_inst = s.new_part("Cello")
star_bass_inst = s.new_part("Star Theme")
pad_bass_inst = s.new_part("Warm Pad")
synth_bass_inst = s.new_part("Synth Bass 2")
melody_inst = s.new_part("Violin")


def play():
    s.fork(PlayPart(drum_line, drum_inst))
    s.fork(PlayPart(bdrum_line, drum_inst))
    s.fork(PlayPart(harmony_line, harmony_inst, vol=0.7))
    s.fork(PlayPart(bass_line, star_bass_inst))
    s.fork(PlayPart(bass_line, pad_bass_inst))
    s.fork(PlayPart(bass_line, synth_bass_inst))
    s.fork(PlayPart(melody_line, melody_inst, vol=0.8))

    s.wait_for_children_to_finish()


if __name__ == "__main__":
    play()