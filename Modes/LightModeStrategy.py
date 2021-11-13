from LightModes.SplitWaveStrategy import SplitWaveStrategy
from LightModes.ChrismasColorStrategy import ChrismasColorStrategy
from LightModes.DigitalSnowStrategy import DigitalSnowStrategy
from LightModes.RainbowLazerStrategy import RainbowLazerStrategy
from LightModes.RainbowWaveStrategy import RainbowWaveStrategy
from LightModes.ReactiveStrategy import ReactiveStrategy
from LightModes.SolidColorStrategy import SolidColorStrategy


class LightModeStrategy:
    _light_mode_strategies = {}
    def __init__(self):
        self._all_strategies = ["digital-snow","reactive", "rainbow-wave","split-wave", "rainbow-lazer", "chrismas-color", "solid-color"]
        self._light_mode_strategies["rainbow-wave"] = RainbowWaveStrategy()
        self._light_mode_strategies["split-wave"] = SplitWaveStrategy()
        self._light_mode_strategies["rainbow-lazer"] = RainbowLazerStrategy()
        self._light_mode_strategies["chrismas-color"] = ChrismasColorStrategy()
        self._light_mode_strategies["reactive"] = ReactiveStrategy()
        self._light_mode_strategies["digital-snow"] = DigitalSnowStrategy()
        self._light_mode_strategies["solid-color"] = SolidColorStrategy()


    def run(self, light_mode):
        if(light_mode in self._all_strategies):
            self._light_mode_strategies[light_mode].run(10800, 60)
        else:
            raise RuntimeError("lightmode "+light_mode +" is not currently implemented")
        

                      


                


        
