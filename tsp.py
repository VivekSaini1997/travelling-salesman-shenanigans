''' this file is intended to be used to do most of the "front end" work,
	namely displaying prompts to the user,
	for the time being this is very simplistic '''

import sys
from algorithms.tsp_util import *
import algorithms.tsp_greedy as tsp_greedy
import algorithms.tsp_greedy_multistart as tsp_greedy_multistart
import algorithms.tsp_2_opt as tsp_2_opt
import algorithms.tsp_sa as tsp_sa
import algorithms.tsp_circle as tsp_circle
import algorithms.tsp_giftwrap as tsp_giftwrap
# import algorithms.tsp_bitonic as tsp_bitonic


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
	#pts = generate_random_points(num_points, (10, screen_resolution[0] - 10), (10, screen_resolution[1] - 10))
	# from a file apparently
	pts = get_points_from_txt('points.csv')

	# a slightly nicer interface to actually select between the algorithms
	# TODO: add a UI to handle user input of map types
	map_type = 'giftwrap'
	# a dictionary storing all of the algorithms as callables
	map_type_dict = {
		'circle': tsp_circle.tsp_circle,
		# 'bitonic': tsp_bitonic.tsp_bitonic,
		'greedy': tsp_greedy.tsp_greedy,
		'multistart': tsp_greedy_multistart.tsp_greedy_multistart,
		'2-opt': tsp_2_opt.tsp_2_opt,
		'simulated annealing': tsp_sa.tsp_sa,
		'giftwrap': tsp_giftwrap.tsp_giftwrap
	}
	# now get the proper algorithm given the map_type
	if map_type in map_type_dict:
		map_algo = map_type_dict.get(map_type)(pts, screen_resolution)
	else:
		print('Invalid map selected')
		return
	# keep map open until user presses enter
	# THIS IS DEFINITELY A WIP
	print ('The cost of the {} path is {}'.format(map_type, map_algo.cost))
	esc  = input()
	return


if __name__ == '__main__':
	main(sys.argv)