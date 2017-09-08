#!/usr/bin/env python

"""

Usage: ./day5-lunch4.py H3K4me3_avg.tab H3K9me3_avg.tab H3K27me3_avg.tab H3K36me3_avg.tab ~/data/results/stringtie/SRR072893/t_data.ctab

Perform ordinary linear regression for all of the four marks to determine how predictive each is of gene expression.
Use all four marks as the independent variables for your regression model
Report the output of the regression (R2, p-value, coefficients, etc.)
Hint: For regression, use ols from statsmodels

"""

import sys
import pandas as pd
import os
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


# transcript = "FBtr0331261"
#
# #series 1 females
# df_samplesf = pd.read_csv( sys.argv[1] )
# soi4 = df_samples4["sex"] == "female"
#
# H3K4me3 = []
#
# for sample in df_samplesf["sample"][soif]:
#     fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
#     df = pd.read_csv( fname, sep="\t" )
#     roi = df ["t_name"] == transcript
#     fpkmsf.append( df[roi]["FPKM"].values )
# df_H3K4me3 = pd.read_csv( sys.argv[1], sep="\t", header=None )
# df_H3K9me3 = pd.read_csv( sys.argv[2], sep="\t", header=None )
# df_H3K27me3 = pd.read_csv( sys.argv[3], sep="\t", header=None )
# df_H3K36me3 = pd.read_csv( sys.argv[4], sep="\t", header=None )
# df_fpkms = pd.read_csv( sys.argv[5], sep="\t" )



df_H3K4me3 = pd.read_csv( sys.argv[1], sep="\t", header=None )
df_H3K4me3 = df_H3K4me3.sort_values(0, ascending=False)

df_H3K9me3 = pd.read_csv( sys.argv[2], sep="\t", header=None )
df_H3K9me3 = df_H3K9me3.sort_values(0, ascending=False)

df_H3K27me3 = pd.read_csv( sys.argv[3], sep="\t", header=None )
df_H3K27me3 = df_H3K27me3.sort_values(0, ascending=False)

df_H3K36me3 = pd.read_csv( sys.argv[4], sep="\t", header=None )
df_H3K36me3 = df_H3K36me3.sort_values(0, ascending=False)

df_fpkms = pd.read_csv( sys.argv[5], sep="\t" )
df_fpkms = df_fpkms.sort_values("t_name", ascending=False)



x1 = df_H3K4me3[5]
x2 = df_H3K9me3[5]
x3 = df_H3K27me3[5]
x4 = df_H3K36me3[5]
y = df_fpkms["FPKM"]


model1 = sm.OLS(y.values, x1.values).fit()
predictions = model1.predict(x1)
print model1.summary()

model2 = sm.OLS(y.values, x2.values).fit()
predictions = model2.predict(x1)
print model2.summary()

model3 = sm.OLS(y.values, x3.values).fit()
predictions = model3.predict(x1)
print model1.summary()

model4 = sm.OLS(y.values, x4.values).fit()
predictions = model4.predict(x4)
print model1.summary()

# model5 = sm.OLS(y, x1, x2, x3, x4).fit()
# predictions = model1.predict(x1, x2, x3, x4)
# print model5.summary()