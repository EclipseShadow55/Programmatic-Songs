from pathlib import Path

from scamp import Session

from utilities.music_structs import Note
from utilities.scamp_utils import PlayPart


s = Session(tempo=20, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))

melody_ins = s.new_part("Violin")
harmony_ins = s.new_part("Cello")
bass_ins = s.new_part("Double Bass")
high_ins = s.new_part("Flute")

# START
melody_start = [
    (Note.from_name("E3"), 1/4), (Note.from_name("D3"), 1/8), (Note.from_name("C3"), 1/8), (Note.from_name("A2"), 1/2),
    (Note.from_name("G2"), 1/4), (Note.from_name("E2"), 1/8), (Note.from_name("G2"), 1/8), (Note.from_name("A2"), 1/2),
    (Note.from_name("E2"), 1/8), (Note.from_name("G2"), 1/8), (Note.from_name("A2"), 1/8), (Note.from_name("C3"), 1/8),
    (Note.from_name("D3"), 1/8), (Note.from_name("E3"), 1/8), (Note.from_name("C3"), 1/8), (Note.from_name("A2"), 1/8),
    (Note.from_name("D3"), 1/2), (Note.from_name("C3"), 1/8), (Note.from_name("A2"), 1/8), (Note.from_name("E2"), 1/8),
    (Note.from_name("G2"), 1/8)
]
harmony_start = [
    (None, 1/1), (Note.from_name("C2"), 1/4), (Note.from_name("B1"), 1/8), (Note.from_name("C2"), 1/8),
    (Note.from_name("E2"), 1/2), (Note.from_name("C2"), 1/8), (Note.from_name("D2"), 1/8), (Note.from_name("E2"), 1/8),
    (Note.from_name("G2"), 1/8), (Note.from_name("A2"), 1/8), (Note.from_name("B2"), 1/8), (Note.from_name("G2"), 1/8),
    (Note.from_name("E2"), 1/8), (Note.from_name("B2"), 1/2), (Note.from_name("G2"), 1/8), (Note.from_name("E2"), 1/8),
    (Note.from_name("C2"), 1/8), (Note.from_name("D2"), 1/8)
]
bass_start = [
    (None, 2/1), (Note.from_name("A1"), 1/8), (Note.from_name("G1"), 1/8), (Note.from_name("A1"), 1/8),
    (Note.from_name("C2"), 1/8), (Note.from_name("D2"), 1/8), (Note.from_name("E2"), 1/8), (Note.from_name("C2"), 1/8),
    (Note.from_name("A1"), 1/8), (Note.from_name("D2"), 1/2), (Note.from_name("C2"), 1/8), (Note.from_name("A1"), 1/8),
    (Note.from_name("E1"), 1/8), (Note.from_name("G1"), 1/8)
]
high_start = [
    (None, 4/1)
]

# CLIFF
melody_cliff = [
    (Note.from_name("A2"), 1/4), (Note.from_name("B2"), 1/8), (Note.from_name("C3"), 1/8), (Note.from_name("D3"), 1/4),
    (Note.from_name("C3"), 1/8), (Note.from_name("B2"), 1/8), (Note.from_name("D3"), 3/8), (Note.from_name("E3"), 1/16),
    (Note.from_name("C3"), 1/16), (Note.from_name("B2"), 1/4), (Note.from_name("A2"), 1/8), (Note.from_name("B2"), 1/8)
]
harmony_cliff = [
    (Note.from_name("E2"), 1/4), (Note.from_name("G2"), 1/4), (Note.from_name("A2"), 1/4), (Note.from_name("G2"), 1/4),
    (Note.from_name("A2"), 3/8), (Note.from_name("E2"), 1/8), (Note.from_name("G2"), 1/4), (Note.from_name("F2"), 1/4)
]
bass_cliff = [
    (Note.from_name("A1"), 1/4), (Note.from_name("B1"), 1/8), (Note.from_name("D2"), 1/8), (Note.from_name("E2"), 1/4),
    (Note.from_name("D2"), 1/8), (Note.from_name("C2"), 1/8), (Note.from_name("D2"), 3/8), (Note.from_name("E2"), 3/8),
    (Note.from_name("D2"), 1/4)
]
high_cliff = [
    (Note.from_name("E5"), 1/8), (Note.from_name("F5"), 1/8), (Note.from_name("G5"), 1/8), (Note.from_name("A5"), 1/8),
    (Note.from_name("C6"), 1/4), (Note.from_name("B5"), 1/4), (Note.from_name("A5"), 1/1)
]

# MIDDLE
melody_mid = [
    (Note.from_name("C3"), 1/8), (Note.from_name("D3"), 1/8), (Note.from_name("B2"), 1/8), (Note.from_name("C3"), 1/8),
    (Note.from_name("A2"), 1/8), (Note.from_name("B2"), 1/8), (Note.from_name("G2"), 1/8), (Note.from_name("A2"), 1/8),
    (Note.from_name("E2"), 1/2), (Note.from_name("E2"), 1/8), (Note.from_name("G2"), 1/8), (Note.from_name("A2"), 1/4)
]
harmony_mid = [
    (Note.from_name("A2"), 1/8), (Note.from_name("B2"), 1/8), (Note.from_name("E3"), 1/8), (Note.from_name("F3"), 1/8),
    (Note.from_name("D3"), 1/8), (Note.from_name("E3"), 1/8), (Note.from_name("D3"), 1/8), (Note.from_name("C3"), 1/8),
    (Note.from_name("B2"), 1/16), (Note.from_name("A2"), 7/16), (Note.from_name("B2"), 1/8), (Note.from_name("D3"), 1/8),
    (Note.from_name("E3"), 1/4)
]
bass_mid = [
    (Note.from_name("C2"), 1/8), (Note.from_name("D2"), 1/8), (Note.from_name("B1"), 1/8), (Note.from_name("C2"), 1/8),
    (Note.from_name("A1"), 1/8), (Note.from_name("B1"), 1/8), (Note.from_name("C2"), 1/8), (Note.from_name("D2"), 1/8),
    (Note.from_name("A1"), 1/2), (Note.from_name("B1"), 1/8), (Note.from_name("G1"), 1/8), (Note.from_name("A1"), 1/4)
]
high_mid = [
    (None, 1/1), (Note.from_name("E6"), 1/2), (Note.from_name("E5"), 1/8), (Note.from_name("G5"), 1/8),
    (Note.from_name("A5"), 1/4)
]

# END
melody_end = [
    (Note.from_name("C3"), 1/4), (Note.from_name("B2"), 1/4), (Note.from_name("C3"), 1/4), (Note.from_name("D3"), 1/4),
    (Note.from_name("F3"), 1/4), (Note.from_name("A3"), 1/2), (Note.from_name("E3"), 1/4), (Note.from_name("A3"), 1/4),
    (Note.from_name("B3"), 1/8), (Note.from_name("C4"), 1/8), (Note.from_name("D4"), 1/4), (Note.from_name("C4"), 1/8),
    (Note.from_name("B3"), 1/8), (Note.from_name("A3"), 1/2), (None, 1/4)
]
harmony_end = [
    (None, 1/2), (Note.from_name("A2"), 1/4), (Note.from_name("G2"), 1/4), (Note.from_name("A2"), 1/4),
    (Note.from_name("C3"), 1/4), (Note.from_name("B2"), 1/4), (Note.from_name("G2"), 1/2), (Note.from_name("B2"), 1/4),
    (Note.from_name("E3"), 1/4), (Note.from_name("D3"), 1/4), (Note.from_name("E3"), 1/2), (None, 1/4)
]
bass_end = [
    (Note.from_name("C2"), 1/4), (Note.from_name("B1"), 1/4), (Note.from_name("C2"), 1/4), (Note.from_name("D2"), 1/4),
    (Note.from_name("F2"), 1/4), (Note.from_name("E2"), 1/4), (Note.from_name("D2"), 1/4), (Note.from_name("E2"), 1/2),
    (Note.from_name("F2"), 1/4), (Note.from_name("B2"), 1/4), (Note.from_name("G2"), 1/4), (Note.from_name("A2"), 1/2),
    (None, 1/4)
]
high_end = [
    (Note.from_name("C6"), 1/8), (Note.from_name("B5"), 1/8), (Note.from_name("A5"), 1/8), (Note.from_name("G5"), 1/8),
    (Note.from_name("E5"), 1/2), (None, 1/1), (Note.from_name("E5"), 1/8), (Note.from_name("F5"), 1/8),
    (Note.from_name("G5"), 1/8), (Note.from_name("A5"), 1/8), (Note.from_name("C6"), 1/4), (Note.from_name("B5"), 1/4),
    (Note.from_name("A5"), 1/2), (None, 1/4)
]


# All Together
melody_line = melody_start + melody_cliff + melody_mid + melody_end
harmony_line = harmony_start + harmony_cliff + harmony_mid + harmony_end
bass_line = bass_start + bass_cliff + bass_mid + bass_end
high_line = high_start + high_cliff + high_mid + high_end


def music_play():
    s.fork(PlayPart(melody_line, melody_ins, shift=6))
    s.fork(PlayPart(harmony_line, harmony_ins, shift=6))
    s.fork(PlayPart(bass_line, bass_ins, shift=6))
    s.fork(PlayPart(high_line, high_ins, vol=0.4, shift=6))

    s.wait_for_children_to_finish()


if __name__ == "__main__":
    music_play()