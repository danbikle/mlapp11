# genf.py

# Demo:
# ~/anaconda3/bin/python genf.py SLOPES='[3,5,9,17]'

# This script should build two types of ML models:
# Linear   Regression
# Logistic Regression
# from GSPC prices from Yahoo.
# Then it should show a comparison of predictive effectiveness from the models.

# SLOPES should specify moving-avg durations, in days, which I compute slopes from.
# I should have at least two SLOPE values and they should be between 2 and 32.

# If you have questions, e-me: bikle101@gmail.com

import numpy  as np
import pandas as pd
import pdb

# I should check cmd line arg
import sys
if (len(sys.argv) != 2):
  pdb.set_trace()
  print('You typed something wrong:')
  print('Demo:')
  print("~/anaconda3/bin/python genf.py SLOPES='[3,5,9,17]'")
  sys.exit()
arg1_l = sys.argv[1].split('=')
if (arg1_l[0] != 'SLOPES'):
  print('Problem:')
  print('I cannot determine SLOPES from your command line.')
  print('Demo:')
  print("~/anaconda3/bin/python genf.py SLOPES='[3,5,9,17]'")
  sys.exit()

slopes_s = arg1_l[1]
slopes_a = []
for slope_s in slopes_s.split(','):
    slope_i = int(slope_s.replace('[','').replace(']',''))
    slopes_a.append(slope_i)

gspc_df = pd.read_csv('/tmp/mlapp11/gspc2.csv')

# I should compute pctlead:
gspc_df['pctlead'] = (100.0 * (gspc_df.cp.shift(-1) - gspc_df.cp) / gspc_df.cp).fillna(0)

# I should compute mvgavg for each slope_i

# ref:
# http://www.ml4.us/cclasses/class03pd41
# http://pandas.pydata.org/pandas-docs/stable/computation.html#rolling-windows
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling

for slope_i in slopes_a:
  pdb.set_trace()
  slope_i
  rollx = gspc_df.rolling(window=slope_i)
  key_s = 'mvgavg'+slope_i

'bye'
