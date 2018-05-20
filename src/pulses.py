"""


"""

import numpy as np
import random
import math
import itertools

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
		self.age = 0

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


	def __init__(self, pulse_life=3):
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
		for pulse_1, pulse_2 in itertools.combinations(self.list, 2):
			if (((abs(pulse_1.px - pulse_2.px) < 2) or (abs(pulse_1.py - pulse_2.py) < 2)) and\
				(pulse_1.age > 1) and (pulse_2.age > 1) and\
				(((pulse_1.vx > 0) and (pulse_2.vx < 0)) or\
				((pulse_1.vx < 0) and (pulse_2.vx > 0)) or\
				((pulse_1.vy > 0) and (pulse_2.vy < 0)) or\
				((pulse_1.vy < 0) and (pulse_2.vy > 0)))):
				for i in range(0, math.floor((pulse_1.life + pulse_2.life) / 3)):
					if (i // 2) == 0:
						self.add_pulse(pulse_1.px, pulse_1.py,\
							np.random.randint(-3, 4), np.random.randint(-3, 4),\
							np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
					else:
						self.add_pulse(pulse_2.px, pulse_2.py,\
							np.random.randint(-3, 4), np.random.randint(-3, 4),\
							np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
									
				
				pulse_1.life = 0
				pulse_2.life = 0

		# destroy pulses

		# move pulses	
		for pulse in self.list:
			pulse.px += pulse.vx
			pulse.py += pulse.vy
			pulse.age += 1

			# check for boundary conditions
			# if pulse is out of boundaries of the matrix...
			if (pulse.px >= xmax) or (pulse.px < 0) or (pulse.py >= ymax) or (pulse.py < 0):
				if pulse.life > 0:	
					pulse.px -= pulse.vx
					pulse.py -= pulse.vy
					vx, vy = pulse.vx, pulse.vy
					if vx < 0:
						pulse.vx = abs(vy)
					else:
						pulse.vx = -1 * abs(vy)
					if vy < 0:
						pulse.vy = abs(vx)
					else:
						pulse.vy = -1 * abs(vx)
					pulse.life -= 1
				else:
					print("removing, matrix bounds: ", pulse)
					self.list.remove(pulse)
					self.pulse_count -= 1
					
			# if pulse is out of bounds of the hexagon...
			elif grid.grid[pulse.py, pulse.px, grid.index] == -1:
				if pulse.life > 0:	
					pulse.px -= pulse.vx
					pulse.py -= pulse.vy
					vx, vy = pulse.vx, pulse.vy
					if vx < 0:
						pulse.vx = abs(vy)
					else:
						pulse.vx = -1 * abs(vy)
					if vy < 0:
						pulse.vy = abs(vx)
					else:
						pulse.vy = -1 * abs(vx)
					pulse.life -= 1
				else:
					print("removing, hexagon bounds: ", pulse)
					self.list.remove(pulse)
					self.pulse_count -= 1
	
			elif pulse.life == 0:
				print("removing, life: ", pulse)
				self.list.remove(pulse)
				self.pulse_count -= 1
		
		print(self.list)


