#!/usr/bin/env python

""" 

Usage: ./manhattan_batch.py <*.assoc.linear> <*_manhattan_plot.png>

"""

import sys
import numpy as np
import matplotlib.pyplot as plt

phenotypes = open(sys.argv[1])

pos = []
pval = []
position = 0
for line in phenotypes:
    if "CHR" in line:
        continue
    fields = line.split()
    if "NA" in fields[8]:
        continue   
    else:
        position = position + 1
        pos.append(position)       
        pval.append(float(fields[8]))
# print pos    
        
coords = []
for x,y in zip(pos,pval):
    assocs = (x,y)
    coords.append(assocs)
# print coords
sigx = []  
sigy = []
nsigx = []
nsigy = []
            
for a,b in coords:
    if b <= 1e-5:
        sigx.append(a)
        sigy.append(b)  
    elif b > 1e-5:
        nsigx.append(a)
        nsigy.append(b)          

plt.figure()
plt.scatter(nsigx, -np.log10(nsigy), alpha = 0.5, c="blue")
plt.scatter(sigx, -np.log10(sigy), alpha = 0.5, c="red")

plt.ylabel("-log10 p value")
plt.xlabel("Genome Location")

plt.savefig(str(sys.argv[2]) + "_manhattan_plot.png")
plt.close()
