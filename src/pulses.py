"""


"""

import numpy as np
import random

class pulse:
	def __init__(self, px, py, vx, vy, color, life):
		# position
		self.px = px 
		self.py = py
		# velocity
		self.vx = vx
		self.vy = vy
		
		self.color = color
		self.life = life

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
		self.list = np.empty((0, 1), dtype=pulse)
		self.pulse_life=pulse_life

	def add_pulse(self, x, y, color):

		new_pulse = pulse(x, y, \
					np.random.randint(0, 3), np.random.randint(0, 3), \
					color, self.pulse_life)

		self.list = np.append(self.list, new_pulse)


	def move_pulses(self, grid):
		# bounds of grid
		ymax = grid.grid.shape[0]
		xmax = grid.grid.shape[1]

		# check for collisions

		# destroy pulses

		# move pulses	
		for pulse in self.list:
			pulse.px += pulse.vx
			pulse.py += pulse.vy

		for pulse in self.list:
			# check for boundary conditions
			# if pulse is out of boundaries of the matrix...
			if (pulse.px >= xmax) or (pulse.px < 0) or (pulse.py >= ymax) or (pulse.py < 0):
				pulse.life = 0
			# if pulse is out of bounds of the hexagon...
			if grid.grid[pulse.px, pulse.py, 3] == -1:
				pulse.life = 0 
	
		# clean pulse list
		for i in range(self.list.shape[0]):
			if self.list[i].life == 0:
				self.list = np.delete(self.list, i)




