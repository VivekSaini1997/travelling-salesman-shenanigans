import graphics as g
import numpy as np
import scipy
import matplotlib
import random
import cmath
import math
import time
import sys

''' hopefully uses numpy and graphics.py in order to simulate travelling salesman problem solutions '''

# creates 'num' amount of points with centers in ranges
# xrange_ and yrange_, which are tuples denoting the min and max 
# x/y coordinates for each of the points
def generate_random_points(num, xrange_, yrange_):
	return np.array([ g.Point(random.randint(xrange_[0], xrange_[1]), random.randint(yrange_[0], yrange_[1])) for k in range(num) ])

# returns the straight line distance between two points
# assumes the points are of type Point from the graphics lib
def sl_distance(pt1, pt2):
	return math.sqrt(((pt2.x - pt1.x) ** 2) + ((pt2.y - pt1.y) ** 2))

# the same as above but doesn't use a sqrt to save computation time
# this makes sense in a more preformant language
def fast_sl_distance(pt1, pt2):
	return ((pt2.x - pt1.x) ** 2) + ((pt2.y - pt1.y) ** 2)

# this object is used to manage the TSP map
class tsp_map(object):

	"""docstring for tsp_map"""
	# sets up the map to have verticies based on the input
	# as well as the screen height and width and draws it 
	# if the resolution parameters are passed in
	def __init__(self, pts, screen_res=None):
		self.pts = pts
		self.form_adj_mat()
		# the path for the class and the cost of it
		# the path variable stores indicies not actual points and is 
		# for the actual algo to deal with
		self.cost = 0
		self.path = None
		if screen_res is not None:
			screen_width = screen_res[0]
			screen_height = screen_res[1]
			self.create_screen(screen_width, screen_height)
			self.draw_points()

	# creates the screen that will display the tsp problem,
	# doesn't draw anything to it
	def create_screen(self, screen_width = 1280, screen_height = 720):
		self.window = g.GraphWin('TSP window', screen_width, screen_height)

	# given the points (verticies), sets up the adjacency matrix for a fully connected graph to be used
	# not efficient at all, needs Cython or to be ported to a different language (maybe C++/Java in the future)
	def form_adj_mat(self):
		self.distances = np.array([ [ sl_distance(k, l) for k in self.pts ] for l in self.pts ])

	# draws all the points and edges of the tsp_map to it's screen
	def draw_full_map(self):
		# this draws the points
		self.draw_points()
		# and this draws the edges
		for src in self.pts:
			for dst in self.pts:
				if src != dst:
					line = g.Line(src, dst)	
					line.draw(self.window)

	# just draw the points, don't worry about the edges
	def draw_points(self):
		for pt in self.pts:
			circ = g.Circle(pt, 4)
			circ.setFill('blue')
			circ.draw(self.window)

	# get the cost of the optimal path using the adjacency matrix
	def get_path_cost(self):
		# make sure you don't have a cost from before
		self.cost = 0
		# go through each edge and add its cost
		for dst_index in range(len(self.path)):
			self.cost += self.distances[self.path[dst_idx]][self.path[(dst_idx + 1) % len(self.path)]]
		# return that cost
		return self.cost

	# actually draws out the solution given the path
	def draw_solution(self):
		# go though the path and draw the vertex and a line to the next path for 
		# each vertex
		# ok nvm about the vertex, that's handled in the parent class
		for path_index in range(len(self.path)):
			# then draw the line, if it is the last vertex, draw a line back to the start 
			line = g.Line(self.pts[self.path[path_index]], self.pts[self.path[(path_index + 1) % len(self.path)]])
			line.draw(self.window)
			# this is WIP but we sleep because it ain't real shit (makes things look prettier)
			time.sleep(.05)

# a subclass of tsp_map that implements a greedy algorithm
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

# the main function 
# called when the function is called from command line
# currently just draws a tsp map
def main(args):
	# take in the number of points from the user, default to 20 however
	if len(args) > 1:
		num_points = int(args[1])
	else:
		num_points = 20
	# draw the map
	screen_resolution = (1280, 720)
	pts = generate_random_points(num_points, (10, screen_resolution[0] - 10), (10, screen_resolution[1] - 10))
	greedy_map = greedy_tsp(pts, screen_resolution)

	# keep map open until user presses enter
	# THIS IS DEFINITELY A WIP
	print 'This is the generated map, press enter to exit'
	print 'The cost of this path is {}'.format(greedy_map.cost)
	esc  = raw_input()
	return


if __name__ == '__main__':
	main(sys.argv)