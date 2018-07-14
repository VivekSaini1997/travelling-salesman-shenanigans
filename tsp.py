''' this file is intended to be used to do most of the "front end" work,
	namely displaying prompts to the user,
	for the time being this is very simplistic '''

import sys
from tsp_util import *
import algorithms.tsp_greedy as tsp_greedy

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
	greedy_map = tsp_greedy.greedy_tsp(pts, screen_resolution)

	# keep map open until user presses enter
	# THIS IS DEFINITELY A WIP
	print 'This is the generated map, press enter to exit'
	print 'The cost of this path is {}'.format(greedy_map.cost)
	esc  = raw_input()
	return


if __name__ == '__main__':
	main(sys.argv)