import pandas as pd
import matplotlib.pyplot as plt
import random

train_df = pd.read_csv("train.csv")

x_train = train_df.iloc[:, 1:].values
y_train = train_df.iloc[:, 0].values

i = random.randint(0, 45)
some_digit = x_train[i]

some_digit_image = some_digit.reshape(28, 28)
print(f"Label: {y_train[i]}")
plt.imshow(some_digit_image, cmap="binary")
plt.show()
