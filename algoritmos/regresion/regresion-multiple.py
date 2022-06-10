from matplotlib import pyplot as plt
import pandas
from sklearn import linear_model 
import matplotlib.pyplot as plt

df = pandas.read_csv("../../datasets/reg-mult-cars.csv")

x = df[['Weight','Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x, y) 

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]]) 

print("CO2 para un vehículo de 2300kg y 1300cc: ", predictedCO2)
print("Valor coef de regresión (Peso, cc): ", regr.coef_)