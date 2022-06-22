import numpy 
import matplotlib.pyplot as plt 
from sklearn.metrics import r2_score
numpy.random.seed(2)

#The x axis represents the number of minutes before 
#making a purchase. 

#The y axis represents the amount of money spent on 
#the purchase.
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100)/x 

plt.scatter(x, y)
print("DATOS DATASET ORIGINAL")
plt.show()

#The training set should be a random selection of 80% of 
#the original data. 

#The testing set should be the remaining 20%.
train_x = x[:80] 
train_y = y[:80] 

test_x = x[80:] 
test_y = y[80:]

# -------------------------------------------------------

print("DATOS DE ENTRENAMIENTO")

mymodel1 = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline1 = numpy.linspace(0, 6, 100)
r2a = r2_score(train_y, mymodel1(train_x))

#It measures the relationship between the x axis and the y
#axis, and the value ranges from 0 to 1, where 0 means no 
#relationship, and 1 means totally related.
print("Error R2: ", r2a)

plt.scatter(train_x, train_y)
plt.plot(myline1, mymodel1(myline1))
plt.show()

# -------------------------------------------------------

print("DATOS DE TEST")

mymodel2 = numpy.poly1d(numpy.polyfit(test_x, test_y, 4))
myline2 = numpy.linspace(0, 6, 100)
r2b = r2_score(test_y, mymodel2(test_x))

print("Error R2: ", r2b)

plt.scatter(test_x, test_y)
plt.plot(myline2, mymodel2(myline2))
plt.show()

# -------------------------------------------------------

#How much money will a buying customer spend, 
#if she or he stays in the shop for 5 minutes? 
mymodel = numpy.poly1d(numpy.polyfit(test_x, test_y, 4))
print(mymodel(5))