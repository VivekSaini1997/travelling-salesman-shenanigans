''' a subclass of tsp_map that implements a greedy algorithm
	to get a quick (and suboptimal) tsp solution
	it's a start lmao '''

import graphics as g
import numpy as np
import math
import time
from .tsp_map import *

# felt cute <3 might multi-start later
class tsp_greedy(tsp_map):
	"""docstring for tsp_greedy"""
	def __init__(self, pts, screen_res = None, start_idx = None, parent = False):
		super(tsp_greedy, self).__init__(pts, screen_res)
		# if this class isn't constucted from a child class, do the regular init
		# otherwise the child class will handle it
		if parent == False:
			if start_idx is None:
				start_idx = 0
			# generate and draw the greedy solution
			self.path, self.cost = self.generate_solution(start_idx)
			self.draw_solution()

	# given the index of a point in particular, get the closest unvisited point
	def get_next_destination(self, src_idx):
		point_possibilites = self.distances[src_idx]
		# unless we have a limit, the safest bet is to just use the max
		# not perfomant i am aware
		best_dist = max(point_possibilites)
		best_idx = -1
		# find the best unvisited point and return its index and cost
		for dst_idx in range(len(point_possibilites)):
			if self.visited[dst_idx] == 0 and point_possibilites[dst_idx] <= best_dist:
				best_dist = point_possibilites[dst_idx]
				best_idx = dst_idx
		return best_idx, best_dist

	# generates a greedy solution using the starting index provided
	# returns the path and the cost of said path in that order
	def generate_solution(self, start_idx):
		# set the initial point to be the starting index, i.e. the first vertex in the path
		prev_pt = start_idx
		# set the initial cost to zero
		cost = 0
		# allocate an array for the path, set it to be empty except for the first entry which is the 
		# starting point and create a counter to denote the last element accessed
		path = np.empty(len(self.pts)).astype(int)
		path[0] = start_idx
		counter = 1
		# set a visited array to be all zeros except for the start index
		self.visited = np.zeros(len(self.pts))
		self.visited[start_idx] = 1
		# while the solution path doesn't contain all of the verticies, generate the next vertex
		# using the nearest valid one and continue
		while counter < len(self.pts):
			# get the next point
			next_pt, edge_cost = self.get_next_destination(prev_pt)
			# mark it visited
			self.visited[next_pt] = 1
			# update the path and the cost
			path[counter] = next_pt
			cost += edge_cost
			counter += 1
			# move to the next vertex
			prev_pt = next_pt
		# account for the last edge from the last point to the first point
		cost += self.distances[path[0]][path[-1]]
		# return the cost, might be useful for a multistart
		return path, cost
