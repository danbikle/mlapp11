readme.txt

This app should build a Machine Learning App which compares
effectiveness of GSPC predictions computed from Linear Regression and
Logistic Regression.

An example of seeing the comparison can be done with this shell command:

./many_learn_test.bash TRAINSIZE=25 2010 SLOPES='[2,3,4,5,6,7,8,9]'

The above command will gather two types of predictions for several years.

Then it will report on the effectiveness of each type.

The TRAINSIZE parameter allows me to specify how many years of observations to learn from.

Each year contains about 251 observations.

The SLOPES parameter allows me to specify the complexity of the predictive model.

If SLOPES='[2,3,4,5]',
I get a simpler model than if I use a setting like this:
SLOPES='[2,3,4,5,6,7,8,9]'

Each slope value should be between 2 and 32.

A slope value drives calculation of a slope of a moving average for each observation.

I use slope of a moving average because I believe that if slope is negative then I have entered a situation when I should be bullish.

Clone this repo with this shell command:

git clone https://github.com/danbikle/mlapp11

The scripts in this repo should work if you are on Linux and you have installed anaconda3.

The Anaconda download is at the URL listed below:

https://www.continuum.io/downloads

A download link I like:

https://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh

This should work:

/usr/bin/curl repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh > ~/Anaconda3-4.1.1-Linux-x86_64.sh
bash ~/Anaconda3-4.1.1-Linux-x86_64.sh

If you have questions, e-me: bikle101@gmail.com

