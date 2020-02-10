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
    print('''Hello! Let\'s explore some US bikeshare data!\nPlease enter the following in their lowercase and unabbreviated forms.''')
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


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    raw_data =input('Would you like to see some raw data?(type y or n): ')
    count = 0
    while True:
        if raw_data == 'y':
            print(df.iloc[count:count+5])
            count += 5
            raw_data = input('Whould you like to see some more?(type y or n): ')
        elif raw_data == 'n':
            break
        else:
            raw_data = input('''Plese answer 'y' or 'n':''')


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


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


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_tra = df['Trip Duration'].sum()
    print('Total travel time is: ',tot_tra,' seconds.')

    # display mean travel time
    mean_tra = df['Trip Duration'].mean()
    print('Average travel time is: ',mean_tra,' seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    cut = df['User Type'].value_counts()
    print(cut)

    # Display counts of gender
    try:
        cg = df['Gender'].value_counts()
        print(cg)
    except KeyError:
        print('''Sorry, we don't have data on gender in this city.''')

    # Display earliest, most recent, and most common year of birth
    try:
        e_bt = df['Birth Year'].min()
        r_bt = df['Birth Year'].max()
        c_bt = df['Birth Year'].mode()[0]
        print('''The earliest year of birth is {},
    the most recent yaer of birth is {}
    and the mose common year of birth is {}'''.format(e_bt,r_bt,c_bt))
    except KeyError:
        print('''Sorry, we don't have data on birth year in this city.''')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
