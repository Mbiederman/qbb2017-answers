#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv( sys.argv[1], sep="\t" )
df2 = pd.read_csv( sys.argv[2], sep="\t" )

fpkm= ["FPKM"]



x = np.log(df1[fpkm] + 1)
y = np.log(df2[fpkm] + 1)
##np.polyfit(df1.values.flatten(), df2.values.flatten(), 1)
#poly = np.polyfit(x,y,1)
#fit = np.poly1d(poly)

plt.figure()
plt.scatter( x, y, alpha=0.05)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x,y, deg=2))(np.unique(x)))
plt.axis([0, 10, 0, 10])
plt.grid(True)
plt.xlabel("SRR072915")
plt.ylabel('SRR072893')
plt.title('Scatterplot of RPKM')

plt.savefig( sys.argv[3] + ".png")

plt.close()
