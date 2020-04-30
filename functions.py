import math
import numpy as np


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


x = input("X: ")
x = int(x)
print("Sigmoid:")
print(sigmoid(x))
print("Softmax:")
print(softmax(x))
