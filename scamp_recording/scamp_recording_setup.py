"""
For SCAMP recording, there doesn't seem to be any
public facing API even though the feature is included,
so run this file to modify the SCAMP settings file directly.

Change `OUTPUT_PATH` to the preferred relative
or absolute filepath of the output .wav file
"""

import os
import sys
import json

from scamp import Session


s = Session()

OUTPUT_PATH = "output.wav"


if sys.platform.startswith("win"):
    os_data_path = os.getenv("LOCALAPPDATA")
elif sys.platform.startswith("darwin"):
    os_data_path = "~/Library/Application Support"
else:
    os_data_path = os.getenv("XDG_DATA_HOME", "~/.local/share")

os_data_path = os.path.expanduser(os_data_path)
scamp_playback_settings_path = os.path.join(os_data_path, "SCAMP", "playbackSettings.json")

with open(scamp_playback_settings_path, "r") as f:
    scamp_playback_settings = json.load(f)

prev_scamp_rec_path = scamp_playback_settings["recording_file_path"]
scamp_playback_settings["recording_file_path"] = OUTPUT_PATH

with open(scamp_playback_settings_path, "w") as f:
    json.dump(scamp_playback_settings, f, indent=4)

scamp_reset_settings = {
    "scamp_playback_settings_path": scamp_playback_settings_path,
    "prev_scamp_rec_path": prev_scamp_rec_path
}

with open("scamp_reset_settings.json", "w") as f:
    json.dump(scamp_reset_settings, f, indent=4)