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
