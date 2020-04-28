import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv", sep=',')
df = df['label']
df = df.to_frame()
location = []
for i in range(0, 10):
    search = i
    df.loc[df.isin([search]).any(axis=1)].index.to_list().append(location)
print(location)
'''
df['Location'] = location
df.reset_index(inplace=True)
df.columns = ['Number', 'Location']
df.plot(kind='scatter', x='Number', y='Location')
plt.show()
'''