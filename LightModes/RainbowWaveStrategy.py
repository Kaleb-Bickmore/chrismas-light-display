import time
from Lights.Pixels import Pixels
from datetime import datetime, timedelta


class RainbowWaveStrategy:
    def __init__(self):
        self._pixels = Pixels()
        pass


    def wheel(self, pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b)


    def rainbow_cycle(self, wait):
        for j in range(255):
            for i in range(self._pixels._num_pixels):
                pixel_index = (i * 256 // self._pixels._num_pixels) + j
                self._pixels._pixels[i] = self.wheel(pixel_index & 255)
            self._pixels._pixels.show()
            time.sleep(wait)

    def run(self, cycle_time, bps):
        t_end = time.time() + cycle_time
        # do whatever you do
        while t_end >= time.time():
            self._pixels._pixels.fill((255, 0, 0))
            self._pixels._pixels.show()
            time.sleep(1)
            self._pixels._pixels.fill((0, 255, 0))
            self._pixels._pixels.show()
            time.sleep(1)
            self._pixels._pixels.fill((0, 0, 255))
            self._pixels._pixels.show()
            time.sleep(1)
            self.rainbow_cycle(bps/6000)