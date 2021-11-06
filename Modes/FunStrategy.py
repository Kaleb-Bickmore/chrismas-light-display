import random
from LightModes.ChrismasColorStrategy import ChrismasColorStrategy
from LightModes.PingPongStrategy import PingPongStrategy
from LightModes.RainbowLazerStrategy import RainbowLazerStrategy
from LightModes.RainbowWaveStrategy import RainbowWaveStrategy
class FunStrategy:
    _light_mode_strategies = {}
    _list_of_strategies = []
    def __init__(self, bps):
        self._bps = bps
        self._list_of_strategies = ["rainbow-wave", "ping-pong", "rainbow-lazer", "chrismas-color"]
        self._light_mode_strategies["rainbow-wave"] = RainbowWaveStrategy()
        self._light_mode_strategies["ping-pong"] = PingPongStrategy()
        self._light_mode_strategies["rainbow-lazer"] = RainbowLazerStrategy()
        self._light_mode_strategies["chrismas-color"] = ChrismasColorStrategy()


    def run(self):
        while(True):
            random_light_mode = self._list_of_strategies[random.randint(0, len(self._list_of_strategies)-1)]
            random_cycle_time = random.randint(10, 20)
            self._light_mode_strategies[random_light_mode].run(random_cycle_time, self._bps)

