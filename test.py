import time
from Pixels import Pixels

if __name__== "__main__" :
    pixels = Pixels()
    pixels._pixels.fill((255,255,255))
    pixels._pixels.show()
    time.sleep(5)
    pixels.turn_off()

