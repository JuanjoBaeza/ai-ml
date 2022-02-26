# Source: https://pub.towardsai.net/decision-trees-vs-random-forests-in-machine-learning-be56c093b0f
# Importing all the libraries needed for the process

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ice_cream=pd.read_csv("../../datasets/decis-tree-IceCreamData.csv")
ice_cream.head(10)

# Using the displot to know the distribution of the Revenue column present in the dataset
#sns.displot(x='Revenue',data=ice_cream,kde=True)

# Using the scatter plot to know the relation between the Temperature and revenue in the dataset
# Plot this or above, not both at same time
plt.scatter(x='Temperature',y='Revenue',data=ice_cream)
plt.title("Relation between Temp and rev")
plt.xlabel('Temp')
plt.ylabel('rev')
plt.show()

# The Temperature is independent and Revenue is dependent on temperature

X=pd.DataFrame(ice_cream['Temperature'])
Y=pd.DataFrame(ice_cream['Revenue'])

#importing train_test_split method from sklearn
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,
                                               random_state=1)

#importing the DecisionTreeRegressor from the sklearn lib
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, Y_train)

#Predicting the values
y_pred=regressor.predict(X_test)
x_pred=regressor.predict(X_train)

#Evaluating the model based on the metrics
from sklearn import metrics

print('Mean Absolute Error:',
            "%.3f" % (metrics.mean_absolute_error(Y_test,y_pred)))
             
             
print('Root Mean Squared Error of train dataset:',
            np.sqrt(metrics.mean_squared_error(Y_train,x_pred)))
             
print('Root Mean Squared Error of test dataset:', 
            "%.3f" % (np.sqrt(metrics.mean_squared_error(Y_test, y_pred))))

