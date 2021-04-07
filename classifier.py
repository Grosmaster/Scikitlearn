import pandas as pd
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


data = pd.read_csv('res.csv')
data.drop('file_name', axis=1, inplace=True)
print(data.head(5))

X = data.iloc[:,1:].values
y = data['class_name']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=27)

# print("X_train")
# print(X_train)
# print("y_train")
# print(y_train)

SVC_model = svm.SVC()
KNN_model = KNeighborsClassifier(n_neighbors=5)

SVC_model.fit(X_train, y_train)
KNN_model.fit(X_train, y_train)

SVC_prediction = SVC_model.predict(X_test)
KNN_prediction = KNN_model.predict(X_test)

# Оценка точности — простейший вариант оценки работы классификатора
print(accuracy_score(SVC_prediction, y_test))
print(accuracy_score(KNN_prediction, y_test))
# Но матрица неточности и отчёт о классификации дадут больше информации о производительности
print(confusion_matrix(SVC_prediction, y_test))
print(classification_report(KNN_prediction, y_test))