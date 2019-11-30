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
		# this is done so the original arr is not mutated
		# it can lead to frustration if it is 
		return np.array(list(arr[a:b]))

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
	# now replace the indicies between a and b with the reversed subarray
	# different logic depending on whether or not a is smaller than b
	# basically the range differs
	if a < b:
		for k in range(abs(b-a)):
			_arr[(a + k) % len(_arr)] = subarray[k]
	else:
		for k in range(len(arr) - abs(b-a)):
			_arr[(a + k) % len(_arr)] = subarray[k]
	# return the array
	return _arr

# generates the random points and prints them to a .csv file
# also generates the number of points printed to the file
# assumes filename does not have an extension
# also generates a file in the same directory 
def generate_random_points_to_file(num, xrange_, yrange_, filename):
	# get the random points
	pts = generate_random_points(num, xrange_, yrange_)
	# then print them to the file
	file = open(filename + ".csv", 'w')
	file.write("{}\n".format(num))
	for point in pts:
		file.write("{},{},\n".format(point.x, point.y))
	file.close()

# grabs points from a text file
# to be used to test algorithms on static inputs
def get_points_from_txt(filename):
	file = open(filename, 'r')
	num = int(file.readline())
	# initialize the array we wish to return
	arr = np.array([g.Point(0,0) for k in range(num)])
	count = 0 
	# for each of the lines, parse them and store them in the array
	for line in file:
		arr[count] = g.Point(line.split(',')[0], line.split(',')[1]) 
		count += 1
	# close the file and return the array
	file.close()
	return arr
