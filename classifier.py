import pandas as pd
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.linear_model import LogisticRegression

from sklearn.feature_selection import RFE

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
# LR_model = LogisticRegression()
RandomForest_model = RandomForestClassifier()

RandomForest_model.fit(X_train, y_train)

rfe = RFE(RandomForest_model, 5)
fit = rfe.fit(X_train, y_train)

# LR_model.fit(X_train, y_train)
SVC_model.fit(X_train, y_train)
KNN_model.fit(X_train, y_train)


SVC_prediction = SVC_model.predict(X_test)
FIT_prediction = fit.predict(X_test)
KNN_prediction = KNN_model.predict(X_test)
RandomForest_prediction = RandomForest_model.predict(X_test)
# LR_prediction = LR_model.predict(X_test)

# Оценка точности — простейший вариант оценки работы классификатора
print("")
print("acc SVC:", accuracy_score(SVC_prediction, y_test))
print("acc KNN:", accuracy_score(KNN_prediction, y_test))
print("acc RF:", accuracy_score(RandomForest_prediction, y_test))
# print("acc LR:", accuracy_score(LR_prediction, y_test))
print("acc FIT:", accuracy_score(FIT_prediction, y_test))
print("")


# Но матрица неточности и отчёт о классификации дадут больше информации о производительности
# print(confusion_matrix(SVC_prediction, y_test))
# print(classification_report(KNN_prediction, y_test))
