__author__ = 'Xu'

import random
from distance import Distance

class KMeansClassfier(object):
    def __init__(self, data):
        self.data = data

    def clustering(self, K, N=100):
        classes = {}
        # generate K initial points
        pts = []
        for i in range(K):
            classes[i] = []
            pt = []
            for j in range(len(self.data[0][0])):
                pt.append(random.random())    # normallized data
            pts.append(pt)
        #
        for n in range(N):
            for i in range(K):
                classes[i] = []
            for i in range(len(self.data)):
                temp = 9999
                flag = 0
                for j in range(K):
                    dist = Distance.euclideanDist(self.data[i][0], pts[j])
                    if dist < temp:
                        temp = dist
                        flag = j
                classes[flag].append(i)
            #
            for i in range(K):
                means = [0]*len(self.data[0][0])
                for j in range(len(classes[i])):
                    for k in range(len(self.data[0][0])):
                        means[k] = means[k]+self.data[j][0][k]
                    for k in range(len(self.data[0][0])):
                        means[k] = means[k]/len(self.data[0][0])
                pts[i] = means
        return classes