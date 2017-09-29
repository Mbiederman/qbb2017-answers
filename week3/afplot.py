#!/usr/bin/env python

"""

Usage: ./afplot.py <af.info.txt> <af.png>

ftp://210.218.217.24/Store/BioTools/vcftools_0.1.11/website/src/options.inc 

--get-INFO <string>

This option is used to extract information from the INFO field in the VCF file. The <string> argument specifies the INFO tag to be extracted, and the option can be used multiple times in order to extract multiple INFO entries. The resulting file, with suffix '.INFO', contains the required INFO information in a tab-separated table. For example, to extract the NS and DB flags, one would use the command: 

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(sys.argv[1], sep="\t")

af_list = []

for item in df["AF"]:
    if "," in item:
        stupid = item
        duh = stupid.split(",")
        for x in duh:
            #if x not in af_list:
            af_list.append(float(x))
    else:
        af_list.append(float(item))       
#af_list.sort()            
                
# for af in af_list:
#     print af
x = af_list
# minimum = np.min(x)
# maximum = np.max(x)

plt.figure()
plt.hist(x, bins=10, range=(min(x), max(x)))
#plt.hist(x, bins=0.1, range=[0,1])
#plt.savefig("afplot.png")
plt.savefig(sys.argv[2] + ".png")
plt.close()   
                
#df = df.sort_values(by="AF", ascending=True)
#
# af_list = []
#
# for item in df["AF"]:
#     if "," in item:
#         stupid = item
#         duh = stupid.split(",")
#         for x in duh:
#             if x not in af_list:
#                 af_list.append(x)
#     else:
#         af_list.append(item)
# # af_list.sort()
# # for a in af_list:
# #     print a
#
# #print af_list
# af_values = []
#
# for m in af_list:
#     if m not in af_values:
#         af_values.append(m)
#     else:
#         continue
#
# af_values.sort()
#
# af_array = []
# for u in af_values:
#     count = 0
#     for e in df["AF"]:
#         if e == u:
#             count = count + 1
#         else:
#             continue
#     tup = (u, count)
#     af_array.append(tup)
#
# # for v in af_array:
# #     print v
#
# af_df = pd.DataFrame(af_array, columns=['AF value', 'AF count'])
#
# af_df.to_csv("af.csv", sep='\t')
# # x = af_df['AF value']
# # y = af_df['AF count']
#
# # print af_df
#
# # plt.figure()
# # plt.hist( af_array, bins=10, range=[0,500000000])
# # plt.savefig( sys.argv[2] + ".png" )
# # plt.close()
# # plt.xlabel('AF value')
# # plt.ylabel('AF count')
# # plt.title('Allele Frequencies in s. cerevisiae')
# # #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# # plt.axis(0,10)
# # plt.grid(True)
# # plt.show()
# # plt.close()
#
#
#
# # print af_dict
# # af_array = []
# #
# # for z in af_dict:
# #     af = af_dict[z]
# #     for w in af:
# #         af_array.append((z,w))
# #
# # for potion in af_array:
# #     print potion
#
# # for p in af_values:
# #     print p
#
# # af_list = af_list
# # #print af_list
# # for other_item in df["AF"]:
# #     af_list.append(other_item)
# #
# # for a in af_list:
# #     print a
#
#
#
#     # if item in af_values:
# #         continue
# #     elif item not in af_values:
# #
# #             # for x in dumb:
# # #                 if item in af_values:
# # #                     continue
# # #                 else:
# # #                     af_values.append(x)
# #         else:
# #             af_values.append(item)
# #
# # af_values.sort()
# # # print af_values
# #
# # for x in af_values:
# #     print x
#
# #af_counts = pd.Series(af_values).value_counts()
# #print af_counts
#
# # af_dict = {}
# # for i in df["AF"]:
# #     count = 0
# #     if i == x in af_values:
# #         count = count + 1
# #         af_dict[int(x)] = count
# #     print af_dict
#