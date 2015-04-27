"""
Copyright: Copyright (C) 2015 Baruch College - MTH 9899 Machine Learning
Description: Sample code from Quantopian using previous 10 bars' movements to predict the next movement
"""

# python imports

from collections import deque
import numpy as np

# scipy learn imports

from sklearn.ensemble import RandomForestClassifier


def initialize(context):
    ''' 
    @summary: standard initialization function in Quantipian 
    @param context: a container to save data
    '''

    # Security universe setting
    # A more readable way will be 
    #
    # context.securities = symbols('AAPL', 'MSFT')
    #
    # Finally, we will extend the universe as S&P100, or NYSE100

    context.security = sid(698)

    # Machine Learning setting

    # algo selection
    # we will do research do other algos as well
    # e.g. 
    # Linear model, classifier = linear_model.LinearRegression()
    # SVM, classifier = svm.SVC()
    # Nearest neighbor, classifier = NearestCentroid()

    context.classifier = RandomForestClassifier()
    
    # ML algo uses historical price to learn
    # define historical period to look back

    context.window_length = 10 
    
    # Other containers as cache

    context.recent_prices = deque(maxlen=context.window_length+2) # Stores recent prices
    context.X = deque(maxlen=500) # Independent, or input variables
    context.Y = deque(maxlen=500) # Dependent, or output variable
    context.prediction = 0        # Stores most recent prediction
    


def handle_data(context, data):
    ''' 
    @summary: main part to define trades, which is run every backtesting day
    @param context: container including all initialization data
    @param data: dict to read equity data
    ''' 

     # Update the recent prices

    context.recent_prices.append(data[context.security].price)
    
    # If there's enough recent price data (if not, there would not be enough historical data to look back)

    if len(context.recent_prices) == context.window_length+2: 
        
        # Define independent and dependent variables

        changes = np.diff(context.recent_prices) > 0
        context.X.append(changes[:-1]) 
        context.Y.append(changes[-1])
        
        # Wait until the there is enough data to make a good model

        if len(context.Y) >= 100: 

            # Fit model and predict tomorrow's trend

            context.classifier.fit(context.X, context.Y)
            context.prediction = context.classifier.predict(changes[1:]) # Predict
            
            # If prediction = 1, implies up, buy all shares
            # If prediction = 0, implies down, sell all shares

            order_target_percent(context.security, context.prediction)
            record(prediction=int(context.prediction))