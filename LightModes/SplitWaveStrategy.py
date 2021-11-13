import time
import random
from Pixels import Pixels

class SplitWaveStrategy:
    def __init__(self):
        self._pixels = Pixels()
    def wheel(self, pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
        pos = pos%255
        if pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b)
    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        while(t_end>=time.time()):
            step = 5
            split = 50
            ratio = self._pixels._num_pixels/split
            
            for i in range(0, split, step):
                for j in range(ratio):
                    self._pixels._pixels[i+split*j:i+step+split*j] = [self.wheel(aa) for aa in self._pixels._pixels[i+split*j:i+step+split*j]]
                self._pixels._pixels.show()

            for i in range(split,step,-1*step):
                for j in range(ratio):
                    self._pixels._pixels[i-step+split*j:i+split*j] = [(0,0,0) for aa in self._pixels._pixels[i-step+split*j:i+split*j]]
                self._pixels._pixels.show()


                      


                


        
