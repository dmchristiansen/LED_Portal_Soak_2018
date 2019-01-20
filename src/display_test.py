"""

Panel display test

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
frame_delay = 0.005 # delay between calls to draw_screen
max_brightness = 1


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
	max_speed_hz=4000000)

# pulse representation
pulse_list = pulse_list()

# internal representation of grid data
grid = grid(0x08, 0x08, 0x08)

# I2C interface to trellis keypads
matrix0 = Adafruit_Trellis.Adafruit_Trellis()
matrix1 = Adafruit_Trellis.Adafruit_Trellis()
keypad = Adafruit_Trellis.Adafruit_TrellisSet(matrix0, matrix1)
I2C_BUS = 1
numPads = 2
numKeys = numPads * 16
#keypad.begin((0x70, I2C_BUS))
keypad.begin((0x70, I2C_BUS), (0x71, I2C_BUS))





def main():

	
	with panel_lock:
		panel.clear_strip()
		panel.show()	
		for i in range(PIXEL_COUNT):
			panel.set_pixel_rgb(i, panel.wheel((i*10) % 255))
			# TODO: alter wheel function to use modulo 255

		panel.show()
	
	#t = threading.Timer(frame_delay, draw_screen, args=[panel, pulse_list, grid, \
	#	pulse_lock, grid_lock, panel_lock, spi_lock])
	#t.start()
	
	try:
		while True:
			time.sleep(0.3)
			panel.rotate(1)
			panel.show()

	except KeyboardInterrupt:
		print(" KB Int")
	
	finally:
		panel.clear_strip()
		panel.cleanup()

		for i in range(numKeys):
			keypad.clrLED(i)
		keypad.writeDisplay()

if __name__ == "__main__":
	main()


