from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
 
iris = datasets.load_iris()
 
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)
 
kf = KFold(n_splits=5)
 
clf = LogisticRegression(solver='lbfgs',max_iter=1000)
 
clf.fit(X_train, y_train)
 
score = clf.score(X_train,y_train)
 
print("Metrica del modelo:", score)
 
scores = cross_val_score(clf, X_train, y_train, cv=kf, scoring="accuracy")
 
print("Metricas cross_validation:", scores)
 
print("Media de cross_validation:", scores.mean())
 
preds = clf.predict(X_test)
 
score_pred = metrics.accuracy_score(y_test, preds)
 
print("Metrica en Test:", score_pred)