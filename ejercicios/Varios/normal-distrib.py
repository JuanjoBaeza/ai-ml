from numpy.random import seed
from numpy.random import normal
import numpy as np
import matplotlib.pyplot as plt

#make this example reproducible
seed(1)

#generate sample of 200 values that follow a normal distribution 
data = normal(loc=0, scale=1, size=1000)

#view first five values
print("Primeros 5 valores: ", data[0:5])

#find mean of sample
m = np.mean(data)
print("La media de la muestra: ", m)

#find standard deviation of sample
d = np.std(data, ddof=1)
print("La desviación standard: ", d)

#create a quick histogram to visualize the distribution of data values
count, bins, ignored = plt.hist(data, 30)
plt.show()