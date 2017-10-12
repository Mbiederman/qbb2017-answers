#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(sys.argv[1], sep="\t")

x = df["PC1"]
y = df["PC2"]




plt.figure()
plt.scatter(x,y)
plt.savefig( sys.argv[2] )
plt.close()