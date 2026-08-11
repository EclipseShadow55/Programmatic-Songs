import itertools as itt
from collections.abc import Iterable, Sequence
from functools import cache
from typing import Callable, Sized

import scamp
from scamp import wait
from scamp_extensions.pitch.utilities import note_name_to_number

from utilities.music_structs import Note, Chord


class PlayPart(Callable):
    total_id = itt.count(0)
    def __init__(self, line_to_play: list[tuple[Note | Chord | None, float | int]], instrument: scamp.ScampInstrument, vol: float|int = 1.0, shift: int = 0, debug: bool = False, given_id: str|None = None):
        if given_id is None:
            self.id = next(self.total_id)
        else:
            self.id = given_id

        self.line_to_play = line_to_play
        self.instrument = instrument

        self.vol = vol
        self.debug = debug
        self.shift = shift

        if debug:
            print(f"PlayPart(id={self.id}, {self.instrument}) initialized")

    def __call__(self):
        for pitch, duration in self.line_to_play:
            if isinstance(pitch, Chord):
                if self.debug:
                    print(f"PlayPart(id={self.id}, {self.instrument}) playing {pitch} for {duration}")
                self.instrument.play_chord(list(map(lambda x: note_name_to_number(str(x)) + self.shift, pitch.notes)), self.vol, duration)
            elif isinstance(pitch, Note):
                if self.debug:
                    print(f"PlayPart(id={self.id}, {self.instrument}) playing {pitch} for {duration}")
                self.instrument.play_note(note_name_to_number(str(pitch)) + self.shift, self.vol, duration)
            else:
                if self.debug:
                    print(f"PlayPart(id={self.id}, {self.instrument}) waiting for {duration}")
                wait(duration)

    def duration(self) -> float:
        total_length = 0
        for item, dur in self.line_to_play:
            total_length += dur
        return total_length

# TODO: Sequence class to hold strings of notes, index by time measures

