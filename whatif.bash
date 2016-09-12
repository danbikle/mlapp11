#!/bin/bash

# whatif.bash

# This script helps me answer: 'Whatif price is $x?'

# Demo:
# ./whatif.bash TRAINSIZE=25 SLOPES='[2,3,5,9,17]' 2123.40

if [ $# -ne 3 ]
then
  echo
  echo "You typed something wrong."
  echo "Try something like this:"
  echo "Demo:"
  echo "./whatif.bash TRAINSIZE=25 SLOPES='[2,3,5,9,17]' 2123.40"
  exit 1
fi

# I should create a folder to hold temporary data:
mkdir -p /tmp/mlapp11/

# I should get prices from Yahoo:
/usr/bin/curl http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC > /tmp/mlapp11/gspc.csv

# I should extract two columns and also sort:
echo cdate,cp                                                       > /tmp/mlapp11/gspc2.csv
sort /tmp/mlapp11/gspc.csv|awk -F, '{print $1"," $5}'|grep -v Date >> /tmp/mlapp11/gspc2.csv
# I should add the whatif price:
tail -1 /tmp/mlapp11/gspc2.csv >> /tmp/mlapp11/gspc2.csv
sed -i "$ s/,.*/,$3/" /tmp/mlapp11/gspc2.csv

# I should compute features from the prices:
${HOME}/anaconda3/bin/python genf.py $2

# I should learn, test, and report:
${HOME}/anaconda3/bin/python learn_tst_rpt.py $1 TESTYEAR=`date +%Y`

echo _
echo whatif price is $3
echo logr prediction:
tail -1 /tmp/mlapp11/predictions_logr.csv
echo linr prediction:
tail -1 /tmp/mlapp11/predictions_linr.csv
echo _

exit
