import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer

# https://medium.com/@julie.yin/understanding-the-data-splitting-functions-in-scikit-learn-9ae4046fbd26

# Read the data
X_full = pd.read_csv('datasets/train.csv', index_col='Id')
X_test_full = pd.read_csv('datasets/test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X_full.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X_full.SalePrice # La variable dependiente 'y' es la columna SalePrice, por ello se descarta
X_full.drop(['SalePrice'], axis=1, inplace=True)

# To keep things simple, we'll use only numerical predictors, we exclude object type columns
X = X_full.select_dtypes(exclude=['object'])
X_test = X_test_full.select_dtypes(exclude=['object'])

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

print (X_train.head())
print("\n")
print(X_train.shape)

# Number of missing values in each column of training data
missing_val_count_by_column = (X_train.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])

""" ----------------------------------------------------------------------------------------- """

def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# Fill in the line below: get names of columns with missing values
cols_with_missing = [col for col in X_train.columns if X_train[col].isnull().any()]

print("\n")
print("Cols with missing values:", cols_with_missing)

""" ----------------------------------------------------------------------------------------- """

# Fill in the lines below: drop columns in training and validation data
reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)

X_train = np.nan_to_num(X_train)
X_valid = np.nan_to_num(X_valid)
y_train = np.nan_to_num(y_train)
y_valid = np.nan_to_num(y_valid)

print("MAE (Without Drop columns with missing values):", score_dataset(X_train, X_valid, y_train, y_valid))
print("MAE (Drop columns with missing values):", score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))

""" ----------------------------------------------------------------------------------------- """

# Fill in the lines below: imputation
my_imputer = SimpleImputer(strategy='median')
final_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
final_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

final_X_train = X_train
final_X_valid = X_valid

print("MAE (Imputation):", score_dataset(final_X_train, final_X_valid, y_train, y_valid))

""" ----------------------------------------------------------------------------------------- """

# Define and fit model
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(final_X_train, y_train)

# Get validation predictions and MAE
preds_valid = model.predict(final_X_valid)
print("MAE (Your approach):", mean_absolute_error(y_valid, preds_valid))

# Preprocess test data
final_X_test = pd.DataFrame(my_imputer.transform(X_test))

# Get test predictions
preds_test = model.predict(final_X_test)

# Save test predictions to file
output = pd.DataFrame({'Id': X_test.index,
                       'SalePrice': preds_test})
output.to_csv('/mnt/c/Repo/ai-ml/kaggle/datasets/submission.csv', index=False)