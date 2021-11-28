from math import pi
import time
import random
from Lights.Pixels import Pixels

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

        while(t_end>=time.time()):
            selectedIndexes = []
            incrementIndexes = []
            for _ in range(50):
                selectedIndexes.append(pixel_ids.pop(random.randint(0, len(pixel_ids)-1)))
            for _ in range(50):
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
                self._pixels._pixels[selectedIndexes[10]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[11]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[12]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[13]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[14]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[15]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[16]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[17]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[18]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[19]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[20]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[21]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[22]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[23]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[24]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[25]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[26]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[27]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[28]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[29]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[30]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[31]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[32]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[33]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[34]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[35]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[36]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[37]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[38]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[39]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[40]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[41]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[42]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[43]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[44]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[45]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[46]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[47]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[48]] = (i,0,i)
                self._pixels._pixels[selectedIndexes[49]] = (i,0,i)
             
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
                self._pixels._pixels[incrementIndexes[10]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[11]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[12]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[13]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[14]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[15]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[16]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[17]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[18]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[19]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[20]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[21]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[22]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[23]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[24]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[25]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[26]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[27]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[28]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[29]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[30]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[31]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[32]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[33]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[34]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[35]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[36]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[37]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[38]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[39]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[40]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[41]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[42]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[43]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[44]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[45]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[46]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[47]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[48]] = (255-i,0,255-i)
                self._pixels._pixels[incrementIndexes[49]] = (255-i,0,255-i)
               
                self._pixels._pixels.show()
                   


                


        
