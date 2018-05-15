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
		
		self.color = (color & 0xFFFFFF)
		self.life = life

	def __str__(self):
		return ("px=" + str(self.px) + " py=" + str(self.py) + " vx=" + str(self.vx) +\
		 	" vy=" + str(self.vy) + " life=" + str(self.life) + " color=" + hex(self.color))

	def __repr__(self):
		return self.__str__()

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
		self.list = []
		self.pulse_life=pulse_life
		self.pulse_count = 0

	def add_pulse(self, x, y, color):

		self.list.append(pulse(x, y, \
					np.random.randint(0, 3), np.random.randint(0, 3), \
					color, self.pulse_life))

		self.pulse_count += 1
		print(self.list)

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

			# check for boundary conditions
			# if pulse is out of boundaries of the matrix...
			if (pulse.px >= xmax) or (pulse.px < 0) or (pulse.py >= ymax) or (pulse.py < 0):
				print("removing, matrix bounds: ", pulse)
				self.list.remove(pulse)
				
			# if pulse is out of bounds of the hexagon...
			elif grid.grid[pulse.py, pulse.px, 3] == -1:
				print("removing, hexagon bounds: ", pulse)
				self.list.remove(pulse)
	
			elif pulse.life == 0:
				print("removing, life: ", pulse)
				self.list.remove(pulse)
		
		print(self.list)


