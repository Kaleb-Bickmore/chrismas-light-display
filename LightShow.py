from Modes.BasicStrategy import BasicStrategy
from Modes.LightModeStrategy import LightModeStrategy
from Modes.MusicStrategy import MusicStrategy
from Modes.FunStrategy import FunStrategy
from Lights.Pixels import Pixels

class LightShow:
    _mode_strategies = {}
    def __init__(self):
        self._mode_strategies["basic"] = BasicStrategy()
        self._mode_strategies["music"] = MusicStrategy()
        self._mode_strategies["fun"] = FunStrategy()
        self._light_mode_strategy = LightModeStrategy()

        self._pixels = Pixels()

    def run(self, mode, lightmode):
        if(lightmode != None):
            self._light_mode_strategy.run(lightmode)
        else:
            if(mode == None):
                mode = "basic"
        self._mode_strategies[mode].run()

    def turn_off(self):
        self._pixels.turn_off()

