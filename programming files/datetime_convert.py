from datetime import datetime
#declares a specific date and time as a string, is not the current date and time
date_str = "2022-03-17 10:45:30"
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
#formatts
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')
#prints the formatted string
print(formatted_date)
