''' the file for the main tsp_map class
	hopefully uses numpy and graphics.py in order to simulate travelling salesman problem solving algorithms '''

import graphics as g
import numpy as np
import math
import time
from .tsp_util import *

# this object is used to manage the TSP map
class tsp_map(object):

	"""docstring for tsp_map"""
	# sets up the map to have verticies based on the input
	# as well as the screen height and width and draws it 
	# if the resolution parameters are passed in
	def __init__(self, pts, screen_res = None):
		self.pts = pts
		self.form_adj_mat()
		# the path for the class and the cost of it
		# the path variable stores indicies not actual points and is 
		# for the actual algo to deal with
		self.cost = 0
		self.path = list()
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

	# get the cost of any path of the map using the adjacency matrix
	def get_path_cost(self, path):
		# initialize the cost to zero
		cost = 0
		# go through each edge and add its cost
		for dst_index in range(len(path)):
			cost += self.distances[path[dst_index]] [path[(dst_index + 1) % len(path)]]
		# return that cost
		return cost

	# actually draws out the solution given the path
	def draw_solution(self):
		# go though the path and draw the vertex and a line to the next path for 
		# each vertex
		# ok nvm about the vertex, that's handled in the parent class
		for path_index in range(len(self.path)):
			# print(path_index)
			# then draw the line, if it is the last vertex, draw a line back to the start 
			line = g.Line(self.pts[self.path[path_index]], self.pts[self.path[(path_index + 1) % len(self.path)]])
			line.draw(self.window)
			# this is WIP but we sleep because it ain't real shit (makes things look prettier)
			time.sleep(.05)
