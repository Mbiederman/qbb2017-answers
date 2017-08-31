#!/usr/bin/env python

"""usage: ./kmer_matcher.py <target.fa> <query.fa> <k>"""


# target path: /Users/cmdb/qbb2017-answers/day3-homework
# query path: /Users/cmdb/qbb2017-answers/day3-homework
# fasta.py path: /Users/cmdb/qbb2017-answers/day3-homework 


import sys
import fasta 


target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3])

kmer_index = {}

for ident, sequence in fasta.FASTAReader(target):
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k):
        kmer = sequence[i:i+k]
        if kmer not in kmer_index:
            kmer_index[kmer] = [(ident, i)]
        else:
            kmer_index[kmer].append((ident, i))


#for kmer, count in kmer_index.iteritems():
   #print kmer, count  

ident, sequence_q = fasta.FASTAReader(query).next()
sequence_q = sequence_q.upper()
for x in range(0, len(sequence_q) - k):
    qkmer = sequence_q[x:x+k]
    if qkmer in kmer_index:
        result = kmer_index[qkmer] 
        for q in result:
            print str(q[0]) + "\t" + str(q[1]) + "\t" + str(x) + "\t" + str(qkmer)
            
        
              

#for kmer, count in kmer_counts.iteritems():
   # print kmer, count  

 