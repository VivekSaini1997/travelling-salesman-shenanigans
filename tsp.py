''' this file is intended to be used to do most of the "front end" work,
	namely displaying prompts to the user,
	for the time being this is very simplistic '''

import sys
from tsp_util import *
import algorithms.tsp_greedy as tsp_greedy
import algorithms.tsp_greedy_multistart as tsp_greedy_multistart
import algorithms.tsp_2_opt as tsp_2_opt

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
	#greedy_map = tsp_greedy.tsp_greedy(pts, screen_resolution)
	#multi_map = tsp_greedy_multistart.tsp_greedy_multistart(pts, screen_resolution)
	two_opt_map = tsp_2_opt.tsp_2_opt(pts, screen_resolution, 5)

	# keep map open until user presses enter
	# THIS IS DEFINITELY A WIP
	print 'This is the generated map, press enter to exit'
	#print 'The cost of the greedy path is {}'.format(greedy_map.cost)
	#print 'The cost of the multistart path is {}'.format(multi_map.cost)
	print 'The cost of the 2-opt path is {}'.format(two_opt_map.cost)
	esc  = raw_input()
	return


if __name__ == '__main__':
	main(sys.argv)