import time
import random
from Pixels import Pixels

class SplitWaveStrategy:
    def __init__(self):
        self._pixels = Pixels()
    def wheel(self, i):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
        if(i<50):
            return (255,0,0)

        if(i>=50 and i <100):
            return (0,255,0)

        if(i>=100 and i <150):
            return (255,255,255)

        if(i>=150 and i <200):
            return (255,0,0)

        if(i>=200 and i <250):
            return (0,255,0)

        if(i>=250 and i <300):
            return (255,255,255)

        if(i>=300 and i <350):
            return (255,0,0)

        if(i>=350):
            return (0,255,0)
    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        while(t_end>=time.time()):
            step = 5
            split = 50
            ratio = int(self._pixels._num_pixels/split)

            for i in range(0, split, step):
                for j in range(ratio):
                    self._pixels._pixels[i+split*j:i+step+split*j] = [ self.wheel(i+split*j) for aa in self._pixels._pixels[i+split*j:i+step+split*j]]
                self._pixels._pixels.show()
                time.sleep(bps/6000)

            for i in range(split,0,-1*step):
                for j in range(ratio):
                    self._pixels._pixels[i-step+split*j:i+split*j] = [(0,0,0) for aa in self._pixels._pixels[i-step+split*j:i+split*j]]
                self._pixels._pixels.show()
                time.sleep(bps/6000)


                      


                


        
