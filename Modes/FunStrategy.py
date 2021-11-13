import random
import time
from LightModes.ChrismasColorStrategy import ChrismasColorStrategy
from LightModes.DigitalSnowStrategy import DigitalSnowStrategy
from LightModes.RainbowLazerStrategy import RainbowLazerStrategy
from LightModes.RainbowWaveStrategy import RainbowWaveStrategy
from LightModes.ReactiveStrategy import ReactiveStrategy

class FunStrategy:
    _light_mode_strategies = {}
    _list_of_strategies = []
    def __init__(self, bps):
        self._bps = bps
        self._list_of_strategies = ["digital-snow","reactive", "rainbow-wave", "rainbow-lazer", "chrismas-color"]
        self._light_mode_strategies["rainbow-wave"] = RainbowWaveStrategy()
        self._light_mode_strategies["rainbow-lazer"] = RainbowLazerStrategy()
        self._light_mode_strategies["chrismas-color"] = ChrismasColorStrategy()
        self._light_mode_strategies["reactive"] = ReactiveStrategy()
        self._light_mode_strategies["digital-snow"] = DigitalSnowStrategy()


    def run(self):
        tmpList = self._list_of_strategies.copy()
        random.seed(time.clock())
        while(True):
            if(len(tmpList) == 0):
                tmpList = self._list_of_strategies.copy()
            random_light_mode = tmpList.pop(random.randint(0, len(tmpList)-1))
            print(random_light_mode)
            random_cycle_time = random.randint(15, 25)
            self._light_mode_strategies[random_light_mode].run(random_cycle_time, self._bps)
            time.sleep(self._bps/600)
