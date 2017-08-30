#!/usr/bin/env python

import random

key = 4
#initialize the whole to be searched
nums = range(10)

hi = len(nums)     
lo = 0

#main loop: keep going while there are options available
while lo < hi:
    midix = (hi + lo)/2
    mid = nums[midix]
    print "checking in the range [%d, %d] midix[%d] = %d" % (lo, hi, midix, mid)
    if (mid == key):
        print "found %d, at position %d, who's value is %d!" % (key, midix, mid)
        break
    elif key > mid:
        lo = midix + 1
    else:
        hi = midix
    
                   
#print nums 


#for i in nums:
   # while key != i:
       # if key > (len(nums)/2):
           # nums = nums.range(len(nums/2),10)
       # else:
           # nums = nums.range(0,(len(nums/2))
#    print nums
            

