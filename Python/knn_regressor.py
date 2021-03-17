import numpy as np
import pandas as pd

path = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

headernames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

url = path

data = pd.read_csv(url, names=headernames)
array = data.values
X = array[:,:2]
y = array[:,2]
data.shape

#output:(150, 5)

from sklearn.neighbors import KNeighborsRegressor
knnr = KNeighborsRegressor(n_neighbors=10)
knnr.fit(X, y)

print ("The MSE is:",format(np.power(y-knnr.predict(X),2).mean()))
