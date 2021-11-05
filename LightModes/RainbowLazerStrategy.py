import time
import random
from Pixels import Pixels

class RainbowLazerStrategy:
    def __init__(self):
        self._pixels = Pixels()

    def explosion(self, bps):
        explosionStart = self._pixels._num_pixels-1
        self._pixels._pixels[explosionStart]= (255, 255, 255)
        self._pixels._pixels.show()
        time.sleep(bps/6000)
        i=1
        while(explosionStart-i>0):
            self._pixels._pixels[explosionStart-i]= (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self._pixels._pixels.show()
            time.sleep(bps/6000)
            i+=1

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        length = random.randint(5,20)
        pos = range(0, length)
        while t_end <= time.time():
            if(pos[0]>=self._pixels._num_pixels):
                pos = range(0, length)
            self._pixels._pixels.fill((0, 0, 0))
            self._pixels._pixels.show()
            pos = list(map(lambda a : a+1, pos))
            for i in pos:
                if(i < self._pixels._num_pixels):
                    self._pixels._pixels[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self._pixels._pixels.show()
            time.sleep(bps/6000)
        #finish out ping pong
        while(pos[0]!=self._pixels._num_pixels):
            self._pixels._pixels.fill((0, 0, 0))
            self._pixels._pixels.show()
            pos = list(map(lambda a : a+1, pos))
            for i in pos:
                if(i < self._pixels._num_pixels):
                    self._pixels._pixels[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self._pixels._pixels.show()
            time.sleep(bps/6000)
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        self.explosion(bps)
        
