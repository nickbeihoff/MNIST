import pandas as pd

data = pd.read_csv("train.csv", sep=',')
data = data['label']
print(data.value_counts())
