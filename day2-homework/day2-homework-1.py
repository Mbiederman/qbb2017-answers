#!/usr/bin/env python

import sys

if len( sys.argv ) > 1:
    flydb = open( sys.argv[1] )   
else:
    flydb = sys.stdin
    
Fly_data = {}
    
for line in flydb:
    if "DROME" in line:
        fields = line.rstrip("\r\n").split()
        if len(fields) < 4:
            continue
        else:    
            #AC_column = fields[2]
            #FlyBase_gene_AC_column = fields[3]
            print fields[3] + "\t" + fields[2]
            

#Fly_data[AC_column].append(FlyBase_gene_AC_column)
#print Fly_data
    
       
        #fields = line.rstrip("\r\n").split("\t")
        
        #AC_column = fields[2]
        #FlyBase_gene_AC_column = fields[3]
        #if AC_column not in Fly_data: 
            #Fly_data[gene_name] = [FlyBase_gene_AC_column]
        #else: 
            #Fly_data[AC_column].append(FlyBase_gene_AC_column)
        
#for key, value in Fly_data.iteritems():
    #print key, value
    