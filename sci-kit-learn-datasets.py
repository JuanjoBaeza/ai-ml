import pandas as pd
from sklearn import datasets

data = datasets.load_breast_cancer()

# Read the DataFrame, first using the feature data
df = pd.DataFrame(data.data, columns=data.feature_names)

# Add a target column, and fill it with the target data, 0 será Benigno y 1 Maligno
df['Mal/Ben'] = data.target

# Show the first five rows
print(df.head(50))

# Store the feature data
X = data.data
# store the target data
y = data.target

# split the data using Scikit-Learn's train_test_split
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.neighbors import KNeighborsClassifier
logreg = KNeighborsClassifier(n_neighbors=6)
logreg.fit(X_train, y_train)

print(round(logreg.score(X_test, y_test),3), "% precisión predictiva.")