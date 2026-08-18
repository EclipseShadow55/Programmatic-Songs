from pathlib import Path

from scamp import Session

from utilities.music_structs import Scales, Chord, N, C, R
from utilities.scamp_utils import PlayPart, MusicSeq


key = N("C5")
scale = Scales.NaturalScales.Minor(key) # C3, D3, D#3, F3, G3, G#3, A#3, C4

# CHORUS
melody_chorus = MusicSeq(*[
    (N("C5"), 1/2), (N("C5"), 3/8), (N("G#4"), 1/8),
    (N("A#4"), 1/8), (N("G4"), 1/8), (N("G4"), 1/4), (N("G4"), 3/8), (N("G4"), 1/8),
    (N("F4"), 1/4), (N("F4"), 1/4), (N("F4"), 1/8), (N("G4"), 1/8), (N("G#4"), 1/4),
    (N("C5"), 1/4), (N("G4"), 1/4), (N("G4"), 1/2),

    (N("C5"), 1/2), (N("C5"), 1/4), (N("G#4"), 1/8), (N("G#4"), 1/8),
    (N("A#4"), 1/8), (N("G4"), 1/8), (N("G4"), 1/4), (N("G4"), 3/8), (N("D#4"), 1/8),
    (N("G4"), 1/4), (N("F4"), 1/4), (N("D#4"), 1/4), (N("D4"), 1/4),
    (N("C4"), 1/1)
])
drum1_chorus = MusicSeq(*[
    (C("C#2", "C2"), 1/2), (N("C#2"), 1/2),
    (C("C#2", "C2"), 1/2), (N("C#2"), 1/2),
    (C("C#2", "C2"), 1/2), (N("C#2"), 1/2),
    (C("C#2", "C2"), 1/2), (N("C#2"), 1/2),

    (C("C#2", "C2"), 1/4), (N("C#2"), 1/4), (C("C#2", "C2"), 1/4), (N("C#2"), 1/4),
    (C("C#2", "C2"), 1/4), (N("C#2"), 1/4), (C("C#2", "C2"), 1/4), (N("C#2"), 1/4),
    (C("C#2", "C2"), 1/8), (N("C#2"), 1/8), (C("C#2", "C2"), 1/8), (N("C#2"), 1/8),
    (C("C#2", "C2"), 1/8), (N("C#2"), 1/8), (C("C#2", "C2"), 1/8), (N("C#2"), 1/8),
    (C("C#2", "C2"), 1/1),
])
drum2_chorus = MusicSeq(*[
    *[(N("G#2"), dur)
      for item, dur in melody_chorus if not isinstance(item, R)]
])
harmony_chorus = MusicSeq(*[
    *[(C("G3", "C4", "D#4"), 1/1)],
    *[(C("F3", "D4"), 1/1)],
    *[(C("G3", "A#3", "D#4"), 1/1)],
    *[(C("D#3", "A#3", "G4"), 1/1)],

    *[(C("G3", "C4", "D#4"), 1/2)]*2,
    *[(C("F3", "D4"), 1/2)]*2,
    *[(C("G3", "A#3", "D#4"), 1/4)]*4,
    *[(C("D#3", "G3", "C4"), 1/1)],
])
bass_chorus = MusicSeq(*[
    *[(Chord(item << 1, item) if not isinstance(item, R) else R(), dur)
      for item, dur in melody_chorus]
])

# VERSE 1
melody_verse1 = MusicSeq(*[
    (N("A#4"), 1/2),
    (N("C5"), 1/4), (N("C5"), 1/8), (N("C5"), 1/8), (N("C5"), 1/4), (N("D#5"), 1/4),
    (N("G5"), 1/4), (N("G5"), 1/4), (N("G5"), 1/4), (N("G5"), 1/8), (N("G5"), 1/8),
    (N("G#5"), 1/4), (N("F5"), 1/8), (N("F5"), 1/8), (N("F5"), 1/4), (N("G5"), 1/8), (N("G#5"), 1/8),
    (N("C6"), 1/8), (N("G5"), 1/8), (N("G5"), 1/4), (N("G5"), 3/8), (N("G5"), 1/8),

    (N("C5"), 1/4), (N("C5"), 1/4), (N("C5"), 1/4), (N("D#5"), 1/8), (N("F5"), 1/8),
    (N("G5"), 1/4), (N("G5"), 1/4), (N("G5"), 1/4), (N("G5"), 1/4),
    (N("G5"), 1/4), (N("F5"), 1/4), (N("D#5"), 1/8), (N("D#5"), 1/8), (N("D5"), 1/4),
    (N("C5"), 1/2), (R(), 1/2),
]) << 1
drum1_verse1 = MusicSeq(*[
    (R(), 1/2),
    (N("C#2"), 1/2), (N("C#2"), 1/2),
    (N("C#2"), 1/2), (N("C#2"), 1/2),
    (N("C#2"), 1/2), (N("C#2"), 1/2),
    (N("C#2"), 1/2), (N("C#2"), 1/2),

    (N("C#2"), 1/2), (N("C#2"), 1/2),
    (N("C#2"), 1/2), (N("C#2"), 1/2),
    (N("C#2"), 1/2), (N("C#2"), 1/2),
    (N("C#2"), 1/2), (C("C#2", "C2", "D2", "E2"), 1/2),
])
drum2_verse1 = MusicSeq(*[
    (R(), 1/2),
    *[(N("G#2") if not isinstance(item, R) else R(), dur)
      for item, dur in melody_verse1[1/2:]]
])

# VERSE 2
melody_verse2 = MusicSeq(*[
    (N("A#4"), 1/4),
    (N("C5"), 1/4), (N("C5"), 1/4), (N("C5"), 1/4), (N("D#5"), 1/4),
    (N("G5"), 1/4), (N("G5"), 1/4), (N("G5"), 1/4), (N("G5"), 1/8), (N("G5"), 1/8),
    (N("G#5"), 1/4), (N("F5"), 1/4), (N("F5"), 1/4), (N("G5"), 1/4),
    (N("C6"), 1/4), (N("G5"), 1/4), (N("G5"), 1/4), (N("G5"), 1/8), (N("G5"), 1/8),

    (N("C5"), 1/4), (N("C5"), 1/8), (N("C5"), 1/8), (N("C5"), 1/4), (N("D#5"), 1/8), (N("F5"), 1/8),
    (N("G5"), 1/4), (N("G5"), 1/4), (N("G5"), 1/4), (N("G5"), 1/4),
    (N("G5"), 1/4), (N("F5"), 1/4), (N("D#5"), 1/4), (N("D5"), 1/4),
    (N("C5"), 1/2), (R(), 1/2),
]) << 1
drum1_verse2 = MusicSeq(*[
    (C("C#2", "C2"), 1/2), (N("C#2"), 1/2),
    (N("C#2"), 1/2), (N("C#2"), 1/2),
    (C("C#2", "C2"), 1/2), (N("C#2"), 1/2),
    (N("C#2"), 1/2), (N("C#2"), 1/2),

    (C("C#2", "C2"), 1/2), (N("C#2"), 1/2),
    (N("C#2"), 1/2), (N("C#2"), 1/2),
    (C("C#2", "C2"), 1/2), (N("C#2"), 1/2),
    (N("C#2"), 1/2), (C("C#2", "C2", "D2", "E2"), 1/2),
])
drum2_verse2 = MusicSeq(*[
    (R(), 1/4),
    *[(N("G#2") if not isinstance(item, R) else R(), dur)
      for item, dur in melody_verse2[1/4:]]
])
bass_verse2 = MusicSeq(*[
    *[(Chord(item << 1, item) if not isinstance(item, R) else R(), dur)
      for item, dur in melody_verse2]
])

# LINE
melody_line = MusicSeq(*[
    melody_verse1,
    melody_chorus[:-1/4],
    melody_verse2,
    melody_chorus,
])
drum1_line = MusicSeq(*[
    drum1_verse1,
    drum1_chorus,
    drum1_verse2,
    drum1_chorus,
])
drum2_line = MusicSeq(*[
    drum2_verse1,
    drum2_chorus[:-1/4],
    drum2_verse2,
    drum2_chorus,
])
harmony_line = MusicSeq(*[
    (R(), 1/2),
    (R(), 8/1),
    harmony_chorus,
    (R(), 8/1),
    harmony_chorus,
])
bass_line = MusicSeq(*[
    (R(), 1/2),
    (R(), 8/1),
    bass_chorus[:-1/4],
    bass_verse2,
    bass_chorus,
]) << 2


s = Session(tempo=55, default_soundfont=str(Path(__file__).parent.parent / "GeneralUser-GS.sf2"))
melody_inst = s.new_part("Cello")
drum_inst = s.new_part("Electronic Kit")
harmony_inst = s.new_part("Grand Piano")
synth_bass_inst = s.new_part("Synth Bass 2")


def play():
    s.fork(PlayPart(melody_line, melody_inst))
    s.fork(PlayPart(drum1_line, drum_inst, vol=0.9))
    s.fork(PlayPart(drum2_line, drum_inst, vol=0.8))
    s.fork(PlayPart(harmony_line, harmony_inst, vol=0.8))
    s.fork(PlayPart(bass_line, synth_bass_inst, vol=0.7))

    s.wait_for_children_to_finish()

if __name__ == "__main__":
    play()