import time
import random
from Lights.Pixels import Pixels

class LastChristmasStrategy:
    song_timing = {
        "intro": 17,
        "chorus": 33
            }
    def __init__(self):
        self._pixels = Pixels()
    def intro(self):
        for i in range(16):   
            self._pixels.fill_left_side((0,255,0))
            self._pixels._pixels.show()
            time.sleep(.1)
            self._pixels.fill_left_side((0,0,0))
            self._pixels._pixels.show()
            time.sleep(.1)

        for i in range(16):   
            self._pixels.fill_right_side((255,0,0))
            self._pixels._pixels.show()
            time.sleep(.1)
            self._pixels.fill_right_side((0,0,0))
            self._pixels._pixels.show()
            time.sleep(.1)

        for i in range(16):   
            self._pixels._pixels.fill((0,0,0))
            self._pixels.fill_left_side((0,255,0))
            self._pixels._pixels.show()
            time.sleep(.1)
            self._pixels._pixels.fill((0,0,0))
            self._pixels.fill_right_side((255,0,0))
            self._pixels._pixels.show()
            time.sleep(.1)

        for i in range(16):   
            self._pixels.fill_right_side((255,0,0))
            self._pixels.fill_left_side((0,255,0))
            self._pixels.fill_top_side((0,0,255))
            self._pixels._pixels.show()
            time.sleep(.1)
            self._pixels._pixels.fill((0,0,0))
            self._pixels._pixels.show()
            time.sleep(.1)

    def chorus(self):
        self._pixels._pixels.fill((0,0,0))
        self._pixels.fill_group("left-pillar", (255,255,255))
        self._pixels._pixels.show()
        time.sleep(.6)
        self._pixels.fill_group("right-pillar", (255,255,255))
        self._pixels._pixels.show()
        time.sleep(.6)
        self._pixels._pixels.fill((0,0,0))
        self._pixels._pixels.fill((0,255,0))
        self._pixels.fill_group("left-pillar", (255,255,255))
        self._pixels.fill_group("right-pillar", (255,255,255))
        time.sleep(.4)
        offset = 0
        for i in range(50):
            for j in range(self._pixels._num_pixels):
                if((j+offset)%3==0):
                    self._pixels._pixels[j] = (0,0,0)
                if((j+offset)%3==1):
                    self._pixels._pixels[j] = (0,255,0)
                if((j+offset)%3==2):
                    self._pixels._pixels[j] = (255,255,255)
            offset +=1
            self._pixels._pixels.show()
            time.sleep(.1)
        self._pixels._pixels.fill((0,0,0))
        self._pixels.fill_group("left-pillar", (255,255,255))
        self._pixels.fill_group("right-pillar", (255,255,255))
        self._pixels._pixels.show()
        time.sleep(.6)
        self._pixels._pixels.fill((0,0,0))
        self._pixels._pixels.fill((255,0,0))
        self._pixels.fill_group("left-pillar", (255,255,255))
        self._pixels.fill_group("right-pillar", (255,255,255))
        self._pixels._pixels.show()
        time.sleep(.6)
        offset = 0
        for i in range(50):
            for j in range(self._pixels._num_pixels):
                if((j+offset)%3==0):
                    self._pixels._pixels[j] = (0,0,0)
                if((j+offset)%3==1):
                    self._pixels._pixels[j] = (255,0,0)
                if((j+offset)%3==2):
                    self._pixels._pixels[j] = (255,255,255)
            offset +=1
            self._pixels._pixels.show()
            time.sleep(.1)
                

    def chorus2(self):
        pass
    
    def run(self, cycle_time, bps):
        self.intro()
        self.chorus()
        self.chorus()
        self.chorus2()


                      


                


        
