#!/usr/bin/env python

"""
Usage: ./day5-lunch2.py <day5-lunch.bed> 

Average the signal over each region using bigWigAverageOverBed which can be found in /usr/local/Cellar/ucsc-genome-browser/316/bin
Remember: Running with no options will usually display usage


"""

import sys
import pandas as pd

df = pd.read_csv( sys.argv[1], sep="\t" )

