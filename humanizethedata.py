import pandas as pd
from sklearn import preprocessing

pd.read_csv("train.csv", sep=',')

le = preprocessing.LabelEncoder()
