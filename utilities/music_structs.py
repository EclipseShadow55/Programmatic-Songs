"""
Simple structures for musical parts, SCAMP ones are overly complicated
"""

import math
from collections.abc import Iterable

from scamp_extensions.pitch.utilities import note_name_to_number

from utilities.database import TETNotes, TETNotesList, LetterNotesList


class Note:
    name: TETNotes
    octave: int

    @classmethod
    def from_name(cls, name: str):
        if len(name) < 2:
            raise ValueError("invalid note representation")

        up_name = name.upper()
        if up_name[0] in LetterNotesList:
            let_ind = LetterNotesList.index(up_name[0])
        else:
            raise ValueError(f"invalid note letter: {name[0]}")

        num_start = 2
        if up_name[1] == "#":
            note_mod = "#"
        elif up_name[1] == "b":
            let_ind = (let_ind - 1) % len(LetterNotesList)
            note_mod = "#"
        else:
            note_mod = ""
            num_start = 1

        note_ind = TETNotesList.index(LetterNotesList[let_ind] + note_mod)
        if note_ind == -1:
            raise ValueError("invalid note representation")

        if len(name) + 1 <= num_start:
            raise ValueError("invalid note representation")

        try:
            octave = int(up_name[num_start:])
        except ValueError:
            raise ValueError("invalid note representation")

        return cls(TETNotesList[note_ind], octave)

    def __init__(self, name: TETNotes, octave: int):
        self.name = name
        self.octave = octave

    def __str__(self):
        return self.name + str(self.octave)

    def __repr__(self):
        return str(self)

    def tet_ind(self):
        return TETNotesList.index(self.name)

    def to_number(self):
        return note_name_to_number(str(self))

    def copy(self):
        return self.__class__(self.name, self.octave)

    def __add__(self, other: int | None): # Shift up one note
        if other is None:
            return None
        ind = TETNotesList.index(self.name)
        step = math.floor((ind + other) / 12)
        return self.__class__(TETNotesList[(ind + other) % 12], self.octave + step)

    def __sub__(self, other: int | None): # Shift down one note
        if other is None:
            return None
        ind = TETNotesList.index(self.name)
        step = math.floor((ind - other) / 12)
        return self.__class__(TETNotesList[(ind - other) % 12], self.octave + step)

    def __rshift__(self, other: int | None): # Shift up one octave
        if other is None:
            return None
        return self.__class__(self.name, self.octave + other)

    def __lshift__(self, other: int | None): # Shift down one octave
        if other is None:
            return None
        return self.__class__(self.name, self.octave - other)

    def perfect_fifth(self):
        return self + 7

    def perfect_fourth(self):
        return self + 5

class Chord:
    notes: list[Note]

    @classmethod
    def from_note_names(cls, first: str|list[str], *names: str):
        if isinstance(first, list):
            note_names = first
        else:
            note_names = [first] + list(names)
        notes = []
        for note_name in note_names:
            notes.append(Note.from_name(note_name))
        return cls(notes)

    def __init__(self, first: Note | Iterable[Note], *notes: Note):
        if isinstance(first, Note):
            self.notes = [first] + list(notes)
        elif isinstance(first, Iterable):
            self.notes = list(first)

    def __str__(self):
        return f"Chord({[str(note) for note in self.notes]})"

    def __repr__(self):
        return str(self)

    def tet_inds(self):
        ret_inds = []
        for note in self.notes:
            ret_inds.append(note.tet_ind())
        return ret_inds

    def to_numbers(self):
        return list(map(lambda x: note_name_to_number(str(x)), self.notes))

    def copy(self):
        return self.__class__(self.notes.copy())

    def __add__(self, other: int | None): # Shift up one note
        if other is None:
            return None
        ret_notes = []
        for note in self.notes:
            ret_notes.append(note + other)
        return self.__class__(ret_notes)

    def __sub__(self, other: int | None): # Shift down one note
        if other is None:
            return None
        ret_notes = []
        for note in self.notes:
            ret_notes.append(note - other)
        return self.__class__(ret_notes)

    def __rshift__(self, other: int | None): # Shift up one octave
        if other is None:
            return None
        ret_notes = []
        for note in self.notes:
            ret_notes.append(note >> other)
        return self.__class__(ret_notes)

    def __lshift__(self, other: int | None): # Shift down one octave
        if other is None:
            return None
        ret_notes = []
        for note in self.notes:
            ret_notes.append(note << other)
        return self.__class__(ret_notes)

    def layered(self):
        ret = []
        for i, note in enumerate(self.notes):
            if i == 0:
                ret.append(self.notes[0])
            else:
                ret.append(self.__class__(self.notes[:i+1]))
        return ret


class Scale:
    shift_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    indexing = 12
    length = 12

    root: Note

    def __init__(self, root: Note):
        self.root = root

    def __len__(self):
        return self.indexing

    def __str__(self):
        return str(self.root) + " Chromatic Scale"

    def __repr__(self):
        return str(self)

    def size(self):
        return self.length

    def __getitem__(self, index: int):
        if index < 0:
            raise ValueError("index out of range")

        oct_shift = index // len(self)
        ret = self.root >> oct_shift
        if self.shift_set[index % len(self)] is None:
            return None
        return ret + self.shift_set[index % len(self)]

    def __add__(self, other: int | None): # Shift up one note
        new_root = self.root + other
        if new_root is None:
            return None
        return self.__class__(new_root)

    def __sub__(self, other: int | None): # Shift up one note
        new_root = self.root - other
        if new_root is None:
            return None
        return self.__class__(new_root)

    def __rshift__(self, other: int | None): # Shift up one note
        new_root = self.root >> other
        if new_root is None:
            return None
        return self.__class__(new_root)

    def __lshift__(self, other: int | None): # Shift up one note
        new_root = self.root << other
        if new_root is None:
            return None
        return self.__class__(new_root)

    def notes(self, end_cap: bool = True):
        return list(map(lambda x: self[x], range(len(self) + int(end_cap))))

    def chord(self, index: int):
        ind = index - 1
        notes = [self[ind], self[ind+2], self[ind+4]]
        return Chord(*notes)

class HeptaScale(Scale):
    length = 7

    def tonic(self):
        return self.root.copy()

    def first(self):
        return self.root + self.shift_set[0]

    def second(self):
        return self.root + self.shift_set[1]

    def third(self):
        return self.root + self.shift_set[2]

    def fourth(self):
        return self.root + self.shift_set[3]

    def fifth(self):
        return self.root + self.shift_set[4]

    def sixth(self):
        return self.root + self.shift_set[5]

    def seventh(self):
        return self.root + self.shift_set[6]

class PentaScale(Scale):
    length = 5

    def tonic(self):
        return self.root.copy()

    def third(self):
        return self.root + self.shift_set[2]

    def fourth(self):
        return self.root + self.shift_set[3]

    def fifth(self):
        return self.root + self.shift_set[4]

    def seventh(self):
        return self.root + self.shift_set[6]

class Scales:
    class NaturalScales:
        class Major(HeptaScale):
            shift_set = [0, 2, 4, 5, 7, 9, 11]
            indexing = 7

            def __str__(self):
                return str(self.root) + " Natural Major Scale"

        class Minor(HeptaScale):
            shift_set = [0, 2, 3, 5, 7, 8, 10]
            indexing = 7

            def __str__(self):
                return str(self.root) + " Natural Minor Scale"

        class Dorian(HeptaScale):
            shift_set = [0, 2, 3, 5, 7, 9, 10]
            indexing = 7

            def __str__(self):
                return str(self.root) + " Dorian Mode Scale"

        class Phrygian(HeptaScale):
            shift_set = [0, 1, 3, 5, 7, 8, 10]
            indexing = 7

            def __str__(self):
                return str(self.root) + " Natural Phrygian Scale"

        class Locrian(HeptaScale):
            shift_set = [0, 1, 3, 5, 6, 8, 10]
            indexing = 7

            def __str__(self):
                return str(self.root) + " Natural Locrian Scale"

        class MajPenta(PentaScale):
            shift_set = [0, 2, 5, None, 7, 9, None]
            indexing = 7 # Base Diatonic Uses 7-Indexed Notes

            def __str__(self):
                return str(self.root) + " Natural Major Pentatonic Scale"

        class MinPenta(PentaScale):
            shift_set = [0, None, 3, 5, 7, None, 10]
            indexing = 7 # Base Diatonic Uses 7-Indexed Notes

    class HarmonicScales:
        class Minor(HeptaScale):
            shift_set = [0, 2, 3, 5, 7, 8, 11]
            indexing = 7

            def __str__(self):
                return str(self.root) + " Harmonic Minor Scale"

    class MelodicScales:
        class Minor(HeptaScale):
            shift_set = [0, 2, 4, 5, 7, 8, 11]
            indexing = 7

            def __str__(self):
                return str(self.root) + " Melodic Minor Scale"


class Rest:
    def __str__(self):
        return "Rest"

    def __repr__(self):
        return str(self)


N = Note.from_name
C = Chord.from_note_names
R = Rest