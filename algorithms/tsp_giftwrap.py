''' a subclass of tsp_map that implements the gift wrapping algorithm to find a convex hull
man i should abuse the linear algebra i learned in university huh '''

import graphics as g
import numpy as np
import math
import time
from .tsp_map import *

# now we using the gift wrapping algorithm to find a convex hull
# maybe this will generate solid paths?
class tsp_giftwrap(tsp_map):
    """docstring for tsp_giftwrap"""
    def __init__(self, pts, screen_res = None):
        # initialize the subclass?
        # tbh it's been a while since i used this codebase
        super(tsp_giftwrap, self).__init__(pts, screen_res)

        self.generate_hull()


        self.cost = self.get_path_cost(self.path)
        # finally draw the solution
        self.draw_solution()
        

    # generates the outermost hull
    # look at this page to better understand what it's doing
    # https://en.wikipedia.org/wiki/Gift_wrapping_algorithm
    # TODO: update this so it can be called multiple times
    def generate_hull(self):
        # first find the leftmost point
        leftmost_pt = self.pts[0]
        for pt in self.pts:
            if pt.x < leftmost_pt.x:
                leftmost_pt = pt
        # now start the convex hull from that index
        # using python lists instead of numpy lists so i can resize better
        # leftmost_idx = np.where(self.pts == leftmost_pt)[0][0]
        convex_hull = [leftmost_pt]
        # find the second point for the convex hull path using a ghost point
        ghost_pt = g.Point(leftmost_pt.x, leftmost_pt.y + 1000)
        print(ghost_pt)
        # get the distance between the leftmost point and the ghost point
        e1 = 1000
        # now iterate through the other points and find the angle formed by the points
        # ghost_pt, leftmost_pt, pt, where pt is the other points
        # find the maximum interior angle, that is the minimum convex angle
        # that will correspond to the next point on the convex hull
        max_angle = 0
        max_pt = leftmost_pt
        for pt in self.pts:
            if pt != leftmost_pt:
                e2 = sl_distance(leftmost_pt, pt)
                e3 = sl_distance(pt, ghost_pt)
                # use cosine law to find the angle
                angle = np.arccos(((e1 ** 2) + (e2 ** 2) - (e3 ** 2)) / (2 * e1 * e2))
                # if this angle is greater than the maximum found angle,
                # make this the point of comparison
                if angle > max_angle:
                    max_angle = angle
                    max_pt = pt
        # now add the max point to the hull
        convex_hull.append(max_pt)
        # now keep finding convex hull points until you hit the beginning 
        while convex_hull[-1] != convex_hull[0]:
            # start by initializ
            e1 = sl_distance(convex_hull[-2], convex_hull[-1])
            max_angle = 0
            max_pt = leftmost_pt
            for pt in self.pts:
                if pt != convex_hull[-1] and pt != convex_hull[-2]:
                    e2 = sl_distance(convex_hull[-1], pt)
                    e3 = sl_distance(pt, convex_hull[-2])
                    # use cosine law to find the angle
                    angle = np.arccos(((e1 ** 2) + (e2 ** 2) - (e3 ** 2)) / (2 * e1 * e2))
                    # if this angle is greater than the maximum found angle,
                    # make this the point of comparison
                    if angle > max_angle:
                        max_angle = angle
                        max_pt = pt
            # now add the max point to the hull
            convex_hull.append(max_pt)

        # convert the convex hull to a path and set it to the self.path
        self.path = np.array([np.where(self.pts == pt)[0][0] for pt in convex_hull])
