import numpy as np
import pandas as pd
import sklearn
import sklearn
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
from sklearn import metrics

digits = pandas.read_csv("train.csv", sep=",")