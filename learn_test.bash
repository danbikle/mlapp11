#!/bin/bash

# learn_test.bash

# Demo:
# ./learn_test.bash TRAINSIZE=30 TESTYEAR=2015 SLOPES='[3,5,9,17]'

# This script should build two types of ML models:
# Linear   Regression
# Logistic Regression
# from GSPC prices from Yahoo.
# Then it should show a comparison of predictive effectiveness from the models.

# TRAINSIZE should specify years  of training data to learn from.
# TESTYEAR  should specify a year of observations which I want to predict.
# SLOPES should specify moving avg durations, in days, which I compute slopes from.
# I should have at least two SLOPE values and they should be between 2 and 32.

# If you have questions, e-me: bikle101@gmail.com

# I should create a folder to hold temporary data:
mkdir -p /tmp/mlapp11/

# I should get prices from Yahoo:
# debug
# /usr/bin/curl http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC > /tmp/mlapp11/gspc.csv
# debug

# I should extract two columns and also sort:
echo cdate,cp                                                       > /tmp/mlapp11/gspc2.csv
sort /tmp/mlapp11/gspc.csv|awk -F, '{print $1"," $5}'|grep -v Date >> /tmp/mlapp11/gspc2.csv

# I should compute features from the prices:

if [ $# -ne 3 ]
then
  echo
  echo "You typed something wrong."
  echo "Try something like this:"
  echo "Demo:"
  echo "./learn_test.bash TRAINSIZE=30 TESTYEAR=2015 SLOPES='[3,5,9,17]'"
  exit 1
fi

${HOME}/anaconda3/bin/python genf.py $3

# I should learn, test, and report:
${HOME}/anaconda3/bin/python learn_tst_rpt.py $1 $2

exit


