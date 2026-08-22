from pathlib import Path

from scamp import Session

from utilities.music_structs import Scales, N, C, R
from utilities.scamp_utils import PlayPart, MusicSeq, repeat

key = N("C5")
scale = Scales.NaturalScales.Major(key)

# PATTERN
harmony_pattern = MusicSeq(*[
    (C("C3", "E3", "G3"), 1/1),
    (C("E3", "G3", "B3"), 1/1),
    (C("F3", "A3", "C4"), 1/1),
    (C("D3", "F3", "A3"), 1/1),
])
drum_pattern = MusicSeq(*[
    (N("D2"), 1/8), (N("F#2"), 1/16), (R(), 1/16), (N("D2"), 1/8), (N("F#2"), 1/16), (N("F#2"), 1/16),
    (N("D2"), 1/8), (N("F#2"), 1/16), (R(), 1/16), (N("D2"), 1/8), (N("D2"), 1/8),

    (N("D2"), 1/8), (N("F#2"), 1/16), (R(), 1/16), (N("D2"), 1/8), (N("F#2"), 1/16), (N("F#2"), 1/16),
    (N("D2"), 1/8), (N("F#2"), 1/16), (R(), 1/16), (N("D2"), 1/8), (N("D2"), 1/8),

    (N("D2"), 1/8), (N("F#2"), 1/16), (R(), 1/16), (N("D2"), 1/8), (N("F#2"), 1/16), (N("F#2"), 1/16),
    (N("D2"), 1/8), (N("F#2"), 1/16), (R(), 1/16), (N("D2"), 1/8), (N("D2"), 1/8),

    (N("D2"), 1/16), (N("F#2"), 1/16), (N("F#2"), 1/16), (N("D2"), 1/16), (N("F#2"), 1/16), (N("F#2"), 1/16),
    (N("D2"), 1/16), (N("F#2"), 1/16), (N("F#2"), 1/16), (N("D2"), 1/16), (N("F#2"), 1/16), (N("F#2"), 1/16),
    (N("D2"), 1/8), (N("D2"), 1/8),
])
bass_rhythm_pattern = MusicSeq(*[
    *repeat(C("C1", "C2"), [3/16, 3/16, 4/16, 2/16, 4/16]),
    *repeat(C("E1", "E2"), [3/16, 3/16, 4/16, 2/16, 4/16]),
    *repeat(C("F1", "F2"), [3/16, 3/16, 4/16, 2/16, 4/16]),
    *repeat(C("D1", "D2"), [3/16, 3/16, 4/16, 2/16, 4/16]),
])
bass_pattern = MusicSeq(*[
    (C("C1", "C2"), 1/1),
    (C("E1", "E2"), 1/1),
    (C("F1", "F2"), 1/1),
    (C("D1", "D2"), 1/1),
])

# LINE
harmony_line = MusicSeq(*[
    harmony_pattern * 4,
    (C("C3", "E3", "G3"), 1/1),
])
drum_line = MusicSeq(*[
    (R(), 4/1),
    drum_pattern * 3,
    (N("D2"), 1/1),
])
bass_rhythm_line = MusicSeq(*[
    (R(), 4/1),
    bass_rhythm_pattern * 3,
    (C("C1", "C2"), 1/1),
])
bass_line = MusicSeq(*[
    (R(), 4/1),
    bass_pattern * 3,
    (C("C1", "C2"), 1/1),
])
melody_line = MusicSeq(*[
    (R(), 8/1),
    (C("C4","C4", "C5"), 3/16), (C("C4", "C4", "C5"), 3/16),
    (C("C4", "C4", "C5"), 2/16), (C("E4", "E5"), 4/16),
    (C("C4", "C4", "C5"), 4/16),
    
    (C("E4", "E4", "E5"), 3/16), (C("E4", "E4", "E5"), 3/16),
    (C("E4", "E4", "E5"), 2/16), (C("G4", "G4", "G5"), 4/16),
    (C("E4", "E4", "E5"), 4/16),
    
    (C("F4", "F4", "F5"), 3/16), (C("F4", "F4", "F5"), 3/16),
    (C("F4", "F4", "F5"), 2/16), (C("F4", "F4", "F5"), 3/16),
    (C("F4", "F4", "F5"), 3/16), (C("F4", "F4", "F5"), 2/16),
    
    (C("D4", "D4", "D5"), 3/16), (C("D4", "D4", "D5"), 3/16),
    (C("D4", "D4", "D5"), 2/16), (C("F4", "F4", "F5"), 3/16),
    (C("F4", "F4", "F5"), 3/16), (C("E4", "E4", "E5"), 2/16),
    
    (C("C4","C4", "C5"), 3/16), (C("C4", "C4", "C5"), 3/16),
    (C("C4", "C4", "C5"), 2/16), (C("E4", "E5"), 4/16),
    (C("C4", "C4", "C5"), 4/16),
    
    (C("E4", "E4", "E5"), 3/16), (C("E4", "E4", "E5"), 3/16),
    (C("E4", "E4", "E5"), 2/16), (C("G4", "G4", "G5"), 4/16),
    (C("E4", "E4", "E5"), 4/16),
    
    (C("F4", "F4", "F5"), 3/16), (C("F4", "F4", "F5"), 3/16),
    (C("E4", "E4", "E5"), 2/16), (C("D4", "D4", "D5"), 3/16),
    (C("E4", "E4", "E5"), 3/16), (C("F4", "F4", "F5"), 2/16),

    (C("E4", "E4", "E5"), 3/16), (C("D4", "D4", "D5"), 3/16),
    (C("C4", "C4", "C5"), 2/16), (C("B3", "B3", "B4"), 3/16),
    (C("A3", "A3", "A4"), 3/16), (C("B3", "B3", "B4"), 2/16),
    
    (C("C4", "C4", "C5"), 1/1),
])


s = Session(tempo=25, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))
harmony_inst = s.new_part("Synth Strings 3")
drum_inst = s.new_part("Electronic Kit")
bass_rhythm_inst = s.new_part("Synth Bass 2")
star_bass_inst = s.new_part("Star Theme")
pad_bass_inst = s.new_part("Warm Pad")
melody_inst = s.new_part("Grand Piano")


def play():
    s.fork(PlayPart(harmony_line, harmony_inst))
    s.fork(PlayPart(drum_line, drum_inst, vol=0.8))
    s.fork(PlayPart(bass_rhythm_line, bass_rhythm_inst))
    s.fork(PlayPart(bass_line, star_bass_inst))
    s.fork(PlayPart(bass_line, pad_bass_inst))
    s.fork(PlayPart(melody_line, melody_inst))

    s.wait_for_children_to_finish()


if __name__ == "__main__":
    play()