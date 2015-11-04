__author__ = 'Xu'

from ..Data import Data

def ReadCarData():
    data = Data()
    f = open("data\cardata\car.data")
    buying = {"vhigh":1.0, "high":2.0, "med":3.0, "low":4.0}
    maint = {"vhigh":1.0, "high":2.0, "med":3.0, "low":4.0}
    doors = {"2":1.0, "3":2.0, "4":3.0, "5more":4.0}
    persons = {"2":1.0, "4":2.0, "more":3.0}
    lugboot = {"small":1.0, "med":2.0, "big":3.0}
    safety = {"low":1.0, "med":2.0, "high":3.0}
    for line in f.readlines():
        fs = line.rstrip("\n").split(",")
        d = [buying[fs[0]],maint[fs[1]],doors[fs[2]],persons[fs[3]],lugboot[fs[4]],safety[fs[5]]]
        v = fs[6]
        data.append([d, v])
    f.close()
    return data
