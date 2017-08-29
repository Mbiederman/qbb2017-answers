#!/usr/bin/env python

import sys


count = 0

if len( sys.argv ) > 1:
    sam = open( sys.argv[1] )   
else:
    sam = sys.stdin
  
        
for line in sam:
    if line.startswith("@"):
        n = 0
    else:
        if "NH:i:1" in line:
            n=1
        else:
            n=0
    count = count + n              

print count