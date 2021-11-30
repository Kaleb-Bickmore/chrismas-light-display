import time
import random
from Lights.Pixels import Pixels

class SolidGroupStrategy:
    def __init__(self):
        self._pixels = Pixels()

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        self._pixels.fill_left_side((255,0,0))
        self._pixels.fill_top_side((0,255,0))
        self._pixels.fill_right_side((0,0,255))
        self._pixels._pixels.show()
        time.sleep(1)
        flag = "left"
        while(t_end>=time.time()):
            for i in range(60,300,30):
                if flag == "left":
                    self._pixels.fill_left_side((255,0,0))
                    self._pixels.fill_top_side((0,255,0))
                    self._pixels.fill_right_side((0,0,255))
                    self._pixels._pixels.show()
                    flag = "top"
                    
                elif flag == "top":
                    self._pixels.fill_left_side((0,0,255))
                    self._pixels.fill_top_side((255,0,0))
                    self._pixels.fill_right_side((0,255,0))
                    self._pixels._pixels.show()
                    flag = "right"

                else:
                    self._pixels.fill_left_side((0,255,0))
                    self._pixels.fill_top_side((0,0,255))
                    self._pixels.fill_right_side((0,255,0))
                    self._pixels._pixels.show()
                    flag = "left"
                time.sleep(bps/i) 

                      


                


        
