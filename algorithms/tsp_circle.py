'''	ok this is a janky algorithm i thought of, doesn't mean it hasn't been done before however 
what it does is it generates a circle around the midpoint of all the points such that half of the points 
lie within it and half the points lie outside, then it generates two simple polygons from the points on either side,
then it tries to connects the two together by removing an edge on both polygons and connecting the two paths together
only god knows hwo good the path will be but it is efficient (only O(n^2) i believe)'''

import graphics as g
import numpy as np
import math
import time
import random
from tsp_map import *

# called tsp_circle because the main focal point of the algorithm is a circle
class tsp_circle(tsp_map):
	"""docstring for tsp_circle"""
	def __init__(self, pts, screen_res):
		super(tsp_circle, self).__init__(pts, screen_res)
		self.draw_circle()

	# uses all the pts to generate a circle with center at the midpoint of all points and radius
	# such that exactly half the points lie outside of it
	def draw_circle(self):
		# get the midpoint
		pt_cnt = len(self.pts)
		avg_pt = g.Point(sum([k.x for k in self.pts])/pt_cnt, sum([k.y for k in self.pts])/pt_cnt)

		# now get the average distance away
		# this is attempted with list comprehensions and not for loops
		radius_arr = [ sl_distance(k, avg_pt) for k in self.pts ]
		avg_radius = sum(radius_arr)/pt_cnt

		circ = g.Circle(avg_pt, avg_radius)
		circ.setOutline('red')
		circ.draw(self.window)
