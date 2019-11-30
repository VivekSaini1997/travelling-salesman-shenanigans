'''	ok this is 2opt but slightly better lmao
	it is known as simulated annealing (it sounds kind of funny)
	uses more random swapping to avoid local minima'''

import graphics as g
import numpy as np
import math
import time
import random
from .tsp_2_opt import *

# called tsp_sa as the sa stands for simulated annealing
class tsp_sa(tsp_2_opt):
	"""docstring for tsp_sa"""
	# called sa_time because two_opt time doesn't make much sense
	def __init__(self, pts, screen_res, sa_time = 30):
		super(tsp_sa, self).__init__(pts, screen_res, sa_time, True)
		# set an initial temperature for the system,
		# in range 0 to 1, 0 becomes 2-opt, 1 allows for always swapping
		# initially, values in between allow for more or less randomness
		initial_temp = 0.8
		# using an exponential model, k is a paremeter instead
		k = -4 * math.log(10)
		# this is the loop equivalent to 2opt
		# pass in shrinking values of temp to simulate annealing that vary with 
		# the remaining time
		start_time = float(time.clock())
		curr_time = float(time.clock())
		while curr_time - start_time < self.algo_time:
			# the temperature calculation, it's linear for now
			# slightly innacurate but that's ok
			temp = (curr_time - start_time)/self.algo_time
			# jk its exponential with a slight bias factor so the temperature goes to "zero"
			temp = math.exp(k * temp) - 0.01
			# the actual simulated annealing
			self.simulate_annealing(temp)
			# update the current time so you know to exit
			curr_time = float(time.clock())

		# finally draw the solution
		self.draw_solution()


	# does the simulated annealing
	# it's not that different from 2-opt, really
	# temp is a value normalized between 0 and 1 that is used to determine whether or not a swap is to be made
	# starts high and goes low
	def simulate_annealing(self, temp):
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
		# otherwise, swap randomly with probability temp
		# temp starts high then goes low gradually
		else:
			chance = np.random.random_sample()
			# the name is isn't that good, you want chance to be low
			if chance < temp:
				self.path = p_path
				self.cost = p_cost				

