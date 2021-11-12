import time
import random
from datetime import datetime, timedelta
from Pixels import Pixels

class RainbowLazerStrategy:
    def __init__(self):
        self._pixels = Pixels()

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        pos = 0
        step = 5
        cleanup = False
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
      
        while t_end >= time.time():
            if(pos >= self._pixels._num_pixels-1):
                pos = 0
                if(cleanup):
                    cleanup = False
                else:
                    cleanup = True
            pos = pos+step+1
            if(cleanup):
                self._pixels._pixels[pos:pos+step] = [(0, 0, 0) for aa in self._pixels._pixels[pos:pos+step]]
            else:
                self._pixels._pixels[pos:pos+step] = [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for aa in self._pixels._pixels[pos:pos+step]]
            self._pixels._pixels.show()
        #finish out ping pong
        while(pos<=self._pixels._num_pixels-step-1):
            pos = pos+step+1
            if(cleanup):
                self._pixels._pixels[pos:pos+step] = [(0, 0, 0) for aa in self._pixels._pixels[pos:pos+step]]
            else:
                self._pixels._pixels[pos:pos+step] = [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for aa in self._pixels._pixels[pos:pos+step]]
            self._pixels._pixels.show()
        self._pixels._pixels.show()
        
