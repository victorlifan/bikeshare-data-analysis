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
