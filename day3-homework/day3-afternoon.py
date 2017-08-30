#!/usr/bin/env python

import sys

totalspan = 0
gencnt = 0

for line in sys.stdin:
    line = line.rstrip()
    mylen = int(line)
    totalspan += mylen
    gencnt += 1
    
print "there are %d genes, with a total span of %d, average gen len is %f" % (gencnt, totalspan, float(totalspan)/gencnt)    