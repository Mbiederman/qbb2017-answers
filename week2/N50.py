#!/usr/bin/env python

"""Usage: ./N50.py <fasta>"""

import sys
import fasta

contigs = fasta.FASTAReader(open(sys.argv[1]))

# for item in contigs:
#     print item
"""sort contigs by length, count contigs, sum lengths of contigs, length of contigs/2, find contig closest to length of contigs/2 >="""

sorted_lengths = []
    
for (name, sequence) in contigs:
    seq_length = len(sequence)
    sorted_lengths.append(seq_length)

#reverse=True was contributed by Matthew
sorted_lengths = sorted(sorted_lengths, reverse=True)

#print sorted_lengths

total_length = 0
for length in sorted_lengths:
    total_length = total_length + length
    
print "total length = %d" % (total_length)

count = 0
for item in sorted_lengths:
    count = count + 1
    
print "contig count = %d" % (count)    

N50_length = total_length/2
print "N50 midpoint = %d" % (N50_length)

print "average contig = %f, min contig = %f, max contig = %f" % (float(total_length/count), min(sorted_lengths), max(sorted_lengths))

n50 = 0
n50_contigs = []
for x in sorted_lengths:
    n50 = n50 + x
    n50_contigs.append(x)
    if n50 < N50_length:
        continue
    else:
        break
           
print "N50 crossed midpoint = %d" % (n50)        
#print n50_contigs
print "The N50 contig length is %d" % (n50_contigs[-1])        

#print sorted_lengths

    