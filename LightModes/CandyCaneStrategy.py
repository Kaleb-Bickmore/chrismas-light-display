import time
from Pixels import Pixels

class CandyCaneStrategy:
    def __init__(self):
        self._pixels = Pixels()

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        offset = False
        while(t_end>=time.time()):
            for i in range(0, self._pixels._num_pixels-1):
                if((i+int(offset))%2 == 0):
                    self._pixels._pixels[i] = (0, 255, 0)
                if((i+int(offset))%2 == 1):
                    self._pixels._pixels[i] = (255, 255, 255)
            self._pixels._pixels.show()
            offset = (not offset)
            time.sleep(bps/60) 

                      


                


        
