''' this file is intended to implement two opt swapping for a map '''

import graphics as g
import numpy as np
import math
import time
import random
from .tsp_map import *

# the class responsible for an algorithm which randomly 2-opts
class tsp_2_opt(tsp_map):
	"""docstring for tsp_2-opt"""
	def __init__(self, pts, screen_res, two_opt_time = 30, parent = False):
		super(tsp_2_opt, self).__init__(pts, screen_res)
		# the time to 2opt for
		# this function becomes much more powerful in a performant language 
		self.algo_time = two_opt_time
		# generate a random solution, this is a WIP
		# i suppose going in order is random enough considering the points
		# are generated randomly
		self.path = np.array(range(len(pts)))
		# get a starting benchmark for the cost to be improved upon
		self.cost = self.get_path_cost(self.path)
		# only do the following if the class is not a parent class
		# i.e don't do it if you wanna do simulated annealing
		if parent == False:
			# time.clock fetches the current time in seconds?
			# so the following does do_opt for time seconds that i know for sure
			start_time = float(time.clock())
			while float(time.clock()) - start_time < self.algo_time:
				self.do_opt()
			self.draw_solution()


	# does the two opt swap and possible change if the computed cost of the path is lower
	# called this because it rhymes with two-opt hehe
	def do_opt(self):
		# pick two points and swap them and see what the resulting path it
		# the p in p_path stands for potential
		a = np.random.randint(0, len(self.path))
		b = np.random.randint(0, len(self.path))
		p_path = swap_and_reverse(self.path, a, b)
		# get the potential cost
		p_cost = self.get_path_cost(p_path)
		# if that cost is lower than the current path's cost, change the path
		# this could be optimized
		if p_cost < self.cost:
			self.path = p_path
			self.cost = p_cost

	''' this function might be abandoned '''
	# takes in two points, a and b, and returns the cost of the path between them if edges
	# (a, a+1) and (b, b-1) are swapped so that they become (a, b-1) and (a+1, b)
	# might wanna redesign how the cost is being represented
	def compute_partial_path_cost(edge_a, edge_b):
		# the cost starts at 0
		cost = 0
		# the partial path is the path from a to b
		p_path = get_circular_range(self.path, edge_a, edge_b)
		# go through all of the edges and add their costs
		# assumes the path is acyclic 
		for elem in range(len(path) - 1):
			pass