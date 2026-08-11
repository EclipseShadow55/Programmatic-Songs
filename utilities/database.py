from enum import StrEnum, auto as enum_auto


class TETNotes(StrEnum):
    A = "A"
    As = "A#"
    B = "B"
    C = "C"
    Cs = "C#"
    D = "D"
    Ds = "D#"
    E = "E"
    F = "F"
    Fs = "F#"
    G = "G"
    Gs = "G#"

TETNotesList = [
    TETNotes.C,
    TETNotes.Cs,
    TETNotes.D,
    TETNotes.Ds,
    TETNotes.E,
    TETNotes.F,
    TETNotes.Fs,
    TETNotes.G,
    TETNotes.Gs,
    TETNotes.A,
    TETNotes.As,
    TETNotes.B,
]

LetterNotesList = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G"
]