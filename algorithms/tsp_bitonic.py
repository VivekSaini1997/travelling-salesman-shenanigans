''' implements a bitonic tour from CLRS
	uses dynamic programming to produce a semi optimal path in
	O(n^2) time '''

import graphics as g
import numpy as np
import math
import time
import random
from .tsp_map import *

# function to get the x value of a pt index tuple
def get_x(pt_tuple):
	return pt_tuple[0].x

# the bitonic tour class
class tsp_bitonic(tsp_map):
	"""docstring for tsp_bitonic"""
	def __init__(self, pts, screen_res):
		super(tsp_bitonic, self).__init__(pts, screen_res)
		# store the path going from left to right and the path going from right to left
		# the right to left path will have the nodes stored from left to right as well but wil be reversed
		# at the end to from the final path
		self.rl_path = np.array([])
		self.lr_path = np.array([])

		# also store the best costs of going left to right and left to right assuming the 
		# path only consists of the index plus one pts sorted from the left to right
		self.rl_cost = np.zeros(len(self.pts))
		self.lr_cost = np.zeros(len(self.pts))	
		# sort the array from left to right
		self.sorted_pts = np.array(sorted([ (self.pts[k], k) for k in range(len(self.pts)) ], key=get_x))

		#self.draw_solution()

	# generate the bitonic tour given the sorted pts
	def generate_bitonic_tour(self):
		# in the case of only the left most point, the costs are zero and the path is just that point
		self.rl_cost[]