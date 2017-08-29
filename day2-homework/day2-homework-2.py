#!/usr/bin/env python

# Write a python script for identifier mapping. 
    # input1 = the mapping file (as above) 
    # input2 = a c_tab file from StringTie 
# find the corresponding translation from the mapping file. 
    # If found, print the line from the c_tab file with the identifier. 
    # If not found, it should do one of two things depending on a command line argument:
        # 1. Print nothing (ignore the line)
            #or
        # 2. Print and fill the field with a default value

import sys

# Input mapping file day2-homework-1.out
input1_dict = {}    
with open(sys.argv[1]) as input1:
    for line in input1:
        (key, value) = line.split()
        input1_dict[key] = value
print input1_dict
        
#for key, value in gene_names_counts.iteritems():
input2 = open(sys.argv[2])
for line in input2:
    fields = line.rstrip("\r\n").split()
    if fields[8] in input1_dict:
        fields[8] = input1_dict[fields[8]]
        print "\t".join(fields)
       # if input1(key) in
            
        
    



# Input a c_tab file from StringTie
#input2 = open(sys.argv[2]) 

#for field in input1:
    #if field in input2: 
        #for line in input2:
            #print line 
    #else: 
        #continue
               