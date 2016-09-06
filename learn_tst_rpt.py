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
pdb.set_trace()

# I should get cmd line args:
trainsize_i = int(sys.argv[1].split('=')[1])
testyear_s  = sys.argv[2].split('=')[1]
'bye'
