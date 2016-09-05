# genf.py

# Demo:
# ~/anaconda3/bin/python genf.py TRAINSIZE=30 SLOPES='[3,5,9,17]'

# This script should build two types of ML models:
# Linear   Regression
# Logistic Regression
# from GSPC prices from Yahoo.
# Then it should show a comparison of predictive effectiveness from the models.

# TRAINSIZE should specify years of training data to learn from.
# SLOPES should specify moving-avg durations, in days, which I compute slopes from.
# I should have at least two SLOPE values and they should be between 2 and 32.

# If you have questions, e-me: bikle101@gmail.com

import numpy  as np
import pandas as pd
import pdb

# I should check cmd line arg
import sys
pdb.set_trace()
if (len(sys.argv) < 3):
  print('Demo:')
  print("~/anaconda3/bin/python genf.py TRAINSIZE=30 SLOPES='[3,5,9,17]'")
  print('...')
  sys.exit()
