import time
import random
from Pixels import Pixels

class ChasingLightsStrategy:
    def __init__(self):
        self._pixels = Pixels()

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        end = 0
        while(end != self._pixels._num_pixels-1):
            for j in range(end,0,-1):
                if((end-j)%4 == 0):
                    self._pixels._pixels[j] = (255, 255, 255)
                if((end-j)%4 == 1):
                    self._pixels._pixels[j] = (0,0,0)
                if((end-j)%4 == 2):
                    self._pixels._pixels[j] = (0,255,0)
                if((end-j)%4 == 3):
                    self._pixels._pixels[j] = (0,0,0)
            end+=1
            self._pixels._pixels.show()
            
        while(t_end>=time.time()):
            for i in range(0, self._pixels._num_pixels-1):
                if(i%4 == 0):
                    self._pixels._pixels[i] = (255, 255, 255)
                if(i%4 == 1):
                    self._pixels._pixels[i] = (0,0,0)
                if(i%4 == 2):
                    self._pixels._pixels[i] = (0,255,0)
                if(i%4 == 3):
                    self._pixels._pixels[i] = (0,0,0)
            self._pixels._pixels.show()
            time.sleep(bps/60) 

                      


                


        
