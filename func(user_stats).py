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
