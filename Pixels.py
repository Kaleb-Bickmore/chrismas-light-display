import board
import neopixel
class Pixels():
    def __init__(self):
        # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18 not working
        # NeoPixels must be connected to D10, D12, D18? or D21 to work.
        self._pixel_pin = board.D21
        self._num_pixels = 700
        self._pixels = neopixel.NeoPixel(self._pixel_pin, self._num_pixels, brightness=1, auto_write=False, pixel_order=neopixel.GRB)
    def turn_off(self):
        self._pixels.fill((0, 0, 0))
        self._pixels.show()
