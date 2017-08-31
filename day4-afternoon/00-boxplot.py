#!/usr/bin/env python

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#~/qbb2017/samples.csv 
#~/data/results/stringtie/

df_samples = pd.read_csv( sys.argv[1] )
soi = df_samples["sex"] == "female"

df_gene = pd.DataFrame()
for sample in df_samples["sample"][soi]:
    print sample
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv( fname, sep="\t" )
    roi = df ["gene_name"] == "Sxl"
    df_gene[sample] = np.log1p(df[roi]["FPKM"])
    
print df_gene

plt.figure()
plt.boxplot( df_gene.values )
plt.savefig("boxplot.png")
plt.close()