import time
import random
from Pixels import Pixels

class ChrismasColorStrategy:
    def __init__(self):
        self._pixels = Pixels()

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        while(t_end>=time.time()):
            for i in range(0, self._pixels._num_pixels-1):
                if(i%3 == 0):
                    if(random.randint(0,10) == 0):
                        self._pixels._pixels[i] = (int(255/2), 0, 0)
                    else:
                        self._pixels._pixels[i] = (255, 0, 0)
                if(i%3 == 1):
                    if(random.randint(0,10) == 0):
                        self._pixels._pixels[i] = (0,int(255/2), 0)
                    else:
                        self._pixels._pixels[i] = (0, 255, 0)
                if(i%3 == 2):
                    if(random.randint(0,10) == 0):
                        self._pixels._pixels[i] = (int(255/2),int(255/2), int(255/2))
                    else:
                        self._pixels._pixels[i] = (255, 255, 255) 
            self._pixels._pixels.show()

                      


                


        
