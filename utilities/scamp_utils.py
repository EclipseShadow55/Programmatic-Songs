from __future__ import annotations
import itertools as itt
from collections.abc import Iterable
from typing import Callable

import scamp
from scamp import wait
from scamp_extensions.pitch.utilities import note_name_to_number

from utilities.music_structs import Note, Chord, Rest


class PlayPart(Callable):
    total_id = itt.count(0)
    def __init__(self, line_to_play: list[tuple[Note | Chord | Rest, float | int]] | MusicSeq, instrument: scamp.ScampInstrument, vol: float|int = 1.0, shift: int = 0, debug: bool = False, given_id: str|None = None):
        if given_id is None:
            self.id = next(self.total_id)
        else:
            self.id = given_id

        self.line_to_play = line_to_play
        if isinstance(self.line_to_play, MusicSeq):
            self.line_to_play = self.line_to_play.contents
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

class MusicSeq(Iterable):
    def __init__(self, *contents: tuple[Note | Chord | Rest, float | int] | MusicSeq):
        self.contents = []
        for item in contents:
            if isinstance(item, tuple):
                self.contents.append(item)
            else:
                self.contents.extend(item.contents)

    def duration(self):
        return sum(list(zip(*self.contents))[1])

    def __getitem__(self, index: int | float | slice):
        if isinstance(index, slice):
            start = index.start
            stop = index.stop

            if index.start is None:
                start = 0
            if index.stop is None:
                stop = self.duration()

            if start < 0:
                start = self.duration() + start
            if stop < 0:
                stop = self.duration() + stop

            if start == stop:
                return MusicSeq()

            started = False
            ret = []
            length = 0
            for item, dur in self.contents:
                length += dur
                if not started and start < length:
                    if stop < length:
                        ret.append((item, stop - start))
                        return MusicSeq(*ret)
                    else:
                        ret.append((item, length - start))
                        started = True
                elif started and stop >= length:
                    ret.append((item, dur))
                elif started and stop < length:
                    if stop - length + dur > 0:
                        ret.append((item, stop - (length - dur)))
                    return MusicSeq(*ret)
            return MusicSeq(*ret)
        else:
            if index < 0:
                raise ValueError("index can't be less than zero")
            elif index > self.duration():
                raise ValueError("index must be less than length")

            length = 0
            for item, dur in self.contents:
                length += dur
                if index < length:
                    return item
            return None

    def __iter__(self):
        return iter(self.contents)

    def append(self, item: tuple[Note | Chord | Rest, float | int]):
        self.contents.append(item)

    def extend(self, item: list[tuple[Note | Chord | Rest, float | int]] | MusicSeq):
        if isinstance(item, MusicSeq):
            self.contents.extend(item.contents)
        else:
            self.contents.extend(item)

    def copy(self, count: int = 1):
        ret = []
        for i in range(count):
            ret.append(self.__class__(*[item.copy() for item in self.contents]))
        return tuple(ret)

    def __add__(self, other: int | None):
        if other is None:
            return None
        new_contents = []
        for item, dur in self.contents:
            new_contents.append((item + other, dur))

        return self.__class__(*new_contents)

    def __sub__(self, other: int | None):
        if other is None:
            return None
        new_contents = []
        for item, dur in self.contents:
            new_contents.append((item - other, dur))

        return self.__class__(*new_contents)

    def __mul__(self, other: int):
        return self.__class__(*self.contents*other)

    def __rshift__(self, other: int | None):
        if other is None:
            return None
        new_contents = []
        for item, dur in self.contents:
            new_contents.append((item >> other, dur))

        return self.__class__(*new_contents)

    def __lshift__(self, other: int | None):
        if other is None:
            return None
        new_contents = []
        for item, dur in self.contents:
            new_contents.append((item << other, dur))

        return self.__class__(*new_contents)