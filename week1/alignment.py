#!/usr/bin/env python

"""Usage: $ ./alignment.py <alignment_prot.fa> <1000_homologues.fa> <aminout.out>"""

"""Most of this code was contributed by Tabea.  I figured out my own order of opening files and tab separating the amino acid ids from their nucleotide sequences and then returning the lines after.  I tested my tab separation within the lines using the commented out part at the bottom and command line entry: $ ./alignment.py <alignment_prot.fa> <1000_homologues.fa> <aminout.out> <aminout.out> | less -S

Then I realized that I did want the ids on different lines than the sequences for a fasta format and changed it back."""

import sys
import itertools
import fasta

aminos = fasta.FASTAReader(open(sys.argv[1]))
nucleotides = fasta.FASTAReader(open(sys.argv[2]))
aminout = open(sys.argv[3], 'w')

for (nucname, nuc), (aminame, amino) in itertools.izip(nucleotides, aminos):
    #aminout.write(nucname + "\t")
    aminout.write(nucname + "\n")
    for item in amino:
        if item == "-":
            aminout.write("---")
        else:
            aminout.write(nuc[:3])
            nuc = nuc[3:]
    aminout.write("\n")        
    
# test = open(sys.argv[4])
# for line in test:
#     print line  
        