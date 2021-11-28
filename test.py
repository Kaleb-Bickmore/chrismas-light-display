import time
from MusicPlayer import MusicPlayer
import time
from Pixels import Pixels

if __name__== "__main__" :
	pixels = Pixels()
	for i in range(687, pixels._num_pixels):
		pixels._pixels.fill((0,0,0))
		pixels._pixels[i] = (255,255,255)
		pixels._pixels.show()
		print(i)
		time.sleep(1)

