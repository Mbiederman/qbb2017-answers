#!/usr/bin/env python

"""
Usage ./00-reorder.py <csv_file> <tsv_file>

-Remove header
-Reorder columns: sex, sample, stage
-Subset "female" in sex column
-convert delimiter from comma to tab
"""

import sys
import pandas as pd


df = pd.read_csv( sys.argv[1] )
#specify desired column order
coi = [ "sex", "sample", "stage"]
#print df[coi]
roi = df["sex"] == "female"
df[coi][roi].to_csv( sys.argv[2], sep="\t", header=False, index=False)
