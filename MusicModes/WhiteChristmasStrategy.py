import time
import random
from Lights.Pixels import Pixels

class WhiteChristmasStrategy:
    def __init__(self):
        self._pixels = Pixels()

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        while(t_end>=time.time()):
            for i in range(5) :
                self._pixels._pixels.fill((0, 0, 0))
                self._pixels.fill_group("left-pillar",(255,0,0))
                self._pixels._pixels.show()
                time.sleep(bps/60)
                self._pixels._pixels.fill((0, 0, 0))
                self._pixels.fill_group("right-pillar",(0,255,0))
                self._pixels._pixels.show()
                time.sleep(bps/60)
                self._pixels._pixels.fill((0, 0, 0))
                self._pixels.fill_group("top-main-garage",(0,0,255))
                self._pixels.fill_group("left-main-garage",(0,0,255))
                self._pixels.fill_group("right-main-garage",(0,0,255))
                self._pixels.fill_group("top-side-garage",(0,0,255))
                self._pixels.fill_group("left-side-garage",(0,0,255))
                self._pixels.fill_group("right-side-garage",(0,0,255))

                self._pixels._pixels.show()
                time.sleep(bps/60)
                self._pixels._pixels.fill((0, 0, 0))
                self._pixels.fill_left_side((255,0,0))
                self._pixels._pixels.show()
                time.sleep(bps/180)
                self._pixels._pixels.fill((0, 0, 0))
                self._pixels.fill_right_side((0,255,0))
                self._pixels._pixels.show()
                time.sleep(bps/180)
                self._pixels._pixels.fill((0, 0, 0))
                self._pixels.fill_top_side((0,0,255))
                self._pixels._pixels.show()
                time.sleep(bps/180)
                self._pixels._pixels.fill((0, 0, 0))
                self._pixels.fill_left_side((255,0,0))
                self._pixels.fill_right_side((0,255,0))
                self._pixels.fill_top_side((0,0,255))
                self._pixels._pixels.show()
                time.sleep(bps/60)

                      


                


        
