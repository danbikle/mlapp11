# rpt_logr.py

# This script should report effectiveness of Linear Regression.
import pandas as pd
import numpy  as np

# First, I should report long-only-effectiveness:
logr_df = pd.read_csv('/tmp/mlapp11/many_predictions_logr.csv')
#print('Long-Only-Effectiveness:')
#print(np.sum(logr_df.pctlead))

# I should report Logistic-Regression-Effectiveness:
logr_df = pd.read_csv('/tmp/mlapp11/predictions_logr.csv')
pos_df  = logr_df[logr_df.predictions]
neg_df  = logr_df[~logr_df.predictions]
pos_f   = np.sum(pos_df.pctlead)
neg_f   = np.sum(neg_df.pctlead)
print('Logistic-Regression-Effectiveness:')
print(pos_f-neg_f)
