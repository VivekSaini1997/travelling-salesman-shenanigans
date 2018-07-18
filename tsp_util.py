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

# gets a subarray of arr that starts at index a and goes until index b
# wrapping around if need be
# assumes both arrays are numpy arrays
def get_circular_range(arr, a, b):
	if a > b:
		return np.concatenate((arr[a:], arr[:b])) 
	else:
		return  np.array(list(arr[a:b]))

# takes in a numpy array and two points, reverses their order in the path, 
# and places them back in the path
def swap_and_reverse(arr, a, b):
	# if a and b are the same, there is no swapping to be done
	# so just return
	if a == b:
		return arr
	# get the array by value not reference, we don't want to mutate the list
	_arr = np.array(list(arr))
	# get the subarray and reverse it
	subarray = get_circular_range(_arr, a, b)
	subarray = np.flip(subarray, 0)
	print subarray, a, b
	# now replace the indicies between a and b with the reversed subarray
	# different logic depending on whether or not a is smaller than b
	# basically the range differs
	if a < b:
		for k in range(abs(b-a)):
			print k
			_arr[(a + k) % len(_arr)] = subarray[k]
			print _arr
	else:
		for k in range(len(arr) - abs(b-a)):
			print k
			_arr[(a + k) % len(_arr)] = subarray[k]
			print _arr
	# return the array
	return _arr
