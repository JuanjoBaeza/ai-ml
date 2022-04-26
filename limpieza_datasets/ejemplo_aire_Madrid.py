import pandas as pd
import urllib.request

#Abrimos el csv de 2017 y lo pasamos a un data frame
calidad_aire = pd.read_csv("../datasets/calidad_aire_Madrid.csv", delimiter=";")

calidad_aire

# print ("Columnas del data frame")
# print (calidad_aire.columns)
# print ("\n")
# print ("Dimensiones del data frame")
# print (calidad_aire.shape)
# print ("\n")
# print ("Tipo de dato por variable: \n")
# print (calidad_aire.dtypes)

# Crea un array y añade los nº de columna que tengan valor nulo
L=[]
for i in range(69):
  if calidad_aire.iloc[:,i].isnull().sum()!=0:
      L.append(i)
print(L)

# Imprime las estaciones que sean la 4
estaciones=calidad_aire[calidad_aire.iloc[:,2]==4]
estaciones

# Imprime la octava columna del dataset
print(calidad_aire.iloc[:,8])