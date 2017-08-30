#!/usr/bin/env python

import random

r = random.randint(1,100)
#print r
nums = []

for i in xrange(5):
    r = random.randint(1,100)
    #print "the %dth number is %d" % (i, r)
    nums.append(r)

print nums    

nums.sort()
print nums 

key = 42

for i in xrange(len(nums)):
    v = nums[i]
    print "scanning the %dth number is %d" % (i, v)
    if (v == key):
        print "Found it at position %d" % (i)