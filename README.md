# ML-algotrade
Project Title: Algorithmic Trading with Machine Learning

## Project Proposal
Group project for Baruch MTH 9899 - Big Data II: Machine Learning

### Project Member
 - Weiyi Chen, weiyi.chen@baruchmail.cuny.edu
 - Yifan Cui, yifan.cui@baruchmail.cuny.edu
 - Chengbin Wang, chengbin.wang@baruchmail.cuny.edu
 - Haotian Wu, haotian.wu@baruchmail.cuny.edu

### Data Set and Software: Quantopian
Quantopian is our main research and backtesting platform, we research algorithmic trading ideas and explore curated financial data with the assistance of machine learning algorithm in this hosted research environment. Quantopian supports flexible data access, custom plotting, and post-hoc analysis on backtest. 

For convenience to verify our machine learning algorithms by cheating ('cheat' is like using today's data to forecast today), we also support local access to data from Yahoo, with event study and backtesting tools from Python module QuantSoftware Toolkit. In concludes,

 - Data input
   - Quantopian, or Yahoo
   - Equity Universe: adjusted close of S&P500 index equity component
   - Frequency: daily
 - Software
   - Quantopian, a platform to build, test, and execute trading algorithms.
   - QuantSoftware Toolkit, a modified Python-based open source software framework designed to support portfolio construction and management

### Programming Language
Python. The requirement of this course suggests Matlab, but we request for using Python because our preferred platform Quantopian is using Python and the Python module QSTK we will be using is also in Python.

The main module we will be using is scipy-learn (http://scikit-learn.org/stable/supervised_learning.html#supervised-learning), which contains implemented Machine Learning algorithms.

### Project Idea
Use different machine learning algorithms to modify traditional technical strategies, and backtest with research in cycle to find a good algorithm,
 - Machine Learning algorithms
   - Nearest Neighbors, http://scikit-learn.org/stable/modules/neighbors.html
   - Random Forests, http://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees
   - Support Vector Machine, http://scikit-learn.org/stable/modules/svm.html
 - Technical Strategies
   - Bollinger Band
   - Momentum
   - Rotated Relative Graph

### Books and Papers reference
 - Alpaydin, Ethem. *Introduction to machine learning.* MIT press, 2014.
 - Aronson, David. *Evidence-based technical analysis: applying the scientific method and statistical inference to trading signals.* Vol. 274. John Wiley & Sons, 2011.


## Installation Guide
Repository

### System Requirements
Make sure your system meets these requirements:
  - Operating system: MacOS 10.9 10.10 (it has been tested successfully on these)
  - RAM: 2GB.
  - Disk space: 2GB

### Step 1: Install Command Line Tools
  - Open terminal, type “xcode-select --install” in terminal (without quotes)
  - A pop-up windows will appear asking you about install tools, choose install tools, wait install to finish
  
### Step 2: Install Homebrew

  ```
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  brew tap samueljohn/python
  brew tap homebrew/science
  ```

### Step 3: Install gcc and its libraries

  ```
  brew install gcc
  ```

### Step 4: Install Python and its modules
    
  ```
  brew install python
  
  pip install virtualenv
  pip install nose
  pip install pyparsing
  pip install python-dateutil
  
  pip install numpy
  pip install scipy
  pip install matplotlib
  
  pip install pandas
  pip install scikits.statsmodels
  pip install scikit-learn
  pip install QSTK
  ```

### Step 4: Install Sublime IDE and Fix Mac Path (other systems no need to fix)

  ```
  brew install sublime
  git clone https://github.com/int3h/SublimeFixMacPath.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/FixMacPath
  ```

### Step 5: Clone AlgoTrading and Overwrite QSTK package

  ```
  git clone https://github.com/weiyialanchen/AlgoTrading.git
  cp -r AlgoTrading/* /usr/local/lib/python2.7/site-packages/QSTK/
  rm -r AlgoTrading/
  ```

### Step 6: Set up alias to working directory

Note that your working directory is /usr/local/lib/python2.7/site-packages/QSTK/, to make alias

  ```
  subl ~/.bash_profile
  ```

  Append the following line to the file

  ```
  alias AlgoTrading='cd /usr/local/lib/python2.7/site-packages/QSTK/'
  ```
  
  Save, exit and restart the terminal. Next time when you want to go to the working folder and open it, just run

  ```
  AlgoTrading
  subl ./
  ```
