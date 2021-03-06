"""

 This file contains definition of the self.grid representing the pixels of the panel.
 Since the panel is a hexagon, but pulses moving across the panel is easier to
 track with a 2D array, I've chosen to represent the self.grid with a 2D array,
 with information for how it's mapped to the pixel array.

 TODO:


 QUESTIONS
 - Background color other than off?
 - 


"""

import numpy as np

class grid:


	# constants


	
	def __init__(self, br, bg, bb):

		# grid data indices
		self.cr    = 0
		self.cg    = 1
		self.cb    = 2
		self.tr    = 3
		self.tg    = 4
		self.tb    = 5
		self.type  = 6
		self.index = 7

		# (row, column, pixel info)
		# pixel info = [current (r,g,b), target (r,g,b), pixel type, array index]
		# pixel type: 0-> invalid, 1->valid
		# array index: 0+ are valid indices, -1 means invalid
		self.grid = np.zeros((28, 32, 8), dtype=int)
		self.background_r = br
		self.background_g = bg
		self.background_b = bb

		# fill in self.grid borders
		self.grid[0, np.r_[0:9, 23:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 16	
		self.grid[1, np.r_[0:9, 23:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 16
		self.grid[2, np.r_[0:8, 24:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 18
		self.grid[3, np.r_[0:8, 24:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 18
		self.grid[4, np.r_[0:7, 25:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 20
		self.grid[5, np.r_[0:6, 26:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 22
		self.grid[6, np.r_[0:6, 26:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 22	
		self.grid[7, np.r_[0:5, 27:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 24
		self.grid[8, np.r_[0:4, 28:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 26
		self.grid[9, np.r_[0:4, 28:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 26
		self.grid[10, np.r_[0:3, 29:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 28
		self.grid[11, np.r_[0:2, 30:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 30
		self.grid[12, np.r_[0:2, 30:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 30
		self.grid[13, np.r_[0:1, 31:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 32
		self.grid[14, np.r_[0:1, 31:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 32
		self.grid[15, np.r_[0:2, 30:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 30
		self.grid[16, np.r_[0:2, 30:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 30
		self.grid[17, np.r_[0:3, 29:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 28
		self.grid[18, np.r_[0:4, 28:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 26
		self.grid[19, np.r_[0:4, 28:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 26
		self.grid[20, np.r_[0:5, 27:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 24
		self.grid[21, np.r_[0:6, 26:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 22
		self.grid[22, np.r_[0:6, 26:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 22
		self.grid[23, np.r_[0:7, 25:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 20
		self.grid[24, np.r_[0:8, 24:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 18
		self.grid[25, np.r_[0:8, 24:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 18
		self.grid[26, np.r_[0:9, 23:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 16	
		self.grid[27, np.r_[0:9, 23:32]] = [0, 0, 0, 0, 0, 0, 0, -1] # 16
		
		# fill in array indices
		self.grid[0, 8:24, 7] = np.arange(0, 16, dtype=int)
		self.grid[1, 8:24, 7] = np.arange(16, 32, dtype=int)
		self.grid[2, 7:25, 7] = np.arange(32, 50, dtype=int)
		self.grid[3, 7:25, 7] = np.arange(50, 68, dtype=int)
		self.grid[4, 6:26, 7] = np.arange(68, 88, dtype=int)
		self.grid[5, 5:27, 7] = np.arange(88, 110, dtype=int)
		self.grid[6, 5:27, 7] = np.arange(110, 132, dtype=int)
		self.grid[7, 4:28, 7] = np.arange(132, 156, dtype=int)
		self.grid[8, 3:29, 7] = np.arange(156, 182, dtype=int)
		self.grid[9, 3:29, 7] = np.arange(182, 208, dtype=int)
		self.grid[10, 2:30, 7] = np.arange(208, 236, dtype=int)
		self.grid[11, 1:31, 7] = np.arange(236, 266, dtype=int)
		self.grid[12, 1:31, 7] = np.arange(266, 296, dtype=int)
		self.grid[13, 0:32, 7] = np.arange(296, 328, dtype=int)
		self.grid[14, 0:32, 7] = np.arange(328, 360, dtype=int)
		self.grid[15, 1:31, 7] = np.arange(360, 390, dtype=int)
		self.grid[16, 1:31, 7] = np.arange(390, 420, dtype=int)
		self.grid[17, 2:30, 7] = np.arange(420, 448, dtype=int)
		self.grid[18, 3:29, 7] = np.arange(448, 474, dtype=int)
		self.grid[19, 3:29, 7] = np.arange(474, 500, dtype=int)
		self.grid[20, 4:28, 7] = np.arange(500, 524, dtype=int)
		self.grid[21, 5:27, 7] = np.arange(524, 546, dtype=int)
		self.grid[22, 5:27, 7] = np.arange(546, 568, dtype=int)
		self.grid[23, 6:26, 7] = np.arange(568, 588, dtype=int)
		self.grid[24, 7:25, 7] = np.arange(588, 606, dtype=int)
		self.grid[25, 7:25, 7] = np.arange(606, 624, dtype=int)
		self.grid[26, 8:24, 7] = np.arange(624, 640, dtype=int)
		self.grid[27, 8:24, 7] = np.arange(640, 656, dtype=int)

		# set background color
		for r in range(self.grid.shape[0]):
			for c in range(self.grid.shape[1]):
				self.grid[r, c, self.tr] = self.background_r 
				self.grid[r, c, self.tg] = self.background_g
				self.grid[r, c, self.tb] = self.background_b

	def interpolate(self, current, target):
		fade_val = 10

		diff = target - current
		if diff < -1*fade_val:
			return current - fade_val
		elif diff > fade_val:
			return current + fade_val
		else:
			return target

	def update_color_state(self, pulse_list):
		"""
		Updates current color values based on pulse location and previous colors
		Fades between current color and target color
		Sets current color based ob pulse location
		"""
		
		for r in range(self.grid.shape[0]):
			for c in range(self.grid.shape[1]):
				if self.grid[r, c, self.index] != -1:
					self.grid[r, c, self.cr] =\
						self.interpolate(self.grid[r, c, self.cr], self.grid[r, c, self.tr]) 
					self.grid[r, c, self.cg] =\
						self.interpolate(self.grid[r, c, self.cg], self.grid[r, c, self.tg])
					self.grid[r, c, self.cb] =\
						self.interpolate(self.grid[r, c, self.cb], self.grid[r, c, self.tb])		


		# change current grid colors under pixel
		for pulse in pulse_list.list:
			self.grid[pulse.py, pulse.px, self.cr:self.cb+1] = pulse.r, pulse.g, pulse.b

	def update_color_array(self, panel):
		"""
		Updates strip color values based on grid state
		"""
		
		for r in range(self.grid.shape[0]):
			for c in range(self.grid.shape[1]):
				if self.grid[r, c, self.index] != -1:
					panel.set_pixel(self.grid[r, c, self.index], int(self.grid[r, c, self.cr]),\
						int(self.grid[r, c, self.cg]), int(self.grid[r, c, self.cb]))


 
