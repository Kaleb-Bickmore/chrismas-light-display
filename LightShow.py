from Modes.BasicStrategy import BasicStrategy
from Modes.MusicStrategy import MusicStrategy
from Modes.FunStrategy import FunStrategy
from Pixels import Pixels

class LightShow:
    _mode_strategies = {}
    def __init__(self):
        self._mode_strategies["basic"] = BasicStrategy(60)
        self._mode_strategies["music"] = MusicStrategy(60)
        self._mode_strategies["fun"] = FunStrategy(60)
        self._pixels = Pixels()

    def run(self, mode):
        self._mode_strategies[mode].run()

    def turn_off(self):
        self._pixels.turn_off()

