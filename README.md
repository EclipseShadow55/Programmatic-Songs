# Instructions
## Project Set Up (Assuming Windows, Should Be Similar for Other Operating Systems)
1. CD into the project directory using `cd path\to\the\project`
2. (Optional) [Create and activate a virtual environment](https://www.w3schools.com/python/python_virtualenv.asp)
3. Install all the requirements using `pip install -r requirements.txt`
4. (Optional) [Set up recording](#setting-up-recording) if you want to export the final sound to a file
5. Run `music.py` to play the music live from the script
## Description
- Made using SCAMP (Suite for Computer-Assisted Music in Python) for composition and playback
- Uses instruments from the [GeneralUser-GS Soundfont by S. Christian Collins](https://schristiancollins.com/generaluser.php), which follows to the General MIDI 2.0 Standard
- Implements helper structures in `utilities\scamp_utils.py`
## Songs
### Song 1
- 4 parts: Melody (Clarinet), Harmony (Cello), Bass (Double Bass), High (Flute)
### Song 2
- 4 Parts: Melody (Grand Piano), Harmony (Grand Piano), Bass (Star Theme + Warm Pad + Synth Bass 2), Drums (Electronic Kit - C2 = Bass Drum, D2 = Snare Drum, F#2 = Closed Hat)
### Song 3
- 4 Parts: Melody (Clarinet), Harmony (Cello), Bass (Star Theme + Warm Pad + Synth Bass 2), Drums (Electronic Kit - C2 = Bass Drum, D2 = Snare Drum, F#2 = Closed Hat)
## Setting Up Recording
- SCAMP has a recording feature implemented, but as of the time this was developed, it does not have any public API for it. The only way to access it is to add a recording path directly in the settings file.
- To do this automatically, run `scamp_recording/scamp_recording_setup.py`, then just run `music.py` as normal and it will record the song to a wav file on top of playing it.
- To reset it to its original value, run `scamp_recording/scamp_recording_reset.py`. DO NOT DELETE `scamp_recording/scamp_reset_settings.json` or the resetting won't work.