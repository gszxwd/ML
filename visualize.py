__author__ = "Xu"

import matplotlib.pyplot as plt
from data.cardata.ReadCarData import ReadCarData

data = ReadCarData()
data.nomarlized()
data.display()
x = []
y = []
for d in data.data:
    x.append(d[0][0])
    y.append(d[0][1])
fig = plt.figure()
plt.scatter(x, y, color='r')
plt.show()
