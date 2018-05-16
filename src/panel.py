"""

    _    ____ ___ ____    _____   _    _    ____  
   / \  / ___|_ _|  _ \  / / / \ | |  / \  |  _ \ 
  / _ \| |    | || | | |/ / /|  \| | / _ \ | |_) |
 / ___ \ |___ | || |_| / / / | |\  |/ ___ \|  __/ 
/_/   \_\____|___|____/_/_/  |_| \_/_/   \_\_|    



"""

import sys
import random
sys.path.insert(0, '../ext/APA102_Pi')
import apa102
import time
import threading
from grid import grid
from pulses import pulse_list
import RPi.GPIO as GPIO
import Adafruit_Trellis
import numpy as np

# global variables
PIXEL_COUNT = 656
frame_delay = 0.01 # delay between calls to draw_screen
max_brightness = 5


# locks - acquire in this order!
pulse_lock = threading.Lock()
grid_lock = threading.Lock()
panel_lock = threading.Lock()
spi_lock = threading.Lock()

# define led array object (actually sk9822 leds)
panel = apa102.APA102(
	num_led=PIXEL_COUNT,
	global_brightness=max_brightness,
	mosi=10,
	sclk=11,
	order='rbg',
	max_speed_hz=8000000)

# pulse representation
pulse_list = pulse_list()

# internal representation of grid data
grid = grid()

# I2C interface to trellis keypads
matrix0 = Adafruit_Trellis.Adafruit_Trellis()
keypad = Adafruit_Trellis.Adafruit_TrellisSet(matrix0)
I2C_BUS = 1
numPads = 1
numKeys = numPads * 16
keypad.begin((0x70, I2C_BUS))
#keypad.begin((0x70, I2C_BUS), (0x71, I2C_BUS))



def draw_screen(panel, pulse_list, grid, pulse_lock, grid_lock, panel_lock, spi_lock):

	# move pulses
	with pulse_lock:
		pulse_list.move_pulses(grid)	

	# update grid information
	with pulse_lock:
		with grid_lock:
			grid.update_color_state(pulse_list)

	# update pixel array values
	with grid_lock:
		with panel_lock:
			grid.update_color_array(panel)

	# redraw screen
	with panel_lock:
		with spi_lock:	
			panel.show()

	# re-arm frame timer
	t = threading.Timer(frame_delay, draw_screen, args=[panel, pulse_list, grid, \
		pulse_lock, grid_lock, panel_lock, spi_lock])
	t.start()




def main():

	# values for pulse initialization
	# each button's number is the index into the arrays to get it's data
	#y = [2, 5, 8, 11, 14, 16, 19, 22, 25, 2, 5, 8, 11, 14, 16, 19, 22, 25]
	#x = [9, 7, 5, 3, 3, 5, 7, 9, 23, 25, 27, 29, 29, 27, 25, 23]
	px = [8, 7, 6, 6, 5, 4, 4, 3, 3, 4, 4, 5, 6, 6, 7, 8]
	py = [3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23, 24]
	vxmin = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	vxmax = [4, 4, 4, 4, 4, 4, 4, 4 ,4, 4, 4, 4, 4, 4, 4, 4]
	vymin = [0, 0, 0, 0, 0, 0, 0, 0, -3, -3, -3, -3, -3, -3, -3, -3]
	vymax = [3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0] 

	with panel_lock:
		panel.clear_strip()
		panel.show()	
		for i in range(PIXEL_COUNT):
			panel.set_pixel_rgb(i, 0xF0F0F0)
			#panel.set_pixel_rgb(i, panel.wheel((i*10) % 255))
			# TODO: alter wheel function to use modulo 255

		panel.show()
	
	t = threading.Timer(frame_delay, draw_screen, args=[panel, pulse_list, grid, \
		pulse_lock, grid_lock, panel_lock, spi_lock])
	t.start()
	
	try:
		while True:
			time.sleep(0.03)
			if keypad.readSwitches():
				for i in range(numKeys):
					if keypad.justPressed(i):
						print('v{0}'.format(i))
						with pulse_lock:
							pulse_list.add_pulse(px[i], py[i],\
								np.random.randint(vxmin[i], vxmax[i]),\
								np.random.randint(vymin[i], vymax[i]),\
								(i * 15), (255 - (i * 15)), ((i % 4) * 20))	

	except KeyboardInterrupt:
		print(" KB Int")
	
	finally:
		t.cancel()
		panel.clear_strip()
		panel.cleanup()

		

if __name__ == "__main__":
	main()


