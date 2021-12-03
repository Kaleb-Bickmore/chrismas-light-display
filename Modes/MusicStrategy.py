import os
import random
import time
import subprocess
from MusicModes.AllIWantStrategy import AllIWantStrategy
from MusicModes.FelizNavidadStrategy import FelizNavidadStrategy
from MusicModes.JingleBellStrategy import JingleBellStrategy
from MusicModes.LastChristmasStrategy import LastChristmasStrategy
from MusicModes.WhiteChristmasStrategy import WhiteChristmasStrategy
from MusicModes.WinterWonderlandStrategy import WinterWonderlandStrategy

class MusicStrategy:
    _music_mode_strategies = {}
    _list_of_songs = []
    _cycle_times = {
        "white_christmas.wav": 159,
        "last_christmas.wav": 275,
        "jingle_bell.wav": 127,
        "winter_wonderland.wav": 147,
        "feliz_navidad.wav": 180,
        "all_i_want.wav": 239
    }
    _bps_times = {
        "white_christmas.wav": 60,
        "last_christmas.wav": 60,
        "jingle_bell.wav": 60,
        "winter_wonderland.wav": 60,
        "feliz_navidad.wav": 60,
        "all_i_want.wav": 60
    }
    def __init__(self):
#        self._list_of_songs = ["last_christmas.wav", "all_i_want.wav","feliz_navidad.wav","winter_wonderland.wav","white_christmas.wav","jingle_bell.wav"]
        self._list_of_songs = ["last_christmas.wav"]

        self._music_mode_strategies["last_christmas.wav"] = LastChristmasStrategy()
        self._music_mode_strategies["all_i_want.wav"] = AllIWantStrategy()
        self._music_mode_strategies["feliz_navidad.wav"] = FelizNavidadStrategy()
        self._music_mode_strategies["winter_wonderland.wav"] = WinterWonderlandStrategy()
        self._music_mode_strategies["white_christmas.wav"] = WhiteChristmasStrategy()
        self._music_mode_strategies["jingle_bell.wav"] = JingleBellStrategy()



    def run(self):
        tmpList = self._list_of_songs.copy()
        random.seed(time.clock())
        while(True):
            if(len(tmpList) == 0):
                tmpList = self._list_of_songs.copy()
            random_song = tmpList.pop(random.randint(0, len(tmpList)-1))
            process = subprocess.Popen(["./fm_transmitter/fm_transmitter -f  100.1 ./fm_transmitter/music/"+random_song], shell=True)
            self._music_mode_strategies[random_song].run(self._cycle_times[random_song], self._bps_times[random_song])
            process.wait()
