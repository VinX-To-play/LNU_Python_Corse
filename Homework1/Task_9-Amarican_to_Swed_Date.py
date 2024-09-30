user_string = input('Enter a date in American format:')

if len(user_string) != 8:
    print('wrong format, pleas use: DD/MM/YYYY')

else:
    usDD = user_string[0:1]
    usMM = user_string[3:4]
    usYY = user_string[6:7]
    
    swe_date = usYY + '/' + usMM + '/' + usDD
    
    print('Swedish date is:', swe_date )