#!/bin/bash

# many_learn_test.bash 

# Demo:
# ./many_learn_test.bash TRAINSIZE=25 1990 SLOPES='[2,3,4,5,6,7,8,9]'

# This script should build two types of ML models:
# Linear   Regression
# Logistic Regression
# from GSPC prices from Yahoo.
# Then it should show a comparison of predictive effectiveness from the models.

# If you have questions, e-me: bikle101@gmail.com

# I should create a folder to hold temporary data:

if [ $# -ne 3 ]
then
    echo You typed something wrong.
    echo try something like this:
    echo ./many_learn_test.bash TRAINSIZE=25 2010 SLOPES='[2,3,4,5,6,7,8,9]'
    exit 1
fi

mkdir -p /tmp/mlapp11/

# setup:
rm -f /tmp/mlapp11/many_predictions_linr.csv
rm -f /tmp/mlapp11/many_predictions_logr.csv
# I should loop through a range of years:

for year in `seq $2 2016`
do
  echo Gathering predictions for: $year
  ./learn_test.bash $1 TESTYEAR=$year $3 > /dev/null 2>&1
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
echo _
echo Aggregate Effectiveness Report
${HOME}/anaconda3/bin/python rpt_linr.py
${HOME}/anaconda3/bin/python rpt_logr.py


exit
