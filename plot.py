import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("train.csv", sep=',')
df = train['label'].value_counts()
df['freq'] = df/len(train)
df = df['freq']
df = df.to_frame()
df.reset_index(inplace=True)
df.columns = ['Number', 'Percent']
df.plot(kind='scatter', x='Number', y='Percent')
plt.show()