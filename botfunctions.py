#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:48:48 2020
@author: Aaron Necaise
"""
import pandas as pd
from datetime import datetime, timedelta
import matplotlib

# %%
def insertPurchase(purchase_price, author):
    """
    
    purchase price command fucntions. Saves data to this week database.

    """
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
    """
    
    purchase price command fucntions. Saves data to this week database.

    """

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
    
        
def getPrices(type_flag = 'Sell Price'):
    """
    

    Returns
    -------
    recent : Dataframe
        Table of the most recent turnips prices sorted from highest to lowest

    """
    
    # import database
    data = pd.read_csv('data.csv',  index_col=0)
    
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
    recent = recent.sort_values(by=type_flag, ascending=False)
    
    recent = recent[['Author Name', type_flag]]
    
    return recent

def weeklyUpdate():
    """
    
    Run during new week or wheneber bot is initialized. 
    Saves all previous weeks data in a archived database. 
    

    """
    # Get current week number
    today = datetime.today().date()
    year, week, day = today.isocalendar()
    
    # Find Weeknumber of the data
    data = pd.read_csv('data.csv', index_col=0)
    data.Time = pd.to_datetime(data.Time)
    data['week'] = 0
    for i, val in enumerate(data.Time):
        year, week1, day = val.isocalendar()
        data.week[i] = week1
    
    # Get data for turnips this week and separate that from previous weeks
    
    archive = data[data.week!=week].drop(columns='week')
    data = data[data.week == week].drop(columns='week')
    
    
    # Resets weekly tracker 
    if len(data) == 0 :
        print('Resetting this weeks data')
        data = pd.DataFrame(data =  {'Purchase Price':[0],
                                                'Sell Price':[0],
                                                'Time':[pd.datetime.now()],
                                                'Author Name':['admin']})
        
        data.to_csv('data.csv')
    else:
        print('Getting this weeks numbers...')
        data.to_csv('data.csv')
    
    # Archives old Data
    if len(archive) != 0:
        print('Archiving last weeks data')
        past = pd.read_csv('archive.csv', index_col=0)
        past = pd.concat([past, archive], ignore_index=True)
        past.to_csv('archive.csv')
    
def getAllData():
    """ 
    Combines this weeks data with archived data
    """
    thisWeek = pd.read_csv('data.csv', index_col=0)
    archived = pd.read_csv('archive.csv', index_col=0)
    
    allData = pd.concat([thisWeek, archived], ignore_index=True, sort=False)
    
    return allData
    
def showTrend(player_name):
    
    data = pd.read_csv('data.csv', index_col=0)
    data.Time = pd.to_datetime(data.Time)
    data = data[data['Author Name']==player_name]
    
    
    
    
# %%


# data = pd.DataFrame(data =  {'Purchase Price':[0],
#                                         'Sell Price':[0],
#                                         'Time':[pd.datetime.now()],
#                                         'Author Name':['admin']})

# data.to_csv('data.csv')
data = pd.read_csv('data.csv', index_col=0)
