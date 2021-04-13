import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE


def write_res(name, prediction, test):
    print("")
    print("acc " + name + ":", accuracy_score(prediction, test))
    print("f1_score macro " + name + ":", f1_score(prediction, test, average='macro'))
    print("f1_score micro " + name + ":", f1_score(prediction, test, average='micro'))
    print("f1_score weighted " + name + ":", f1_score(prediction, test, average='weighted'))

    res = open("res_classification/" + name + ".txt", 'w')
    res.writelines(name)
    res.writelines("\n")
    res.writelines("\n")
    res.writelines("confusion_matrix " + name)
    res.writelines("\n")
    res.writelines("\n")
    res.writelines(str(confusion_matrix(prediction, test)))
    res.writelines("\n")
    res.writelines("\n")
    res.writelines("classification_report " + name)
    res.writelines("\n")
    res.writelines("\n")
    res.writelines(classification_report(prediction, test))


data = pd.read_csv('res.csv')
data.drop('file_name', axis=1, inplace=True)
# print(data.head(5))

X = data.iloc[:, 1:].values
y = data['class_name']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=27)

KNN_model = KNeighborsClassifier(n_neighbors=5)
LR_model = LogisticRegression()
RandomForest_model = RandomForestClassifier()

KNN_model.fit(X_train, y_train)
KNN_prediction = KNN_model.predict(X_test)
write_res("KNeighborsClassifier", KNN_prediction, y_test)

LR_model.fit(X_train, y_train)
LR_model_prediction = LR_model.predict(X_test)
write_res("LogisticRegression", LR_model_prediction, y_test)

RandomForest_model.fit(X_train, y_train)
RandomForest_prediction = RandomForest_model.predict(X_test)
write_res("RandomForest", RandomForest_prediction, y_test)

for i in range(1, 28):
    n = i * 10
    rfe = RFE(RandomForest_model, n)
    fit = rfe.fit(X_train, y_train)
    FIT_prediction = fit.predict(X_test)
    write_res("RandomForest RFE-" + str(n), FIT_prediction, y_test)

