#!/usr/bin/env python

import sys
import pandas as pd


df_H3K4me3 = pd.read_csv( sys.argv[1], sep="\t", header=None )
df_H3K9me3 = pd.read_csv( sys.argv[2], sep="\t", header=None )
df_H3K27me3 = pd.read_csv( sys.argv[3], sep="\t", header=None )
df_H3K36me3 = pd.read_csv( sys.argv[4], sep="\t", header=None )
df_fpkms = pd.read_csv( sys.argv[5], sep="\t" )

transcripts = []

