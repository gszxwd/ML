__author__ = 'Xu'

import math

class Distance(object):
    def __init__(self):
        pass

    @staticmethod
    def euclideanDist(pt1, pt2):
        dist = 0
        for i in range(len(pt1)):
            dist = dist+(pt1[i]-pt2[i])*(pt1[i]-pt2[i])
        dist = math.sqrt(dist)
        return dist
