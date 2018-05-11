"""

    _    ____ ___ ____    _____   _    _    ____  
   / \  / ___|_ _|  _ \  / / / \ | |  / \  |  _ \ 
  / _ \| |    | || | | |/ / /|  \| | / _ \ | |_) |
 / ___ \ |___ | || |_| / / / | |\  |/ ___ \|  __/ 
/_/   \_\____|___|____/_/_/  |_| \_/_/   \_\_|    



"""

import sys
sys.path.insert(0, '../ext/APA102_Pi')
import apa102
import time
import threading


# global variables
PIXEL_COUNT = 656
frame_delay = 0.05 # delay between calls to draw_screen

# locks
spi_lock = threading.Lock()

def draw_screen():
	with spi_lock:
		panel.rotate(positions=1)
		panel.show()

	draw_screen.loop_count += 1
	t = threading.Timer(frame_delay, draw_screen)
	t.start()


panel = apa102.APA102(
	num_led=PIXEL_COUNT,
	global_brightness=5,
	mosi=10,
	sclk=11,
	order='rbg')
	#max_speed_hz=1000000)

panel.clear_strip()
panel.show()


for i in range(PIXEL_COUNT):
	panel.set_pixel_rgb(i, panel.wheel((i*10) % 255))
	# TODO: alter wheel function to use modulo 255
	#panel.set_pixel_rgb(i, 0x00FF00)

draw_screen.loop_count = 0

t = threading.Timer(frame_delay, draw_screen)
t.start()

try:
	while draw_screen.loop_count < 5:
		pass

except KeyboardInterrupt:
	t.cancel()
	panel.clear_strip()
	panel.cleanup()





