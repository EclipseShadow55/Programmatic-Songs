from typing import Callable

from scamp import Session, wait
from scamp_extensions.pitch.utilities import note_name_to_number


class PlayPart(Callable):
    def __init__(self, line_to_play, instrument, vol=1.0):
        self.line_to_play = line_to_play
        self.instrument = instrument
        self.vol = vol

    def __call__(self):
        for pitch, duration in self.line_to_play:
            if pitch is None:
                wait(duration)
            else:
                self.instrument.play_note(note_name_to_number(pitch)+6, self.vol, duration)


s = Session(tempo=20)

melody_ins = s.new_part("clarinet")
harmony_ins = s.new_part("cello")
bass_ins = s.new_part("contrabass")
high_ins = s.new_part("flute")

# START
melody_start = [
    ("E3", 1/4), ("D3", 1/8), ("C3", 1/8), ("A2", 1/2),
    ("G2", 1/4), ("E2", 1/8), ("G2", 1/8), ("A2", 1/2),
    ("E2", 1/8), ("G2", 1/8), ("A2", 1/8), ("C3", 1/8),
    ("D3", 1/8), ("E3", 1/8), ("C3", 1/8), ("A2", 1/8),
    ("D3", 1/2), ("C3", 1/8), ("A2", 1/8), ("E2", 1/8),
    ("G2", 1/8)
]
harmony_start = [
    (None, 1/1), ("C2", 1/4), ("B1", 1/8), ("C2", 1/8),
    ("E2", 1/2), ("C2", 1/8), ("D2", 1/8), ("E2", 1/8),
    ("G2", 1/8), ("A2", 1/8), ("B2", 1/8), ("G2", 1/8),
    ("E2", 1/8), ("B2", 1/2), ("G2", 1/8), ("E2", 1/8),
    ("C2", 1/8), ("D2", 1/8)
]
bass_start = [
    (None, 2/1), ("A1", 1/8), ("G1", 1/8), ("A1", 1/8),
    ("C2", 1/8), ("D2", 1/8), ("E2", 1/8), ("C2", 1/8),
    ("A1", 1/8), ("D2", 1/2), ("C2", 1/8), ("A1", 1/8),
    ("E1", 1/8), ("G1", 1/8)
]
high_start = [
    (None, 4/1)
]

# CLIFF
melody_cliff = [
    ("A2", 1/4), ("B2", 1/8), ("C3", 1/8), ("D3", 1/4),
    ("C3", 1/8), ("B2", 1/8), ("D3", 3/8), ("E3", 1/16),
    ("C3", 1/16), ("B2", 1/4), ("A2", 1/8), ("B2", 1/8)
]
harmony_cliff = [
    ("E2", 1/4), ("G2", 1/4), ("A2", 1/4), ("G2", 1/4),
    ("A2", 3/8), ("E2", 1/8), ("G2", 1/4), ("F2", 1/4)
]
bass_cliff = [
    ("A1", 1/4), ("B1", 1/8), ("D2", 1/8), ("E2", 1/4),
    ("D2", 1/8), ("C2", 1/8), ("D2", 3/8), ("E2", 3/8),
    ("D2", 1/4)
]
high_cliff = [
    ("E5", 1/8), ("F5", 1/8), ("G5", 1/8), ("A5", 1/8),
    ("C6", 1/4), ("B5", 1/4), ("A5", 1/1)
]

# MIDDLE
melody_mid = [
    ("C3", 1/8), ("D3", 1/8), ("B2", 1/8), ("C3", 1/8),
    ("A2", 1/8), ("B2", 1/8), ("G2", 1/8), ("A2", 1/8),
    ("E2", 1/2), ("E2", 1/8), ("G2", 1/8), ("A2", 1/4)
]
harmony_mid = [
    ("A2", 1/8), ("B2", 1/8), ("E3", 1/8), ("F3", 1/8),
    ("D3", 1/8), ("E3", 1/8), ("D3", 1/8), ("C3", 1/8),
    ("B2", 1/16), ("A2", 7/16), ("B2", 1/8), ("D3", 1/8),
    ("E3", 1/4)
]
bass_mid = [
    ("C2", 1/8), ("D2", 1/8), ("B1", 1/8), ("C2", 1/8),
    ("A1", 1/8), ("B1", 1/8), ("C2", 1/8), ("D2", 1/8),
    ("A1", 1/2), ("B1", 1/8), ("G1", 1/8), ("A1", 1/4)
]
high_mid = [
    (None, 1/1), ("E6", 1/2), ("E5", 1/8), ("G5", 1/8),
    ("A5", 1/4)
]

# END
melody_end = [
    ("C3", 1/4), ("B2", 1/4), ("C3", 1/4), ("D3", 1/4),
    ("F3", 1/4), ("A3", 1/2), ("E3", 1/4), ("A3", 1/4),
    ("B3", 1/8), ("C4", 1/8), ("D4", 1/4), ("C4", 1/8),
    ("B3", 1/8), ("A3", 1/2), (None, 1/4)
]
harmony_end = [
    (None, 1/2), ("A2", 1/4), ("G2", 1/4), ("A2", 1/4),
    ("C3", 1/4), ("B2", 1/4), ("G2", 1/2), ("B2", 1/4),
    ("E3", 1/4), ("D3", 1/4), ("E3", 1/2), (None, 1/4)
]
bass_end = [
    ("C2", 1/4), ("B1", 1/4), ("C2", 1/4), ("D2", 1/4),
    ("F2", 1/4), ("E2", 1/4), ("D2", 1/4), ("E2", 1/2),
    ("F2", 1/4), ("B2", 1/4), ("G2", 1/4), ("A2", 1/2),
    (None, 1/4)
]
high_end = [
    ("C6", 1/8), ("B5", 1/8), ("A5", 1/8), ("G5", 1/8),
    ("E5", 1/2), (None, 1/1), ("E5", 1/8), ("F5", 1/8),
    ("G5", 1/8), ("A5", 1/8), ("C6", 1/4), ("B5", 1/4),
    ("A5", 1/2), (None, 1/4)
]

# All Together
melody_line = melody_start + melody_cliff + melody_mid + melody_end
harmony_line = harmony_start + harmony_cliff + harmony_mid + harmony_end
bass_line = bass_start + bass_cliff + bass_mid + bass_end
high_line = high_start + high_cliff + high_mid + high_end


def music_play():
    s.fork(PlayPart(melody_line, melody_ins))
    s.fork(PlayPart(harmony_line, harmony_ins, 0.6))
    s.fork(PlayPart(bass_line, bass_ins, 0.6))
    s.fork(PlayPart(high_line, high_ins, 0.5))

    s.wait_for_children_to_finish()


if __name__ == "__main__":
    music_play()