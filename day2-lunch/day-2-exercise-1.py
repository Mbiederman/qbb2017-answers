#!/usr/bin/env python

import sys

# Opening file with open
## f = open( "/Users/cmdb/data/genomes/BDGP6.fa")

## f = open ( sys.argv[1] )
count = 0

if len( sys.argv ) > 1:
    sam = open( sys.argv[1] )   
else:
    sam = sys.stdin
  
        
for line in sam:
    if line.startswith("@"):
        n = 0
    else:
        if "NM" in line:
            n=1
        else:
            n=0
    count = count + n              

print count


