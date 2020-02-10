import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('''Hello! Let\'s explore some US bikeshare data!\nPlease enter the following inputs in thier lowercase and unabbreviated forms.''')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Choose one city from chicago, new york city, washington hit enter when you are done:')
    while True:
        if city in ['chicago','new york city','washington']:
            break
        else:
            city = input('Please choose ONE city from chicago, new york city, washington and type the full name in LOWER case:')



    # get user input for month (all, january, february, ... , june)
    month = input('''Enter 'all' if you want to see data from all the months\nor specify the month you want to know (upto june):''')
    while True:
        if month in ['all','january','february','march','april','may','june']:
            break
        else:
            month = input('''Please enter 'all' or enter one month (upto june) you like to know in lowercase unabbreviated format:''')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('''Enter 'all' if you want to see data from whole week\nor specify the day of week you want to know:''')
    while True:
        if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
        else:
            day = input('''Please enter 'all' or enter one day of week you like to know in lowercase unabbreviated format:''')


    print('-'*40)
    return city, month, day
#get_filters()
