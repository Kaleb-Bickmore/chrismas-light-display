import time
import random
from Pixels import Pixels

class ReactiveStrategy:
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
            length = int(random.randint(int(self._pixels._num_pixels/4),self._pixels._num_pixels-10)/2)
            middle_position = int(self._pixels._num_pixels/2)-1
            step = 5
            for i in range(0, length, step):
                self._pixels._pixels[middle_position-i-step: middle_position-i] = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for aa in self._pixels._pixels[middle_position-i-step: middle_position-i]]
                self._pixels._pixels[middle_position+i : middle_position+i+step] = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for aa in self._pixels._pixels[middle_position+i : middle_position+i+step]]
                self._pixels._pixels.show()
            for i in range(length,step+1,-1*step):
                self._pixels._pixels[middle_position-i : middle_position-i +step ] = [(0,0,0) for aa in self._pixels._pixels[middle_position-i : middle_position-i +step]]
                self._pixels._pixels[middle_position+i -step: middle_position+i ] = [(0,0,0) for aa in self._pixels._pixels[middle_position+i -step: middle_position+i]]
                self._pixels._pixels.show()


                      


                


        
