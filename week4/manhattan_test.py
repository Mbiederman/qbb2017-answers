#!/usr/bin/env python

""" #X-axis is the entire length of the list.
#Y-axis is the actual -log10 p value.

Usage: ./manhattan_test.py <plink.assoc.linear.tsv> <plot name>

I was having strange unknown problems with pandas so I used some of Justin and Danny's line split technique code.  I needed to practice that anyway.

I also could not get the float to work without manually fixing the stupid association file so I did after hours of it not working.

UPDATE: I fixed the issue
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

phenotypes = open(sys.argv[1])

# sigp = []
# nsigp = []

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
# print sigx
# print sigy
# print nsigx
# print nsigy     
       
# print sigp
# print nsigp           
            
    # if "chr*" in line:
#         continue
#     print float(line[8])
        
    #if float(assoc[8]) <= 1e-5:
        #print float(assoc[8])

# df = pd.read_csv(sys.argv[1], sep="\t")
#
# print df["CHR"]
#
# sigp = []
# nsigp = []
#
# for pval in df['P']:
#     if "chr" or "NA" in pval:
#         continue
#     elif float(pheno) <= 1e-5:
#         sigp.append(-np.log10(float(pval)))
#
# print df
        
        
    


plt.figure()
# for i in (x,y):
#     y == i
#     if i > 1e-5:
#         plt.scatter(x, y, alpha = 0.5, c="blue")
plt.scatter(nsigx, -np.log10(nsigy), alpha = 0.5, c="blue")
plt.scatter(sigx, -np.log10(sigy), alpha = 0.5, c="red")

plt.ylabel("-log10 p value")
plt.xlabel("Genome Location")

plt.savefig(str(sys.argv[2]) + "_manhattan_plot.png")
plt.close()
