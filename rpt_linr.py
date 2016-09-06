# rpt_linr.py

# This script should report effectiveness of Linear Regression.
import pandas as pd
import numpy  as np

# First, I should report long-only-effectiveness:
linr_df = pd.read_csv('/tmp/mlapp11/many_predictions_linr.csv')
print('Long-Only-Effectiveness:')
print(np.sum(linr_df.pctlead))

# I should report Linear-Regression-Effectiveness:
eff_sr  = linr_df.pctlead * np.sign(linr_df.predictions)
print('Linear-Regression-Effectiveness:')
print(np.sum(eff_sr))
