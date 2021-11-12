from _typeshed import Self
import time
import random
from datetime import datetime, timedelta
from Pixels import Pixels

class RainbowLazerStrategy:
    def __init__(self):
        self._pixels = Pixels()
    def explosion(self, bps):
        explosionStart = self._pixels._num_pixels-1
        self._pixels._pixels[explosionStart]= (255, 255, 255)
        self._pixels._pixels.show()
        i=1
        while(explosionStart-i>0):
            self._pixels._pixels[explosionStart-i]= (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self._pixels._pixels.show()
            i+=1

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        pos = 0
        cleanup = False;
        while t_end >= time.time():
            if(pos == self._pixels._num_pixels-1):
                pos = 0
                cleanup = True
            pos = pos+1
            if(cleanup):
                self._pixels._pixels[pos] = (0, 0, 0)
            else:
                self._pixels._pixels[pos] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self._pixels._pixels.show()
        #finish out ping pong
        while(pos[0]!=self._pixels._num_pixels-1):
            pos = pos+1
            if(cleanup):
                self._pixels._pixels[pos] = (0, 0, 0)
            else:
                self._pixels._pixels[pos] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self._pixels._pixels.show()
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        self.explosion(bps)
        
