import time
import pandas as pd
import numpy as np
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    com_start = df['Start Station'].mode()[0]
    print('Most commonly used start station is: ',com_start)

    # display most commonly used end station
    com_end = df['End Station'].mode()[0]
    print('Most commonly used end station is: ',com_end)

    # display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + df['End Station']
    com_comb = df['start_end_station'].mode()[0]
    print('Most frequent combination of start station and end station trip is: ',com_comb)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
