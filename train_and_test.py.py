import pandas as pd
from sklearn import svm

# read tarin.csv as pandas datafrane object
train_df = pd.read_csv('train.csv')

# drop label and use remaining feature data columns for training
X_train = train_df.drop("label", axis=1)
# use label column for ground truth data for training
Y_train = train_df["label"]

#use svm classifier for model
clf = svm.SVC()
#start train
clf.fit(X_train, Y_train)

#save trained classifier as joblib file so that we can use it later
import joblib
joblib.dump(clf, "binary_clf.joblib")