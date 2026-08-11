from pathlib import Path

from scamp import Session

from utilities.music_structs import Note, Chord, Scales
from utilities.scamp_utils import PlayPart


current_key = Note.from_name("A#3")
current_scale = Scales.Major(current_key)

# PATTERN
drum_pattern = [
    (Chord.from_note_names("D2", "C2"), 1/4), (Note.from_name("F#2"), 1/8),
    (Note.from_name("F#2"), 1/8),

    (Chord.from_note_names("F#2", "C2"), 1/4), (Note.from_name("F#2"), 1/4),

    (Chord.from_note_names("D2", "C2"), 1/8), (Note.from_name("F#2"), 1/8),
    (Note.from_name("F#2"), 1/8), (Note.from_name("F#2"), 1/8),

    (Chord.from_note_names("D2", "C2"), 1/4), (Note.from_name("D2"), 1/4),

    (Chord.from_note_names("D2", "C2"), 1/8), (Note.from_name("F#2"), 1/8),
    (Note.from_name("F#2"), 1/8), (Note.from_name("D2"), 1/8),

    (Chord.from_note_names("F#2", "C2"), 1/8), (Note.from_name("F#2"), 1/8),
    (Note.from_name("D2"), 1/8), (Note.from_name("F#2"), 1/8),

    (Chord.from_note_names("F#2", "C2"), 1/8), (Note.from_name("D2"), 1/8),
    (Note.from_name("F#2"), 1/8), (Note.from_name("F#2"), 1/8),

    (Chord.from_note_names("D2", "C2"), 1/4), (Chord.from_note_names("D2", "C2"), 1/4)
]
harmony_pattern = [
    (Chord.from_note_names("A3", "C4", "E4"), 1/1),
    (Chord.from_note_names("G3", "B3", "D4"), 1/1),
    (Chord.from_note_names("G3", "C4", "E4"), 1/1),
    (Chord.from_note_names("F3", "A3", "C4"), 1/1),
]
bass_pattern = [
    (Chord.from_note_names("A1", "A2"), 1/1),
    (Chord.from_note_names("G1", "G2"), 1/1),
    (Chord.from_note_names("C1", "C2"), 1/1),
    (Chord.from_note_names("F1", "F2"), 1/1),
]
melody_pattern = [
    (Note.from_name("C4"), 1/4), (Note.from_name("D4"), 1/8),
    (Note.from_name("E4"), 1/8), (Note.from_name("E4"), 1/4),
]

# INTRO
drum_intro = [
    (None, 4/1), *drum_pattern,
]
harmony_intro = [
    *harmony_pattern*2,
]
bass_intro = [
    (None, 4/1), *bass_pattern,
]
melody_intro = [
    (None, 8/1),
]

# VERSE 1
drum_verse1 = [
    *drum_pattern,
]
harmony_verse1 = [
    *harmony_pattern,
]
bass_verse1 = [
    *bass_pattern,
]
melody_verse1 = [
    *melody_pattern, (Note.from_name("G4"), 1/4),
    (Note.from_name("F4"), 3/8), (Note.from_name("E4"), 1/8), (Note.from_name("D4"), 1/4), (Note.from_name("F4"), 1/4),
    (Note.from_name("E4"), 3/8), (Note.from_name("D4"), 1/8), (Note.from_name("C4"), 1/4), (Note.from_name("E4"), 1/4),
    (Note.from_name("C4"), 1/1),
]

# VERSE 2
drum_verse2 = [
    *drum_pattern,
]
harmony_verse2 = [
    *harmony_pattern,
]
bass_verse2 = [
    *bass_pattern,
]
melody_verse2 = [
    *melody_pattern, (Note.from_name("G4"), 1/4),
    (Note.from_name("C5"), 3/8), (Note.from_name("G4"), 1/8), (Note.from_name("F4"), 1/4), (Note.from_name("E4"), 1/4),
    (Note.from_name("C4"), 3/8), (Note.from_name("E4"), 3/8), (Note.from_name("F4"), 3/8), (Note.from_name("E4"), 3/8),
    (Note.from_name("C4"), 1/4), (Note.from_name("B3"), 1/4),
]

# ENDING
drum_end = [
    *drum_pattern,
]
harmony_end = [
    *harmony_pattern,
]
bass_end = [
    *bass_pattern,
]
melody_end = [
    *melody_pattern, (Note.from_name("D4"), 1/4),
    *melody_pattern, (Note.from_name("D4"), 1/4),
    *melody_pattern, (Note.from_name("D4"), 1/4),
    (Chord.from_note_names("C4", "E4"), 1/2)
]

# LINE
drum_line = [
    *drum_intro,
    *drum_verse1,
    *drum_verse2,
    *drum_verse1,
    *drum_end,
]
harmony_line = [
    *harmony_intro,
    *harmony_verse1,
    *harmony_verse2,
    *harmony_verse1,
    *harmony_end,
]
bass_line = [
    *bass_intro,
    *bass_verse1,
    *bass_verse2,
    *bass_verse1,
    *bass_end
]
melody_line = [
    *melody_intro,
    *melody_verse1,
    *melody_verse2,
    *melody_verse1,
    *melody_end
]


s = Session(tempo=38, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))
drum_inst = s.new_part("Electronic Kit")
harmony_inst = s.new_part("Grand Piano")
star_bass_inst = s.new_part("Star Theme")
pad_bass_inst = s.new_part("Warm Pad")
synth_bass_inst = s.new_part("Synth Bass 2")
melody_inst = s.new_part("Grand Piano")


def music_play():
    s.fork(PlayPart(drum_line, drum_inst, vol=0.5))
    s.fork(PlayPart(harmony_line, harmony_inst, vol=0.7))
    s.fork(PlayPart(bass_line, star_bass_inst, 0.7))
    s.fork(PlayPart(bass_line, pad_bass_inst, 0.8))
    s.fork(PlayPart(bass_line, synth_bass_inst, 0.7))
    s.fork(PlayPart(melody_line, melody_inst))

    s.wait_for_children_to_finish()


if __name__ == '__main__':
    music_play()