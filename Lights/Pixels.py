import board
import neopixel
from random import randint
class Pixels():
    _pixel_pin = board.D21
    _num_pixels = 700
    _pixels = neopixel.NeoPixel(_pixel_pin, _num_pixels, brightness=1, auto_write=False, pixel_order=neopixel.GRB)
    _groups = {
            "left-pillar" : (0,66),
            "space-between-pillar" : (67,121),
            "right-pillar" : (122,186),
            "right-pillar-to-door-corner" : (187,213),
            "door-corner-to-garage-corner" : (214,258),
            "top-left-main-garage-top-right-main-garage" : (259,343),
            "top-dead-space" : (344,349),
            "top-left-side-garage-top-right-side-garage" : (350,397),
            "top-right-corner-to-bottom" : (398,435),
            "bottom-corner-to-side-garage" : (436,441),
            "right-side-garage" : (442,471),
            "top-side-garage" : (472,503),
            "left-side-garage" : (504,519),
            "space-between-garages" : (520,543),
            "right-main-garage" : (544,559),
            "top-main-garage" : (560,615),
            "left-main-garage" : (616,631),
            "l-to-top-right-corner" : (632,659),
            "archway" : (660,686),
            "candy-cane" : (687,699)}
    def __init__(self):
        pass
        # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18 not working
        # NeoPixels must be connected to D10, D12, D18? or D21 to work.
        
    def turn_off(self):
        self._pixels.fill((0, 0, 0))
        self._pixels.show()
        
    def fill_groups(self, groups, color=(randint(0,255),randint(0,255),randint(0,255))):
        for group in groups:
            (start_index,end_index) = self._groups[group]
            self._pixels[start_index: end_index] = [color for aa in self._pixels[start_index: end_index]]
        self._pixels.show()
    
    def fill_group(self, group, color=(randint(0,255),randint(0,255),randint(0,255))):
        (start_index,end_index) = self._groups[group]
        self._pixels[start_index: end_index] = [color for aa in self._pixels[start_index: end_index]]
        self._pixels.show()

    def get_all_groups(self):
        return self._groups.keys()