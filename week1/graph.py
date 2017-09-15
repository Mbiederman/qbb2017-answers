#!/usr/bin/env python

"""Usage: $ ./graph.py <1000_homologues.fa> <aminout.out>"""



"""Danny found the codon table code and """




"""
Sourced from:
http://www.petercollingridge.co.uk/python-bioinformatics-tools/codon-table via Danny
"""
import sys
import fasta
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

#Cycles through each combination of three bases (codon) to make all the combinations of the amino acids. Assigns them to a 1-letter code. Stop codons marked as *.
bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

def codon_splitter(sequence, k):
    return [sequence[i:i+k] for i in range(0, len(sequence), k)]

nucfile = open(sys.argv[1])
nucline = codon_splitter(nucfile.readline(), 3)
dS = [0]*len(nucline)
dN = [0]*len(nucline)

for line in nucfile:
    if line[:2] == "gi":
        continue
    for index, (codon, ref) in enumerate(zip(codon_splitter(line, 3), nucline)):
        if codon == ref:
            continue
        if not codon in codon_table or not ref in codon_table:
            continue
        if codon_table[codon] == codon_table[ref]:
            dS[index] += 1
        else:
            dN[index] += 1

# for i in range(len(nucline)):
#     if dN[i] > 0 and dS[i] > 0:
#         dSdN = float(dS[i])/(float(dS[i]) + float(dN[i]))
# print dSdN
        
for i in range(len(nucline)):
    if dN[i] > 0 and dS[i] > 0:
        print("% Similarity ({}): {}".format(nucline[i], float(dS[i])/(dS[i] + dN[i])))
# dsdns = {}
#
# for ident, sequence in fasta.FASTAReader(nucfile):
#     for i in range( 0, len(sequence), 3 ):
#         codon_list = []
#         codon_list.append(sequence[i:i+3])
#     dsdns[ident] = codon_list
#     print dsdns
        
        
# #Split each line into codons
# def codon_splitter(sequence, k):
#     return [sequence[i:i+k] for i in range(0, len(sequence), k)]
#
# alignmentFile = open(sys.argv[1])


#Open file. Parse the file. Skip over headers. Take 3 DNA bases at a time. For loop. Compare each column to the original first codon. If no change or blank, then skip. if bases differ but code for same amino acid, mark as synonymous. If bases differ and code for different amino acids, mark as nonsynonymous. Keep a ratio/count of S and NS for each column. 

#Skip first line with header
# alignmentFile.readline()
# #Store first sequence for comparison
# firstLine = codon_splitter(alignmentFile.readline(), 3)
# dS = [0]*len(firstLine)
# dN = [0]*len(firstLine)
#
# for line in alignmentFile:
#     if line[:2] == "gi":
#         continue
#     for index, (codon, ref) in enumerate(zip(codon_splitter(line, 3), firstLine)):
#         if codon == ref:
#             continue
#
#         if not codon in codon_table or not ref in codon_table:
#             continue
#
#         if codon_table[codon] == codon_table[ref]:
#             dS[index] += 1
#         else:
#             dN[index] += 1
#
# for i in range(len(firstLine)):
#     if dN[i] > 0 and dS[i] > 0:
#         dSdN = float(dS[i])/(float(dS[i]) + float(dN[i]))
#
#
# print dSdN

# for i in range(len(firstLine)):
#     if dN[i] > 0 and dS[i] > 0:
#         print("% Similarity ({}): {}".format(firstLine[i], float(dS[i])/(dS[i] + dN[i])))
        
# df = pd.read_csv( sys.argv[1] )
# #specify desired column order
# coi = [ "sex", "sample", "stage"]
# #print df[coi]
# roi = df["sex"] == "female"
# df[coi][roi].to_csv( sys.argv[2], sep="\t", header=False, index=False)

# import sys
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# nucfile = open(sys.argv[1])
# aminfile = open(sys.argv[2])
#
# nucdict = {}
# amindict = {}
#
# nucfile.readline()
# for line in nucfile:
#     if line.startswith(">"):
#         continue
#     else:
#         nuclist.append(line)
#
# aminfile.readline()
# for x in aminfile:
#     if x.startswith(">"):
#         continue
#     else:
#         aminlist.append(x)
#
# print nuclist
#

