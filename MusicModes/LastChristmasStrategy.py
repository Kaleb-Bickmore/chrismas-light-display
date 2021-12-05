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
        time.sleep(.5)
        self._pixels._pixels.fill((0,255,0))
        self._pixels.fill_group("left-pillar", (255,255,255))
        self._pixels.fill_group("right-pillar", (255,255,255))
        self._pixels._pixels.show()
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
        self._pixels.fill_group("left-pillar", (255,0,0))
        self._pixels.fill_group("right-pillar", (255,0,0))
        self._pixels._pixels.show()
        time.sleep(.6)
        self._pixels._pixels.fill((0,255,0))
        self._pixels.fill_group("left-pillar", (255,0,0))
        self._pixels.fill_group("right-pillar", (255,0,0))
        self._pixels._pixels.show()
        time.sleep(.5)
        offset = 0
        for i in range(50):
            for j in range(self._pixels._num_pixels):
                if((j+offset)%3==0):
                    self._pixels._pixels[j] = (0,0,0)
                if((j+offset)%3==1):
                    self._pixels._pixels[j] = (255,0,0)
                if((j+offset)%3==2):
                    self._pixels._pixels[j] = (0,255,0)
            offset +=1
            self._pixels._pixels.show()
            time.sleep(.1)
                
    def explosion(self,index, length):
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for i in range(0,length,5):
            self._pixels._pixels[index : index+i] = [color for aa in self._pixels._pixels[index :  index+i]]
            self._pixels._pixels[index-i : index] = [color for aa in self._pixels._pixels[index-i : index]]
            self._pixels._pixels.show()

    def chorus2(self):
        self._pixels._pixels.fill((0,0,0))
        self._pixels._pixels.show()
        time.sleep(.6)
        self._pixels._pixels.fill((0,0,0))
        self.explosion(random.randint(100,600),80)
        time.sleep(.2)
        self._pixels._pixels.fill((0,0,0))
        self.explosion(random.randint(100,600),80)
        time.sleep(.1)
        self._pixels._pixels.fill((0,0,0))
        self.explosion(random.randint(100,600),80)
        time.sleep(1)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        time.sleep(2)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        time.sleep(2.5)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        time.sleep(3)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
        self.explosion(random.randint(100,600),50)
    
    def chorus3(self):
        pos = 0
        step = 5
        cleanup = False
        self._pixels._pixels.fill((0, 0, 0))
        self._pixels._pixels.show()
        for i in range(520):
            if(pos >= self._pixels._num_pixels-1):
                pos = 0
                if(cleanup):
                    cleanup = False
                else:
                    cleanup = True
            pos = pos+step+1
            if(cleanup):
                self._pixels._pixels[pos:pos+step] = [(0, 0, 0) for aa in self._pixels._pixels[pos:pos+step]]
            else:
                self._pixels._pixels[pos:pos+step] = [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for aa in self._pixels._pixels[pos:pos+step]]
            self._pixels._pixels.show()
    def chorus4(self):
        self._pixels._pixels.fill((255,0,0))
        self._pixels._pixels.show()
        time.sleep(.2)
        self._pixels._pixels.fill((0,255,0))
        self._pixels._pixels.show()
        time.sleep(.1) 
        self._pixels._pixels.fill((255,0,0))
        self._pixels._pixels.show()     
        self._pixels._pixels.fill((0,0,0))
        self._pixels._pixels.show()
        for i in range(10):   
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
    def run(self, cycle_time, bps):
        self._pixels._pixels.fill((0,0,0))
        time.sleep(.5)
        self.intro()
        self.chorus()
        self.chorus()
        self.chorus2()
        self.chorus3()
        self.chorus4()
        self.chorus()
        self.chorus()
        self.chorus2()
        self.chorus3()
        self.chorus4()
        time.sleep(.2)
        self.chorus()
        self.chorus()
        self.chorus2()
        self.chorus3()
        self._pixels._pixels.fill((0,0,0))
        self._pixels._pixels.show()
        




                      


                


        
