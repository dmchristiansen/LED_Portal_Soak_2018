"""


"""

import numpy as np
import random

class pulse:
	def __init__(self, px, py, vx, vy, r, g, b, life):
		# position
		self.px = px 
		self.py = py
		# velocity
		self.vx = vx
		self.vy = vy
		
		self.r = r
		self.g = g
		self.b = b
		self.life = life

	def __str__(self):
		return ("px=" + str(self.px) + " py=" + str(self.py) + " vx=" + str(self.vx) +\
		 	" vy=" + str(self.vy) + " life=" + str(self.life))
			 #\+ " color=" + hex(int(self.r << 16 + self.g << 8 + self.b)))

	def __repr__(self):
		return self.__str__()

class pulse_list:
	"""
	Class tracks pulses of light that move around the grid
	Maintains a list of pulse objects
	Each object  tracks:
		position (x, y)
		velocity (x, y)
		r, g, b
		lifespan (maybe?)
	"""


	def __init__(self, pulse_life=10):
		self.list = []
		self.pulse_life=pulse_life
		self.pulse_count = 0

	def add_pulse(self, px, py, vx, vy, r, g, b):

		self.list.append(pulse(px, py, vx, vy, r, g, b, self.pulse_life))

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
			elif grid.grid[pulse.py, pulse.px, grid.index] == -1:
				print("removing, hexagon bounds: ", pulse)
				self.list.remove(pulse)
	
			elif pulse.life == 0:
				print("removing, life: ", pulse)
				self.list.remove(pulse)
		
		print(self.list)


