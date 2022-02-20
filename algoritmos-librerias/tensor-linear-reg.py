# Simple Linear Regression
# It’s a technique to estimate the relationship between two quantitative variables. It is used when you want to establish:
# Strength of the relationship — How strong the relationship is between two variables
# The value of the dependent variable at a certain value of the independent variable.

# Where:
# y is the predicted value of the dependent variable for any given value of the independent variable which is X.
# B0 is the intercept and B1 is the regression coefficient
# x is the independent variable
# e is the error of the estimate

import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from utils import *
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, LambdaCallback

# %matplotlib inline <-Esto para usarlo con Jupyter notebook en una celda

# tf.logging.set_verbosity(tf.logging.ERROR)

df = pd.read_csv('data.csv',names=['id','year','a','b','c','d','e','price'])
# check missing data
df.isna().sum()

df = df.iloc[:,1:]
dn = (df-df.mean())/df.std()
y_mean = df['price'].mean()
y_std = df['price'].std()
def cl(pred):
    return int(pred * y_std + y_mean)

x = dn.iloc[:,:6]
y = dn.iloc[:,-1]
x_arr = x.values
y_arr = y.values
x_train,x_test,y_train,y_test = train_test_split(x_arr,y_arr,test_size =0.05,random_state=0)

def gm():
    model = Sequential([
        Dense(10,input_shape = (6,),activation='relu'),
        Dense(20,activation = 'relu'),
        Dense(5,activation='relu'),
        Dense(1)
        
    ])
    model.compile(
        loss ='mse',
        optimizer ='adam'
        
    )
    return model
gm().summary()

es = EarlyStopping(monitor = 'val_loss', patience =5)
model =gm()
pu = model.predict(x_test)
h = model.fit(
    x_train, y_train,
    validation_data =(x_test,y_test),
    epochs=100,
    callbacks = [es]
)

# plot_loss(h)

pt = model.predict(x_test)
compare_predictions(pu,pt,y_test)