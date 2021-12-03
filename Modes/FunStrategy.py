import random
import time
from LightModes.CandyCaneStrategy import CandyCaneStrategy
from LightModes.ChrismasColorStrategy import ChrismasColorStrategy
from LightModes.DigitalSnowStrategy import DigitalSnowStrategy
from LightModes.LightShowStrategy import LightShowStrategy
from LightModes.RainbowLazerStrategy import RainbowLazerStrategy
from LightModes.RainbowWaveStrategy import RainbowWaveStrategy
from LightModes.ReactiveStrategy import ReactiveStrategy
from LightModes.SolidGroupStrategy import SolidGroupStrategy
from LightModes.SplitWaveStrategy import SplitWaveStrategy

class FunStrategy:
    _light_mode_strategies = {}
    _list_of_strategies = []
    def __init__(self):
        self._list_of_strategies = ["candy-cane","digital-snow","light-show", "split-wave","rainbow-wave", "rainbow-lazer", "chrismas-color","solid-group"]
        self._light_mode_strategies["rainbow-wave"] = RainbowWaveStrategy()
        self._light_mode_strategies["split-wave"] = SplitWaveStrategy()
        self._light_mode_strategies["rainbow-lazer"] = RainbowLazerStrategy()
        self._light_mode_strategies["chrismas-color"] = ChrismasColorStrategy()
        self._light_mode_strategies["candy-cane"] = CandyCaneStrategy()
        self._light_mode_strategies["light-show"] = LightShowStrategy()
        self._light_mode_strategies["digital-snow"] = DigitalSnowStrategy()
        self._light_mode_strategies["solid-group"] = SolidGroupStrategy()



    def run(self):
        tmpList = self._list_of_strategies.copy()
        random.seed(time.clock())
        while(True):
            if(len(tmpList) == 0):
                tmpList = self._list_of_strategies.copy()
            random_light_mode = tmpList.pop(random.randint(0, len(tmpList)-1))
            print(random_light_mode)
            random_cycle_time = random.randint(15, 25)
            self._light_mode_strategies[random_light_mode].run(random_cycle_time, 60)
