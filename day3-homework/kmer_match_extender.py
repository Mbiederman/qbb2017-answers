#!/usr/bin/env python

"""Based on your kmer matcher, create kmer_match_extender.py which for each matched k-mer 
will extend on either end to find the longest exact match. For each target sequence, 
print the matches ordered from longest to shortest.

Hints

You can consider each query k-mer (position in the query) independently and in order.
You can track the position in the query using enumerate."""

import sys
import fasta

target = open(sys.argv[1])
#query = open(sys.argv[2])
#k = int(sys.argv[3])
kt = 1
kmer_extender_index = {}
for ident, sequence in fasta.FASTAReader(target):
    sequence = sequence.upper()
    for i in range(0, len(sequence) - kt):
        kmer = sequence[i:i+kt]
        kmer_extender_index[kmer].append((ident, i))

print kmer_extender_index
    #kmer = (ident,i)
        #kmer_extender_index[kmer].append((ident, i))
#print kmer_extender_index

#for kmer, count in kmer_index.iteritems():
   #print kmer, count  

#ident, sequence_q = fasta.FASTAReader(query).next()
#sequence_q = sequence_q.upper()
#for i in range(0, len(sequence_q) - k):
#    qkmer = sequence_q[i:i+k]
#    if qkmer in kmer_index:
#        result = kmer_index[qkmer] 
#        for q in result:
#            #print q[0], "\t", q[1], "\t", i, "\t", qkmer
