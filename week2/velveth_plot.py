#!/usr/bin/env python


"""
Usage: ./velveth_plot.py <velveth_mapped.tsv> <output.png>

     X1            X2        
Refr1_start-----Refr1_end  Refr2_start-----Refr2_end
Cont1_start-----Cont1_end  Cont2_start-----Cont2_end
    Y1             Y2

sort ascending by Refr1_start
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

df_align = pd.read_csv( sys.argv[1], sep="\t")

df_align = df_align.sort_values(by="zstart1", ascending=True)

# print df_align
 
xstart =[]
xend = []
ystart = []
yend = []

for start1 in df_align["zstart1"]:
    xstart.append(start1)

for end1 in df_align["end1"]:
    xend.append(end1)

for start2 in df_align["zstart2"]:
    ystart.append(start2)

for end2 in df_align["end2"]:
    yend.append(end2)   

    
# print xstart, xend, ystart, yend    
# df = pd.DataFrame()
# for contig in df_align["zstart1"]:
#     print sample
#     fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
#     df = pd.read_csv( fname, sep="\t" )
#     roi = df ["gene_name"] == "Sxl"
#     df_gene[sample] = np.log1p(df[roi]["FPKM"])
# print df_align



plt.figure()
# plt.xlim(0, max(xend))
# plt.ylim(0, max(yend))
plt.scatter((xstart,ystart),(xend,yend))
plt.savefig( sys.argv[2] )
plt.close()