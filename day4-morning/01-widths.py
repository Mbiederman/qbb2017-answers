#!/usr/bin/env python

"""
Usage: ./01-width.py <ctab> <prefix>
"""

import sys
import pandas as pd

df = pd.read_csv( sys.argv[1], sep="\t")

coi = [ "chr", "start", "end", "t_name", "FPKM", "width" ]

df["width"] = df["end"] - df["start"] + 1
 
print df[coi].head()

print "Mean %d, std dev %d" % ( df["width"].mean(), df["width"].std() )

import matplotlib.pyplot as plt
plt.figure()
plt.hist( df["width"], bins=100, range=[0,10000] )
plt.savefig( sys.argv[2] + ".png" )
plt.close()

