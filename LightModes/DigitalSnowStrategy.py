from math import pi
import time
import random
from Pixels import Pixels

class DigitalSnowStrategy:
    def __init__(self):
        self._pixels = Pixels()

    def randomRG():
        if(random.randint(0,1)==0):
            return (255,0,0)
        else:
            return (0,255,0)
    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        pixel_ids = []
        for i in range(self._pixels._num_pixels):
            if(random.randint(0, 1) == 0):
                pixel_ids.append(i)
                self._pixels._pixels[i] = (255,0,255)
            else:
                self._pixels._pixels[i] = (0,0,0)
        self._pixels._pixels.show()
        time.sleep(bps/600)

        while(t_end>=time.time()):
            selectedIndexes = []
            incrementIndexes = []
            for _ in range(10):
                selectedIndexes.append(pixel_ids.pop(random.randint(0, len(pixel_ids)-1)))
            for _ in range(10):
                index = random.randint(0, self._pixels._num_pixels-1)
                while(index in pixel_ids):
                    index = random.randint(0, self._pixels._num_pixels-1)
                incrementIndexes.append(index)
            pixel_ids = pixel_ids + incrementIndexes                    

            for i in range(255,-5,-5):
                self._pixels._pixels[selectedIndexes[0]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[1]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[2]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[3]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[4]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[5]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[6]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[7]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[8]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[9]] = (i,0,i)
                self._pixels._pixels[incrementIndexes[0]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[1]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[2]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[3]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[4]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[5]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[6]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[7]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[8]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[9]] = (255-i,0,255-i)
                self._pixels._pixels.show()
            time.sleep(bps/6000)
                   


                


        
