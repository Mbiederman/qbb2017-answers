#!/usr/bin/env python
"""
Basic Exercise: Time Course w/ Replicates
Add a second series of FBtr0331261 abundance to the same plot, this time for male samples.
style it similarly to Lott et al., 2011 PLoS Biology (i.e. x-axis tick labels, color, legend, etc.)
add stage 14 replicates to the same plot (~/qbb2017/replicates.csv)
HINT: since there are only replicates for 14A/B/C/D, you will need to "skip" plotting 10/11/12/13
HINT: plt.plot( x, y, 'o' )
 ./01-timecourse.py ~/qbb2017/samples.csv ~/data/results/stringtie/
Usage:  ./day4-homework.py <samples.csv> <ctabdir> <replicates.csv)
"""
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


transcript = "FBtr0331261"

#series 1 females
df_samplesf = pd.read_csv( sys.argv[1] )
soif = df_samplesf["sex"] == "female"

fpkmsf = []

for sample in df_samplesf["sample"][soif]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv( fname, sep="\t" )
    roi = df ["t_name"] == transcript
    fpkmsf.append( df[roi]["FPKM"].values )

print fpkmsf

#series 2 males
df_samplesm = pd.read_csv( sys.argv[1] )
soim = df_samplesm["sex"] == "male"   

fpkmsm = []


for sample in df_samplesm["sample"][soim]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv( fname, sep="\t" )
    roi = df ["t_name"] == transcript
    fpkmsm.append( df[roi]["FPKM"].values )

print fpkmsm

#series 3 female replicates
df_samplesfr = pd.read_csv( sys.argv[3] )
soifr= df_samplesfr["sex"] == "female"

fpkmsfr = []

while len(fpkmsfr) < 4:
    fpkmsfr.append(None)
for sample in df_samplesfr["sample"][soifr]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv( fname, sep="\t" )
    roi = df ["t_name"] == transcript
    fpkmsfr.append( df[roi]["FPKM"].values )
    
print fpkmsfr

#series 4 male replicates
df_samplesmr = pd.read_csv( sys.argv[3] )
soimr = df_samplesmr["sex"] == "male"   

fpkmsmr = []

while len(fpkmsmr) < 4:
    fpkmsmr.append(None)
for sample in df_samplesmr["sample"][soimr]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv( fname, sep="\t" )
    roi = df ["t_name"] == transcript
    fpkmsmr.append( df[roi]["FPKM"].values )

print fpkmsmr


plt.figure()
plt.plot(fpkmsf, color='r', lw=3)
plt.plot(fpkmsm, color='b', lw=3)
plt.plot(fpkmsfr, "o", color='r', markersize=10)
plt.plot(fpkmsmr, "o", color='b', markersize=10)
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (FPKM)")
plt.title("Transcription of Drosophila Sex Lethal (Sxl) by Developmental Stage")
art = []
plt.margins(0.1,0)
plt.subplots_adjust(bottom=0.15)
plt.legend(["Female", "Male", "Female Replicates", "Male Replicates"], loc="center right", bbox_to_anchor=(1.5,0.5), frameon=False, numpoints=1)
plt.xticks(range(8), ["10", "11", "12", "13", "14A", "14B", "14C", "14D"], rotation=90)
plt.savefig("day4-homework.png", additional_artists=art, bbox_inches="tight")
plt.close()

# plt.figure()
# plt.scatter( x, y, alpha=0.05)
# plt.plot(np.unique(x), np.poly1d(np.polyfit(x,y, deg=2))(np.unique(x)))
# plt.axis([0, 10, 0, 10])
# plt.grid(True)
# plt.xlabel("SRR072915")
# plt.ylabel('SRR072893')
# plt.title('Scatterplot of RPKM')
#
# plt.savefig( sys.argv[3] + ".png")
#
# plt.close()