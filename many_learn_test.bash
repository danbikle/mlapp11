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

./learn_test.bash TRAINSIZE=25 TESTYEAR=1990 SLOPES='[2,3,5,9,17]'
cat /tmp/mlapp11/predictions_linr.csv >> /tmp/mlapp11/many_predictions_linr.csv
cat /tmp/mlapp11/predictions_logr.csv >> /tmp/mlapp11/many_predictions_logr.csv

./learn_test.bash TRAINSIZE=25 TESTYEAR=1991 SLOPES='[2,3,5,9,17]'
cat /tmp/mlapp11/predictions_linr.csv >> /tmp/mlapp11/many_predictions_linr.csv
cat /tmp/mlapp11/predictions_logr.csv >> /tmp/mlapp11/many_predictions_logr.csv

exit


