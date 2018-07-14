''' a subclass of tsp_map that implements a greedy algorithm
	to get a quick (and suboptimal) tsp solution
	it's a start lmao '''

import graphics as g
import numpy as np
import math
import time
from tsp_map import *

# felt cute <3 might multi-start later
class greedy_tsp(tsp_map):
	"""docstring for greedy_tsp"""
	def __init__(self, pts, screen_res = None, start_idx = None):
		super(greedy_tsp, self).__init__(pts, screen_res)
		# an array of all the visited points
		self.visited = np.zeros(len(pts))
		if start_idx is None:
			start_idx = 0
		self.path = np.array([start_idx])
		# an array of the returned path, starts off with just the start
		self.visited[start_idx] = 1
		# generate and draw the greedy solution
		self.generate_solution()
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
	def generate_solution(self):
		# set the initial point to be the starting index, i.e. the first vertex in the path
		prev_pt = self.path[0]
		# set the initial cost to zero
		self.cost = 0
		# while the solution path doesn't contain all of the verticies, generate the next vertex
		# using the nearest valid one and continue
		while len(self.path) < len(self.pts):
			next_pt, edge_cost = self.get_next_destination(prev_pt)
			self.visited[next_pt] = 1
			self.path = np.append(self.path, next_pt)
			self.cost += edge_cost
			prev_pt = next_pt
