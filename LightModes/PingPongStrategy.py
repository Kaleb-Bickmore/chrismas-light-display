from datetime import datetime, timedelta
import random
import time
from Pixels import Pixels

class PingPongStrategy:
    def __init__(self):
        self._pixels = Pixels()
        self._rgw = [(255,0,0), (0,255,0), (255,255,255)]
    def explosion(self, bps):
        explosionStart = int(self._pixels._num_pixels/2)
        self._pixels._pixels[explosionStart]= self._rgw(explosionStart%3)
        self._pixels._pixels.show()
        i=1
        while(explosionStart+i<self._pixels._num_pixels and explosionStart-i>0):
            self._pixels._pixels[explosionStart+i]= self._rgw(explosionStart+i%3)
            self._pixels._pixels[explosionStart-i]= self._rgw(explosionStart+i%3)
            self._pixels._pixels.show()
            i+=1

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        length = random.randint(15,30)
        step = random.randint(3,5)
        pos = 0
        decrementing = False
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        while t_end >= time.time():
            if(pos == self._pixels._num_pixels-1):
                decrementing = True
            if(pos == 0):
                decrementing = False
            if(decrementing):
                pos = pos-1
                self._pixels._pixels[pos] = (0,0,0) 
            else:
                pos = pos+1
                self._pixels._pixels[pos] = self._rgw(pos%3) 
            self._pixels._pixels.show()
        #finish out ping pong
        while(pos[0]!=0 and pos[len(pos)-1] != self._pixels._num_pixels-1):
            if(pos == self._pixels._num_pixels-1):
                decrementing = True
            if(pos == 0):
                decrementing = False
            if(decrementing):
                pos = pos-1
                self._pixels._pixels[pos] = (0,0,0) 
            else:
                pos = pos+1
                self._pixels._pixels[pos] = self._rgw(pos%3) 
            self._pixels._pixels.show()
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        self.explosion(bps)
        
