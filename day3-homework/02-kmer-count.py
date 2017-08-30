#!/usr/bin/env python

"""
Count kmers in a fasta file
"""

import sys
import fasta

kmer_counts = {}
k = 5
for ident, sequence in fasta.FASTAReader( sys.stdin ):
    sequence = sequence.upper()
    for i in range( 0, len(sequence) - k ):
        kmer = sequence[i:i+k]
        if kmer not in kmer_counts:
            kmer_counts[kmer] = 1
        else:
            kmer_counts[kmer] += 1
            
for kmer, count in kmer_counts.iteritems():
    print kmer, count                