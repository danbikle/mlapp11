# learn_tst_rpt.py

# This script should learn from observations in /tmp/mlapp11/feat.csv

# Then it should test its learned models on observations later than the training observations.

# Next it should report effectiveness of the models.

# Demo:
# ~/anaconda3/bin/python genf.py TRAINSIZE=30 TESTYEAR=2015

# Above demo will train from years 1985 through 2014 and predict each day of 2015

import numpy  as np
import pandas as pd
import pdb

# I should check cmd line args
import sys
if (len(sys.argv) != 3):
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
test_sr  = (feat_df.cdate > test_start_s)  & (feat_df.cdate < test_end_s)
train_df = feat_df[train_sr]
test_df  = feat_df[test_sr]

# I should build a Linear Regression model from slope columns in train_df:
x_train_a = np.array(train_df)[:,3:]
y_train_a = np.array(train_df.pctlead)
from sklearn import linear_model
linr_model = linear_model.LinearRegression()
# I should learn:
linr_model.fit(x_train_a, y_train_a)

# Now that I have learned, I should predict:
x_test_a       = np.array(test_df)[:,3:]
predictions_a  = linr_model.predict(x_test_a)
predictions_df = test_df.copy()

# I should create a CSV to report from:
predictions_df['predictions'] = predictions_a.reshape(len(predictions_a),1)
predictions_df.to_csv('/tmp/mlapp11/predictions_linr.csv', float_format='%4.3f', index=False)

# I should build a Logistic Regression model.
logr_model    = linear_model.LogisticRegression()
# I should get classification from y_train_a:
class_train_a = (y_train_a > np.median(y_train_a))
# I should learn:
logr_model.fit(x_train_a, class_train_a)

# Now that I have learned, I should predict:
predictions_a  = logr_model.predict(x_test_a)
predictions_df = test_df.copy()

# I should create a CSV to report from:
predictions_df['predictions'] = predictions_a.reshape(len(predictions_a),1)
predictions_df.to_csv('/tmp/mlapp11/predictions_logr.csv', float_format='%4.3f', index=False)

# I should report long-only-effectiveness:
linr_df = pd.read_csv('/tmp/mlapp11/predictions_linr.csv')
print('Long-Only-Effectiveness:')
print(np.sum(linr_df.pctlead))

# I should report Linear-Regression-Effectiveness:
eff_sr  = linr_df.pctlead * np.sign(linr_df.predictions)
print('Linear-Regression-Effectiveness:')
print(np.sum(eff_sr))

# I should report Logistic-Regression-Effectiveness:
logr_df = pd.read_csv('/tmp/mlapp11/predictions_logr.csv')
pos_df  = logr_df[logr_df.predictions]
neg_df  = logr_df[~logr_df.predictions]
pos_f   = np.sum(pos_df.pctlead)
neg_f   = np.sum(neg_df.pctlead)
print('Logistic-Regression-Effectiveness:')
print(pos_f-neg_f)

'bye'
