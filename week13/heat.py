#!/usr/bin/env python

"""
Usage: ./heat.py abundance_table.tab

"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_abundance = pd.read_csv(sys.argv[1], sep = "\t", index_col = 0)

plt.pcolor(df_abundance)
plt.title("Abundance")
plt.xlabel("Sample")
plt.ylabel("Bin")
plt.xticks(np.arange(0.5, df_abundance.shape[1], 1), df_abundance.columns, rotation=90)
plt.subplots_adjust(bottom=0.4)
plt.colorbar()
#plt.show()
plt.savefig("Abundance_heatmap.png")


    # plt.xlabel("Sample")
#     plt.ylabel("Bin")
#     plt.xticks(np.arange(0.5, df.shape[1], 1), df.columns, rotation=90)
#     #plt.yticks(np.arange(0.5, 8.5, 1))
    # plt.subplots_adjust(bottom=0.4)
#     plt.colorbar(heatmap)
    #plt.show()
    # plt.savefig("Abundance_heatmap.png")

# plot_heatmap(df_abundance, "Abundance")
    # plt.subplots_adjust( # Adjust the spacing of the subplots, to help make everything fit
#         left = 0.05,     # ... the left edge of the left-most plot will be this percent of the way across the width of the plot
#         bottom = 0.15,   # ... the bottom edge of the bottom-most plot will be this percent of the way up the canvas
#         right = 1.0,     # ... the right edge of the right-most plot will be this percent of the way across the width
#         top = 0.95,      # ... the top edge of the top-most plot will be this percent of the way from the bottom
#     )
    # plt.colorbar()
    #plt.subplots_adjust(bottom=0.4)
    #plt.colorbar(heatmap)
    #plt.show()
    


# ticks = ["Lorem ipsum dolor sit amet, consectetur adipisicin", "g elit, sed do",      "eiusmod tempor incididunt ut labo", "re et dolore magna ali", "qua. Ut en", "im ad minim veniam, quis nostr", "ud exercitation ullamco labo", "ris nisi ut aliquip ex ea c", "ommodo co", "nsequat. Duis aute irure dolor in rep"]
# data = [5,1,2,4,1,4,5,2,1,5]
# ind = np.arange(len(data))
# fig = plt.figure()
# ax = plt.subplot(111)
# ax.barh(ind, data, 0.999)
# ax.set_yticks(ind + 0.5)
# r = ax.set_yticklabels(ticks)#, ha = 'le
#df_abundance = pd.read_csv(sys.argv[1], sep = "\t", index_col=0)
#df_data = df_abundance.pivot()
#print df_abundance

#data = np.array(df_abundance)
#print data


# shape of the dataframe
#print df_abundance.shape

# checking what the columns are
#print df_abundance.columns


# bins = df[""]
# sns.heatmap(df, cmap="YlGnBu")
# sns.plt.show()

# df = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
#                        'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
#                        'baz': [1, 2, 3, 4, 5, 6]})
#
# print df                   