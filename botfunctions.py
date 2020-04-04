#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:48:48 2020
@author: Aaron Necaise
"""
import pandas as pd
from datetime import datetime, timedelta

# %%
def insertPurchase(purchase_price, author):

    data = pd.read_csv('data.csv', index_col=0)
    insert = pd.DataFrame(data =  {'Purchase Price':[purchase_price],
                                    'Sell Price':[0],
                                    'Time':[pd.datetime.now()],
                                    'Author Name':[author]})
    
    print(f'Saving : Purchase Price {purchase_price}, Time: {pd.datetime.now()}, Author: {author}')
    data = pd.concat([data, insert], ignore_index=True)
    data.head()
    data.to_csv('data.csv')
    print('Finished!')
    
    
def insertSell(sell_price, author):

    data = pd.read_csv('data.csv', index_col=0)
    insert = pd.DataFrame(data =  {'Purchase Price':[0],
                                    'Sell Price':[sell_price],
                                    'Time':[pd.datetime.now()],
                                    'Author Name':[author]})
    
    print(f'Saving : Sell Price {sell_price}, Time: {pd.datetime.now()}, Author: {author}')
    data = pd.concat([data, insert], ignore_index=True)
    data.head()
    data.to_csv('data.csv')
    print('Finished!')
    
        
def getPrices():
    
    # import database
    data = pd.read_csv('data.csv')
    
    # Set time variables to today and noon for comparison
    today = datetime.now().date()
    noon = datetime.today().replace(hour=12, minute=0, second=0, microsecond=0)
    time = datetime.today()
    data.Time = pd.to_datetime(data.Time)
    
    # Get only prices from today
    recent = data[ [data.Time[i].date() ==  today for i in range(len(data)) ]]
    
    # If the current time is past noon, only return afternoon prices
    if time >= noon:
        recent = recent[ recent.Time >  noon ]
    
    # Drop duplicates by user. Only keeping a users most updated value
    # This way, if a user makes a mistake, they can re-enter
    recent = recent.sort_values(by='Time', ascending=False)
    recent = recent.drop_duplicates(['Author Name'], keep='first')
    recent = recent.sort_values(by='Sell Price', ascending=False)
    
    recent = recent[['Author Name', 'Sell Price']]
    
    return recent

def resetTracker():
    
    # Get current week number
    today = datetime.today().date()
    year, week, day = today.isocalendar()
    
    # Find Weeknumber of the data
    data = pd.read_csv('data.csv')
    data.Time = pd.to_datetime(data.Time)
    data['week'] = 0
    for i, val in enumerate(data.Time):
        year, week, day = va
    
def showTrend(player_name):
    # trends by user
# %%

import pandas as pd
insertPurchase(11, 'aaron')

data = pd.DataFrame(data =  {'Purchase Price':[0],
                                       'Sell Price':[0],
                                       'Time':[pd.datetime.now()],
                                       'Author Name':['admin']})

data.to_csv('data.csv')
data = pd.read_csv('data.csv', index_col=0)
