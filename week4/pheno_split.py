#!/usr/bin/env python

"""

from Danny and Matthew:
"awk 'NR>1''{gsub ("_","\t")}{print}' BYxRM_PhenoData.txt > pheno.txt"



Usage: ./pheno_split.py BYxRM_PhenoData.txt

First I added the column title "FID_IID" to the text file manually.

split column: https://stackoverflow.com/questions/31737939/split-pandas-column-into-two
df['left'],df['right'] = zip(*df[0].apply(lambda x: x.split('|')))

delete column name: https://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe-using-python-del
del df['column_name']

"""
import sys
import pandas as pd

df = pd.read_csv(sys.argv[1], sep="\t")

df_split = df["FID_IID"]
#df['FID'],df['IID'] = zip(*df['FID_IID'].apply(lambda x: x.split('_')))
# df['AB'].str.split('-', 1, expand=True)
df_split['FID'], df_split['IID'] = df_split["FID_IID"].str.split('_', 1).str

# del df['FID_IID']

print df


