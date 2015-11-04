__author__ = 'Xu'

from algorithm.knn import KNNClassifier
from data.cardata.ReadCarData import ReadCarData

data = ReadCarData()
data.nomarlized()
data.display()
knn = KNNClassifier(data.data[:200])
knn.training()
knn.predict([1.0,1.0,1.0,1.0,1.0,1.0], 10)