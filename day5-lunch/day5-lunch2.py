#!/usr/bin/env python

"""
Usage: ./02-scree.py <SRR072893/t_data.ctab> <output.bed>

Determine an approximation of the promoter region for each of the transcripts present in your SRR072893/t_data.ctab file. Do so by finding the region +/- 500bp from the transcription start site of each transcript. Save as a tab separated file with the extension .bed and columns chromosome, start, end, t_name.
Hint: Look at strand information

don't save giant files to git

"""

import sys
import pandas as pd

df = pd.read_csv( sys.argv[1], sep="\t" )

#specify desired column order
coi = [ "t_name", "chr", "start", "end", "strand" ]

for index, row in sample_df.iterrows():
    if row["strand"] == "+":
        pos_st = row["start"]-500
        pos_fin = row["start"]+500
        if pos_st < 1:
            pos_st = 1
        print "\t".join([row["chr"], str(pos_st), str(pos_fin), row["t_name"]])
    elif row["strand"] == "-":
        neg_st = row["end"]-500
        neg_fin = row["end"]+500
        if neg_st < 1:
            neg_st = 1
        print "\t".join([row["chr"], str(neg_st), str(neg_fin), row["t_name"]])

# for index, row in df.iterrows():
#     if row["strand"] == "+":
#         if row["start"] - 500 > 500:
#             row["start"] = 1
#         else:
#             row["start"] = row["start"] - 500
#         print "\t".join([row["chr"], str(row["start"]), str(row["end"]), row["t_name"]], )
#     elif row["strand"] == "-":
#         if row["end"] + 500 < len(df["length"]):
#             row["end"] = len(df["length"])
#         else:
#            row["end"] = row["end"] + 500
#         print "\t".join([row["chr"], str(row["start"]), str(row["end"]), row["t_name"]], )
   
        




#print "\t".join([row["chr"], str(row["start"]), str(row["start"]), row["t_name"]])

#roi1 = df["strand"] == +
#roi2 =
#print df[coi]
#roif = df["strand"] == "+"
#roir = df["strand"] == "-"
#df["promoter_start"] = df["start"] - 500
#df["promoter_end"] = df["start"] + 500



#for x in df["strand"]:
    
    #if x == df["+"]
    
    


#df[coi][roi].to_csv( sys.argv[2], sep="\t", header=False, index=False)

# transcripts_df = pd.read.csv( sys.argv[1] )
#
# t = {}
#
# for chromosome, start, end, t_name in df.itertuples():
#     t_df = (transcripts_df["t_id"], transcripts_df["chr"], transcripts_df["start"], transcripts_df["end",], ["promoter_start"], ["promoter_end"])
#
#     print t_df
    
    
    

#
# for chromosome, start, end, t_name in df.itertuples():
#     sample_df = pd.read_csv( () sys.argv[2], , "t_data.ctab"), sep="\t", index_col="t_name" )
#
#     d[ sex + "_" + stage ] = sample_df["FPKM"]
#
# df = pd.DataFrame ( d )
#
# df.to_csv(sys.stdout)
#
#
#
# for item in ctab.readline():
#     if strand == "+":
#         start = "start" -500
#         end = "start" + 500
#     else:
#         rstart = "start" -500
#         rend = "start" + 500
#
#
#
#
# # plt.figure()
# # plt.scatter( x[:,0], x[:,1], alpha=0.8, c=sexes)
# # plt.savefig( sys.argv[2] )
# # plt.close()