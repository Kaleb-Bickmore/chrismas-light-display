import os
import sys
import PiFm

class MusicPlayer:
    def __init__(self):
        pass
    def play_song(self):
        bps = 60
        os.system("sudo ./pifm sound.wav 100.1")
        return bps
    