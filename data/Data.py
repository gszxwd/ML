__author__ = 'Xu'

class Data(object):
    def __init__(self, data=[]):
        self.data = data

    def append(self, d):
        self.data.append(d)

    def display(self):
        for d in self.data:
            print d

    def nomarlized(self):
        if self.data is None:
            print 'no data'
            return
        self.mins = [9999]*len(self.data[0][0])
        self.maxs = [0]*len(self.data[0][0])
        for d in self.data:
            for i in range(len(d[0])):
                if self.mins[i] > d[0][i]:
                    self.mins[i] = d[0][i]
                if self.maxs[i] < d[0][i]:
                    self.maxs[i] = d[0][i]
        #print self.mins, self.maxs
        for d in self.data:
            for i in range(len(d[0])):
                d[0][i] = abs(d[0][i]-self.mins[i])/(self.maxs[i]-self.mins[i])
