#!/usr/bin/env python

"""
Usage: ./02-scree.py <all.csv> <output.png>
"""
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_csv( sys.argv[1], index_col=0)

#PCA is a class

pca = PCA()

fit = pca.fit( df )

n, p = df.shape

plt.figure()
plt.bar( range(p), fit.explained_variance_ratio_ )
plt.savefig( sys.argv[2] )