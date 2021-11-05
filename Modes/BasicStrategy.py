import random
import time
from LightModes.PingPongStrategy import PingPongStrategy
from LightModes.RainbowLazerStrategy import RainbowLazerStrategy
from LightModes.RainbowWaveStrategy import RainbowWaveStrategy

class BasicStrategy:
    _light_mode_strategies = {}
    _list_of_strategies = []
    def __init__(self, bps):
        self._bps = bps
        self._list_of_strategies = ["rainbow-wave", "ping-pong", "rainbow-lazer"]
        self._light_mode_strategies["rainbow-wave"] = RainbowWaveStrategy()
        self._light_mode_strategies["ping-pong"] = PingPongStrategy()
        self._light_mode_strategies["rainbow-lazer"] = RainbowLazerStrategy()



    def run(self):
        while(True):
            random_light_mode = self._list_of_strategies[random.randint(0, len(self._list_of_strategies)-1)]
            random_cycle_time = random.randint(10, 20)
            self._light_mode_strategies[random_light_mode].run(random_cycle_time, self._bps)
            time.sleep(self._bps/600)


            
