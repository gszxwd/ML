__author__ = 'Xu'

from distance import Distance

class KNNClassifier(object):
    def __init__(self, tdata):
        self.tdata = tdata

    def training(self):
        self.labels = []
        # get labels
        for t in self.tdata:
            if t[1] not in self.labels:
                self.labels.append(t[1])
        # classfy
        self.classes = {}
        for l in self.labels:
            self.classes[l] = []
        for t in self.tdata:
            self.classes[t[1]].append(t[0])

    def predict(self, sample, k):
        candidats = [{9999:0}]*k
        ids = [0]*k
        for i in range(len(self.tdata)):
            dist = Distance.euclideanDist(sample, self.tdata[i][0])
            if dist < candidats[-1].keys()[0]:
                candidats.sort()
                candidats.pop()
                candidats.insert(0,{dist:i})
        # most is the winner
        counter = {}
        for c in candidats:
            counter[self.tdata[c.values()[0]][1]] = 0
        for c in candidats:
            counter[self.tdata[c.values()[0]][1]] = counter[self.tdata[c.values()[0]][1]] + 1
        print counter