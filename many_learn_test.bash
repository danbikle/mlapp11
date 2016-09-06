#!/bin/bash

# many_learn_test.bash 

# Demo:
# ./many_learn_test.bash

# This script should build two types of ML models:
# Linear   Regression
# Logistic Regression
# from GSPC prices from Yahoo.
# Then it should show a comparison of predictive effectiveness from the models.

# If you have questions, e-me: bikle101@gmail.com

# I should create a folder to hold temporary data:
mkdir -p /tmp/mlapp11/

# setup:
rm -f /tmp/mlapp11/many_predictions_linr.csv
rm -f /tmp/mlapp11/many_predictions_logr.csv
# I should loop through a range of years:

for year in `seq 1990 2016`
do
  echo Gathering predictions for: $year
  ./learn_test.bash TRAINSIZE=25 TESTYEAR=$year SLOPES='[2,3,5,9,17]'
  cat /tmp/mlapp11/predictions_linr.csv >> /tmp/mlapp11/many_predictions_linr.csv
  cat /tmp/mlapp11/predictions_logr.csv >> /tmp/mlapp11/many_predictions_logr.csv
done

head -1 /tmp/mlapp11/many_predictions_linr.csv        > /tmp/mlapp11/tmp.csv
grep -v cdate /tmp/mlapp11/many_predictions_linr.csv >> /tmp/mlapp11/tmp.csv
mv /tmp/mlapp11/tmp.csv /tmp/mlapp11/many_predictions_linr.csv

head -1 /tmp/mlapp11/many_predictions_logr.csv        > /tmp/mlapp11/tmp.csv
grep -v cdate /tmp/mlapp11/many_predictions_logr.csv >> /tmp/mlapp11/tmp.csv
mv /tmp/mlapp11/tmp.csv /tmp/mlapp11/many_predictions_logr.csv

# I should report:
${HOME}/anaconda3/bin/python rpt_linr.py
${HOME}/anaconda3/bin/python rpt_logr.py


exit
