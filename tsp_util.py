''' this is a file which is intended to store the non class functions pertaining to the map '''

import graphics as g
import numpy as np
import random
import math

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
