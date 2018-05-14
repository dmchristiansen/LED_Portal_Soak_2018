"""


"""

import numpy as np
import random

class pulse_list:
	"""
	Class tracks pulses of light that move around the grid
	Maintains a list of pulse objects
	Each object  tracks:
		position (x, y)
		velocity (x, y)
		color
		lifespan (maybe?)
	"""


	def __init__(self, pulse_life=10):
		self.list = np.empty((0, 6), dtype=np.int)
		self.pulse_life=pulse_life

	def add_pulse(self, x, y, color):

		new_pulse = np.array([[x, y, \
					np.random.randint(0, high=3), np.random.randint(0, high=3), \
					color, self.pulse_life]])
		
		print(new_pulse.shape)
		self.list = np.append(self.list, new_pulse, axis=0)
		print("new pulse: ", new_pulse)
		print("pulse list: ", self.list)

	def move_pulses(self):
		pass	



