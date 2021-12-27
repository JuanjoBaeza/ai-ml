import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

#1.- Read the data source
df = pd.read_csv('datasets/solubility.csv')
print(df.head())

#2.- Data procesing, 4 first cols assigned to X last col assigned to y
X = df.drop(['logS'], axis=1)
y = df.iloc[:,-1] #Another way -> y = df.logS or y = df[‘logS’]

#3.- Split data, 20% test and 80% train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#4.- Load algorithm & Fit model
lr = LinearRegression()
lr.fit(X_train, y_train)

#5.- Train and test the model
y_lr_train_pred = lr.predict(X_train)
y_lr_test_pred = lr.predict(X_test)

#6.- Model performance measured with mean_square_error
lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)

lr_results = pd.DataFrame(['Linear regression',lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
lr_results.columns = ['Method','Training MSE','Training R2','Test MSE','Test R2']

#7.- Print the MSE value
print(lr_train_mse) #Print mse value
print(lr_results)   #Other way to print all values

## Ahora vamos a aplicar otro algoritmo, Random Forest.

rf = RandomForestRegressor(max_depth=2, random_state=42)
rf.fit(X_train, y_train)

y_rf_train_pred = rf.predict(X_train)
y_rf_test_pred = rf.predict(X_test)

rf_train_mse = mean_squared_error(y_train, y_rf_train_pred)
rf_train_r2 = r2_score(y_train, y_rf_train_pred)

rf_test_mse = mean_squared_error(y_test, y_rf_test_pred)
rf_test_r2 = r2_score(y_test, y_rf_test_pred)

rf_results = pd.DataFrame(['Random forest',rf_train_mse, rf_train_r2, rf_test_mse, rf_test_r2]).transpose()
rf_results.columns = ['Method','Training MSE','Training R2','Test MSE','Test R2']

print(rf_train_mse)
print(rf_results) #Print mse value

print(pd.concat([lr_results, rf_results]))

# Visualization of prediction results

plt.figure(figsize=(5,5))
plt.scatter(x=y_train, y=y_lr_train_pred, c="#7CAE00", alpha=0.3)

z = np.polyfit(y_train, y_lr_train_pred, 1)
p = np.poly1d(z)

plt.plot(y_train,p(y_train),"#F8766D")
plt.ylabel('Predicted LogS')
plt.xlabel('Experimental LogS')

# Como interpretar los valores de R2 y MSE
# https://statisticsbyjim.com/regression/interpret-r-squared-regression/
# https://statisticsbyjim.com/regression/standard-error-regression-vs-r-squared/
