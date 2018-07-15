''' a subclass of tsp_map that implements a greedy algorithm
	to get a quick (and suboptimal) tsp solution
	it's a start lmao '''

import graphics as g
import numpy as np
import math
import time
from tsp_greedy import *

# it's time to multistart i guess lol
class tsp_greedy_multistart(tsp_greedy):
	"""docstring for tsp_greedy_multistart"""
	def __init__(self, pts, screen_res = None,):
		# let greedy know it IS the father (this is a child class of greedy)
		super(tsp_greedy_multistart, self).__init__(pts=pts, screen_res=screen_res, parent=True)

	def multi_start(self):
		pass

