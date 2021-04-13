import pandas as pd
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


data = pd.read_csv('res.csv')
data.drop('file_name', axis=1, inplace=True)
print(data.head(5))

X = data.iloc[:,1:].values
y = data['class_name']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=27)

from sklearn.feature_selection import VarianceThreshold
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
sel.fit_transform(X_test)
print(sel)

# RandomForest_model = RandomForestClassifier()
# RandomForest_model.fit(X_train, y_train)
#
# # rfe = RFE(RandomForest_model, 5)
# # fit = rfe.fit(X_train, y_train)
# # FIT_prediction = fit.predict(X_test)
#
# # test = SelectKBest(RandomForest_model, k=22)
# # fit = test.fit(X_train, y_train)
# # FIT_prediction = fit.predict(X_test)
# sel = SelectFromModel(RandomForestClassifier(n_estimators = 100))
# sel.fit(X_train, y_train)
# RandomForest_prediction = sel.p(X_test)
# # LR_prediction = LR_model.predict(X_test)
#
# # Оценка точности — простейший вариант оценки работы классификатора
# print("")
# print("acc RF:", accuracy_score(RandomForest_prediction, y_test))
# # print("acc LR:", accuracy_score(LR_prediction, y_test))
# # print("acc FIT:", accuracy_score(FIT_prediction, y_test))
# print("")
