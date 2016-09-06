# learn_tst_rpt.py

# This script should learn from observations in /tmp/mlapp11/feat.csv

# Then it should test its learned models on observations later than the training observations.

# Next it should report effectiveness of the models.

# Demo:
# ~/anaconda3/bin/python genf.py TRAINSIZE=30 TESTYEAR=2015

# Above demo will train from years 1984 through 2014 and predict each day of 2015

import numpy  as np
import pandas as pd
import pdb

# I should check cmd line args
import sys
if (len(sys.argv) != 3):
  pdb.set_trace()
  print('You typed something wrong:')
  print('Demo:')
  print("~/anaconda3/bin/python genf.py TRAINSIZE=30 TESTYEAR=2015")
  sys.exit()

# I should get cmd line args:
trainsize     = int(sys.argv[1].split('=')[1])
testyear_s    =     sys.argv[2].split('=')[1]
train_end_i   = int(testyear_s)
train_end_s   =     testyear_s
train_start_i = train_end_i - trainsize
train_start_s = str(train_start_i)
# train and test observations should not overlap:
test_start_i  = train_end_i
test_start_s  = str(test_start_i)
test_end_i    = test_start_i+1
test_end_s    = str(test_end_i)

feat_df  = pd.read_csv('/tmp/mlapp11/feat.csv')
train_sr = (feat_df.cdate > train_start_s) & (feat_df.cdate < train_end_s)
train_df = feat_df[train_sr]
test_sr  = (feat_df.cdate > test_start_s) & (feat_df.cdate < test_end_s)
pdb.set_trace()
test_sr.tail()
len(test_sr)

'bye'
