from datetime import datetime, timedelta
import random
import time
from Pixels import Pixels

class PingPongStrategy:
    def __init__(self):
        self._pixels = Pixels()

    def explosion(self, bps):
        explosionStart = int(self._pixels._num_pixels/2)
        self._pixels._pixels[explosionStart]= (255, 255, 255)
        self._pixels._pixels.show()
        time.sleep(bps/6000)
        i=1
        while(explosionStart+i<self._pixels._num_pixels and explosionStart-i>0):
            self._pixels._pixels[explosionStart+i]= (255, 255, 255)
            self._pixels._pixels[explosionStart-i]= (255, 255, 255)
            self._pixels._pixels.show()
            time.sleep(bps/6000)
            i+=1

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        length = random.randint(1,10)
        step = random.randint(1,3)
        pos = range(0, length, step)
        decrementing = False
        while t_end >= time.time():
            self._pixels._pixels.fill((0, 0, 0))
            self._pixels._pixels.show()
            if(pos[len(pos)-1] == self._pixels._num_pixels-1):
                decrementing = True
            if(pos[0] == 0):
                decrementing = False
            if(decrementing):
                pos = list(map(lambda a : a-1, pos))
            else:
                pos = list(map(lambda a : a+1, pos))
            for i in pos:
                self._pixels._pixels[i] = (255, 255, 255)
            self._pixels._pixels.show()
            time.sleep(bps/6000)
        #finish out ping pong
        while(pos[0]!=0 and pos[len(pos)-1] != self._pixels._num_pixels-1):
            self._pixels._pixels.fill((0, 0, 0))
            self._pixels._pixels.show()
            if(decrementing):
                pos = list(map(lambda a : a-1, pos))
            else:
                pos = list(map(lambda a : a+1, pos))
            for i in pos:
                self._pixels._pixels[i] = (255, 255, 255)
            self._pixels._pixels.show()
            time.sleep(bps/6000)
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        self.explosion(bps)
        
