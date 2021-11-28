import time
import random
from Lights.Pixels import Pixels

class SolidColorStrategy:
    def __init__(self):
        self._color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self._pixels = Pixels()

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        while(t_end>=time.time()):
            for i in range(0, self._pixels._num_pixels-1):
                if(random.randint(0,10) == 0):
                    self._pixels._pixels[i] = tuple(int(a/2) for a in self._color)
                else:
                    self._pixels._pixels[i] = self._color
            self._pixels._pixels.show()

                      


                


        
