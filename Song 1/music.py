from pathlib import Path

from scamp import Session

from utilities.music_structs import Scales, N, R
from utilities.scamp_utils import PlayPart, MusicSeq


composing_key = N("A5")
actual_key = N("D#6")
current_scale = Scales.NaturalScales.Minor(actual_key)


# START
melody_start = MusicSeq(*[
    (N("E3"), 1/4), (N("D3"), 1/8), (N("C3"), 1/8), (N("A2"), 1/2),
    (N("G2"), 1/4), (N("E2"), 1/8), (N("G2"), 1/8), (N("A2"), 1/2),
    (N("E2"), 1/8), (N("G2"), 1/8), (N("A2"), 1/8), (N("C3"), 1/8),
    (N("D3"), 1/8), (N("E3"), 1/8), (N("C3"), 1/8), (N("A2"), 1/8),
    (N("D3"), 1/2), (N("C3"), 1/8), (N("A2"), 1/8), (N("E2"), 1/8),
    (N("G2"), 1/8)
])
harmony_start = MusicSeq(*[
    (R(), 1/1), (N("C2"), 1/4), (N("B1"), 1/8), (N("C2"), 1/8),
    (N("E2"), 1/2), (N("C2"), 1/8), (N("D2"), 1/8), (N("E2"), 1/8),
    (N("G2"), 1/8), (N("A2"), 1/8), (N("B2"), 1/8), (N("G2"), 1/8),
    (N("E2"), 1/8), (N("B2"), 1/2), (N("G2"), 1/8), (N("E2"), 1/8),
    (N("C2"), 1/8), (N("D2"), 1/8)
])
bass_start = MusicSeq(*[
    (R(), 2/1), (N("A1"), 1/8), (N("G1"), 1/8), (N("A1"), 1/8),
    (N("C2"), 1/8), (N("D2"), 1/8), (N("E2"), 1/8), (N("C2"), 1/8),
    (N("A1"), 1/8), (N("D2"), 1/2), (N("C2"), 1/8), (N("A1"), 1/8),
    (N("E1"), 1/8), (N("G1"), 1/8)
])
high_start = MusicSeq(*[
    (R(), 4/1)
])

# CLIFF
melody_cliff = MusicSeq(*[
    (N("A2"), 1/4), (N("B2"), 1/8), (N("C3"), 1/8), (N("D3"), 1/4),
    (N("C3"), 1/8), (N("B2"), 1/8), (N("D3"), 3/8), (N("E3"), 1/16),
    (N("C3"), 1/16), (N("B2"), 1/4), (N("A2"), 1/8), (N("B2"), 1/8)
])
harmony_cliff = MusicSeq(*[
    (N("E2"), 1/4), (N("G2"), 1/4), (N("A2"), 1/4), (N("G2"), 1/4),
    (N("A2"), 3/8), (N("E2"), 1/8), (N("G2"), 1/4), (N("F2"), 1/4)
])
bass_cliff = MusicSeq(*[
    (N("A1"), 1/4), (N("B1"), 1/8), (N("D2"), 1/8), (N("E2"), 1/4),
    (N("D2"), 1/8), (N("C2"), 1/8), (N("D2"), 3/8), (N("E2"), 3/8),
    (N("D2"), 1/4)
])
high_cliff = MusicSeq(*[
    (N("E5"), 1/8), (N("F5"), 1/8), (N("G5"), 1/8), (N("A5"), 1/8),
    (N("C6"), 1/4), (N("B5"), 1/4), (N("A5"), 1/1)
])

# MIDDLE
melody_mid = MusicSeq(*[
    (N("C3"), 1/8), (N("D3"), 1/8), (N("B2"), 1/8), (N("C3"), 1/8),
    (N("A2"), 1/8), (N("B2"), 1/8), (N("G2"), 1/8), (N("A2"), 1/8),
    (N("E2"), 1/2), (N("E2"), 1/8), (N("G2"), 1/8), (N("A2"), 1/4)
])
harmony_mid = MusicSeq(*[
    (N("A2"), 1/8), (N("B2"), 1/8), (N("E3"), 1/8), (N("F3"), 1/8),
    (N("D3"), 1/8), (N("E3"), 1/8), (N("D3"), 1/8), (N("C3"), 1/8),
    (N("B2"), 1/16), (N("A2"), 7/16), (N("B2"), 1/8), (N("D3"), 1/8),
    (N("E3"), 1/4)
])
bass_mid = MusicSeq(*[
    (N("C2"), 1/8), (N("D2"), 1/8), (N("B1"), 1/8), (N("C2"), 1/8),
    (N("A1"), 1/8), (N("B1"), 1/8), (N("C2"), 1/8), (N("D2"), 1/8),
    (N("A1"), 1/2), (N("B1"), 1/8), (N("G1"), 1/8), (N("A1"), 1/4)
])
high_mid = MusicSeq(*[
    (R(), 1/1), (N("E6"), 1/2), (N("E5"), 1/8), (N("G5"), 1/8),
    (N("A5"), 1/4)
])

# END
melody_end = MusicSeq(*[
    (N("C3"), 1/4), (N("B2"), 1/4), (N("C3"), 1/4), (N("D3"), 1/4),
    (N("F3"), 1/4), (N("A3"), 1/2), (N("E3"), 1/4), (N("A3"), 1/4),
    (N("B3"), 1/8), (N("C4"), 1/8), (N("D4"), 1/4), (N("C4"), 1/8),
    (N("B3"), 1/8), (N("A3"), 1/2), (R(), 1/4)
])
harmony_end = MusicSeq(*[
    (R(), 1/2), (N("A2"), 1/4), (N("G2"), 1/4), (N("A2"), 1/4),
    (N("C3"), 1/4), (N("B2"), 1/4), (N("G2"), 1/2), (N("B2"), 1/4),
    (N("E3"), 1/4), (N("D3"), 1/4), (N("E3"), 1/2), (R(), 1/4)
])
bass_end = MusicSeq(*[
    (N("C2"), 1/4), (N("B1"), 1/4), (N("C2"), 1/4), (N("D2"), 1/4),
    (N("F2"), 1/4), (N("E2"), 1/4), (N("D2"), 1/4), (N("E2"), 1/2),
    (N("F2"), 1/4), (N("B2"), 1/4), (N("G2"), 1/4), (N("A2"), 1/2),
    (R(), 1/4)
])
high_end = MusicSeq(*[
    (N("C6"), 1/8), (N("B5"), 1/8), (N("A5"), 1/8), (N("G5"), 1/8),
    (N("E5"), 1/2), (R(), 1/1), (N("E5"), 1/8), (N("F5"), 1/8),
    (N("G5"), 1/8), (N("A5"), 1/8), (N("C6"), 1/4), (N("B5"), 1/4),
    (N("A5"), 1/2), (R(), 1/4)
])

# All Together
melody_line = MusicSeq(*[
    melody_start,
    melody_cliff,
    melody_mid,
    melody_end
])
harmony_line = MusicSeq(*[
    harmony_start,
    harmony_cliff,
    harmony_mid,
    harmony_end
])
bass_line = MusicSeq(*[
    bass_start,
    bass_cliff,
    bass_mid,
    bass_end
])
high_line = MusicSeq(*[
    high_start,
    high_cliff,
    high_mid,
    high_end
])


s = Session(tempo=20, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))
melody_inst = s.new_part("Violin")
harmony_inst = s.new_part("Cello")
bass_inst = s.new_part("Double Bass")
high_inst = s.new_part("Flute")


def music_play():
    s.fork(PlayPart(melody_line, melody_inst, shift=6, debug=True))
    s.fork(PlayPart(harmony_line, harmony_inst, shift=6))
    s.fork(PlayPart(bass_line, bass_inst, shift=6))
    s.fork(PlayPart(high_line, high_inst, vol=0.4, shift=6))

    s.wait_for_children_to_finish()


if __name__ == "__main__":
    music_play()