#!/usr/bin/env python
#code from morning lesson
#For the first 10 alignments, print just the column indicating which chromosome a given read aligns to chromosome
#HINT: .split()

import sys




if len( sys.argv ) > 1:
    sam = open( sys.argv[1] )   
else:
    sam = sys.stdin
  
        
for line in sam:
    if line.startswith("@"):
        n = 0
    else:
        fields = line.split('\t')
        if fields[2] != "*":
            
                 

print id[:10]

#for line in sam:
    # start and end are in columns 3 and 4
    #if line.startswith("t_id"):
        #continue
    #fields = line.split("\t")
    #print str(fields[3]) 