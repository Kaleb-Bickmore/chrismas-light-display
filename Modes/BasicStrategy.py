import random
import time
from LightModes.CandyCaneStrategy import CandyCaneStrategy
from LightModes.ChrismasColorStrategy import ChrismasColorStrategy
from LightModes.DigitalSnowStrategy import DigitalSnowStrategy
from LightModes.RainbowWaveStrategy import RainbowWaveStrategy

class BasicStrategy:
    _light_mode_strategies = {}
    _list_of_strategies = []
    def __init__(self):
        self._list_of_strategies = ["rainbow-wave", "chrismas-color", "digital-snow", "candy-cane"]
        self._light_mode_strategies["rainbow-wave"] = RainbowWaveStrategy()
        self._light_mode_strategies["chrismas-color"] = ChrismasColorStrategy()
        self._light_mode_strategies["candy-cane"] = CandyCaneStrategy()
        self._light_mode_strategies["digital-snow"] = DigitalSnowStrategy()







    def run(self):
        tmpList = self._list_of_strategies.copy()
        random.seed(time.clock())
        while(True):
            if(len(tmpList) == 0):
                tmpList = self._list_of_strategies.copy()
            random_light_mode = tmpList.pop(random.randint(0, len(tmpList)-1))
            print(random_light_mode)
            random_cycle_time = random.randint(45, 60)
            self._light_mode_strategies[random_light_mode].run(random_cycle_time, 60)


            
