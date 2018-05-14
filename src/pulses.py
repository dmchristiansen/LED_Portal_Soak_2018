"""


"""

import numpy as np
import random

class pulse_list:

	def __init__(self, pulse_life=10):
		self.list = np.empty()
		self.pulse_life=pulse_life

	def add_pulse(x, y, color):

		new_pulse = [x, y, color, random.randint(0, 3, dtype=np.int), random.randint(0, 3, dtype-np.int), \
			self.pulse_life] 
		self.list.append(new_pulse, axis=0)

	def move_pulses():
		
		for i in self.list[:, 0]
