# Instructions
## Project Set Up (Assuming Windows, Similar for Other Systems)
1. CD into the project directory using `cd path\to\the\project`
2. (Optional) Create a venv and start it using `.venv/Scripts/activate.bat`
3. Install all the requirements using `pip install -r requirements.txt`
4. (Optional) [Set up recording](#setting-up-recording) if you want to export the final sound to a file
5. Run `music.py` to play the music live from the script
## About the Song
- The song is made using SCAMP, Suite for Computer-Assisted Music in Python)
- It is mosty a direct 'port' of music I composed partially in Tracktion Waveform 13, but I want to get into the algorithmic side of programmatic music composition in the future.
- In 4 parts: Melody (Clarinet), Harmony (Cello), Bass (Contrabass), High (Flute)
## Setting Up Recording
- SCAMP has a recording feature implemented, but as of early August 2026, does not have any public API for it. The only way to access it is to add a recording path directly in the settings file.
- To do this automatically, run `scamp_recording/scamp_recording_setup.py`, then just run `music.py` as normal and it will record the song to a wav file on top of playing it.
- To reset it to its original value, run `scamp_recording/scamp_recording_reset.py`. DO NOT DELETE `scamp_recording/scamp_reset_settings.json` or the resetting won't work.