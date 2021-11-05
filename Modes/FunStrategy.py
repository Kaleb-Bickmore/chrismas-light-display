import random
from LightModes.RainbowWaveStrategy import RainbowWaveStrategy
class FunStrategy:
    _light_mode_strategies = {}
    _list_of_strategies = []
    def __init__(self, bps):
        self._bps = bps
        self._list_of_strategies = ["rainbow-wave"]
        self._light_mode_strategies["rainbow-wave"] = RainbowWaveStrategy()

    def run(self):
        while(True):
            random_light_mode = self._list_of_strategies[random.randint(0, len(self._list_of_strategies)-1)]
            random_cycle_time = random.randint(10, 20)
            self._light_mode_strategies[random_light_mode].run(random_cycle_time, self._bps)

