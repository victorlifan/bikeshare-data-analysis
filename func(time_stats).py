#import time
#import pandas as pd
#import numpy as np




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    com_month_num = df['month'].mode()[0]
    com_month_name = ['january','february','march','april','may','june']
    print('The most popular month is: ',com_month_name[com_month_num-1])
    # display the most common day of week
    com_day = df['day_of_week'].mode()[0]
    print('The most popular hour day: ',com_day)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    com_hr = df['hour'].mode()[0]
    print('The most popular hour is: ',com_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
