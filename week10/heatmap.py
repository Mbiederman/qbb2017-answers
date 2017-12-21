#!/usr/bin/env python


"""
Most of this was a combination of code from Danny, Max, and class 11.

Usage: ./heatmap.py <hema_data.txt>
"""

import numpy as np
import scipy.cluster as sp
import matplotlib.pyplot as plt
import sys
import pandas as pd
import itertools
from sklearn import datasets
from sklearn.cluster import KMeans


heme_data = pd.read_csv(sys.argv[1], sep = "\t")
values = heme_data.as_matrix()[:,1:].astype(float)

#Get the values for the rows for the heatmap.
link = sp.hierarchy.linkage(values, method="average", metric="euclidean")

#Transpose to find the columnar information for the dendrogram.
link_cols = sp.hierarchy.linkage(values.T, method="average", metric="euclidean")
h_index = sp.hierarchy.leaves_list(link)
ordered_data = values[h_index,:]
dendrites = ["CFU", "poly", "unk", "int", "mys", "mid"]


#Plot the heatmap
plt.figure()
plt.pcolor(ordered_data, cmap="plasma")
ax = plt.gca()
plt.xticks()
plt.grid(False)
plt.colorbar()
plt.title("Heatmap of Heme Data")
plt.savefig("heatmap.png")
plt.show()
plt.close()

"""plt.pcolor(df_abundance)
plt.title("Abundance")
plt.xlabel("Sample")
plt.ylabel("Bin")
plt.xticks(np.arange(0.5, df_abundance.shape[1], 1), df_abundance.columns, rotation=90)
plt.subplots_adjust(bottom=0.4)
plt.colorbar()
#plt.show()
plt.savefig("Abundance_heatmap.png")"""

#Plot the dendrogram
plt.figure()
sp.hierarchy.dendrogram(link_cols, labels=dendrites)
plt.savefig("dendrogram.png")
plt.show()
plt.close()



#Make the k-clusters and plot as heatmap 
kmeans = KMeans(n_clusters=5, random_state=0)
kmeans.fit(values)
labels = kmeans.predict(values)
data_matrix = pd.merge(pd.DataFrame(values, columns = ['CFU', 'poly', 'unk', 'int', 'mys', 'mid']), pd.DataFrame( labels, columns=['cluster'] ), left_index=True, right_index=True )
k_cluster = data_matrix.sort_values('cluster')[['CFU', 'poly', 'unk', 'int', 'mys', 'mid']].values

plt.figure()
plt.imshow(k_cluster, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.title("Heatmap of K-cluster")
plt.colorbar()
plt.xticks() 
plt.savefig("k_clustered.png")
plt.show()
plt.close()