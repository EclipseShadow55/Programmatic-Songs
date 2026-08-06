"""
Run this file to reset the SCAMP settings file to
before `scamp_recording_seting.py` was run
"""
import os
import json


if not os.path.isfile("scamp_reset_settings.json"):
    raise RuntimeError("Only works if `scamp_recording_seting.py` was run in the first place!")

with open("scamp_reset_settings.json", "r") as f:
    scamp_reset_settings = json.load(f)

scamp_playback_settings_path = scamp_reset_settings["scamp_playback_settings_path"]
prev_scamp_rec_path = scamp_reset_settings["prev_scamp_rec_path"]

with open(scamp_playback_settings_path, "r") as f:
    scamp_playback_settings = json.load(f)

scamp_playback_settings["recording_file_path"] = prev_scamp_rec_path

with open(scamp_playback_settings_path, "w") as f:
    json.dump(scamp_playback_settings, f, indent=4)