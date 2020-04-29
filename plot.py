import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv", sep=',')
plt.scatter(df.index, df['label'])
plt.show()