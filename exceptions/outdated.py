month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    input_date = input("Date: ")
    try:
        if '/' in input_date:
            input_date = input_date.strip()
            month, day, year = input_date.split('/')
            # if input_date contains '/' and month is in month_names list, repropmt the user
            if month in month_names:
                pass
            # Check if day and month are valid, if not reprompt the user
            elif (int(month) > 12) or (int(day) > 31): 
                pass
            else:
                print(year + "-" + month.zfill(2) + "-" + day.zfill(2))
                break
        elif ',' in input_date:
            date = input_date.replace(',','')
            month, day, year = date.split(' ')
            # If input_date contains ',' and month is a digi, reprompt the user
            if month.isdigit():
                continue
            # Check if day and month are valid, if not reprompt the user
            elif (month_names.index(month)+1 > 12) or (int(day) > 31): 
                continue
            else:
                month_number = str(month_names.index(month)+1)
                print(year + "-" + month_number.zfill(2) + "-" + day.zfill(2))
                break
    except EOFError:
        exit()
        ... 