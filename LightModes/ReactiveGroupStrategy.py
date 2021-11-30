import time
import random
from Lights.Pixels import Pixels

class ReactiveGroupStrategy:
    def __init__(self):
        self._pixels = Pixels()

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        while(t_end>=time.time()):
            length = random.randint(4,11)*5
            for i in range(5,length,5):

                for group in self._pixels._groups:
                    (start_index,end_index) = self._pixels._groups[group]
                    temp_end_index = start_index+i
                    if (end_index-start_index)<i:
                        temp_end_index = end_index
                    color = (255,255,255)
                    if(group in self._pixels._top_sides):
                        color = (0,255,0)
                    self._pixels._pixels[temp_end_index-5:temp_end_index] = [color for aa in self._pixels._pixels[temp_end_index-5:temp_end_index]]
                self._pixels._pixels.show()
            for i in range(length,0,-5):

                for group in self._pixels._groups:
                    (start_index,end_index) = self._pixels._groups[group]
                    temp_end_index = start_index+i
                    if (end_index-start_index)<i:
                        temp_end_index = end_index-5
                    color = (0,0,0)
                    self._pixels._pixels[temp_end_index:temp_end_index+5] = [color for aa in self._pixels._pixels[temp_end_index:temp_end_index+5]]
                self._pixels._pixels.show()


                      


                


        
