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

# global variables
PIXEL_COUNT = 656
frame_delay = 0.05 # delay between calls to draw_screen
max_brightness = 1


# locks
spi_lock = threading.Lock()
pulse_lock = threading.Lock()
grid_lock = threading.Lock()
panel_lock = threading.Lock()

# define led array object (actually sk9822 leds)
panel = apa102.APA102(
	num_led=PIXEL_COUNT,
	global_brightness=max_brightness,
	mosi=10,
	sclk=11,
	order='rbg')
	#max_speed_hz=1000000)

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



def draw_screen():
	
	# move pulses
	pulse_list.move_pulses()	

	# update pixel array values
	

	# redraw screen
	with spi_lock:
		
		panel.rotate(positions=1)
		panel.show()

	# re-arm frame timer
	t = threading.Timer(frame_delay, draw_screen)
	t.start()




def main():

	panel.clear_strip()
	panel.show()
	
	
	for i in range(PIXEL_COUNT):
		panel.set_pixel_rgb(i, panel.wheel((i*10) % 255))
		# TODO: alter wheel function to use modulo 255
	
	draw_screen.loop_count = 0
	
	t = threading.Timer(frame_delay, draw_screen)
	t.start()
	
	try:
		while True:
			time.sleep(0.03)
			if keypad.readSwitches():
				for i in range(numKeys):
					if keypad.justPressed(i):
						print('v{0}'.format(i))
						panel.rotate(positions=5) # for testing...
						pulse_list.add_pulse(1, 2, panel.wheel(random.randint(0, 10)*10 % 255))	

	except KeyboardInterrupt:
		print(" KB Int")
	
	finally:
		t.cancel()
		panel.clear_strip()
		panel.cleanup()

		

if __name__ == "__main__":
	main()


