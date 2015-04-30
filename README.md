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
   - Nearest Neighbors (http://scikit-learn.org/stable/modules/neighbors.html)
   - Random Forests (http://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees)
   - Support Vector Machine (http://scikit-learn.org/stable/modules/svm.html)
 - Technical Strategies
   - Bollinger Band
   - Momentum
   - Rotated Relative Graph

### Books and Papers reference
 - Alpaydin, Ethem. *Introduction to machine learning.* MIT press, 2014.
 - Aronson, David. *Evidence-based technical analysis: applying the scientific method and statistical inference to trading signals.* Vol. 274. John Wiley & Sons, 2011.
