
def convert_to_days():
    hours = int(input("Hours:"))
    minutes = int(input("Minutes:"))
    seconds = int(input("Seconds:"))
    days = get_days(hours,minutes,seconds)
    print(f"the aproximate number of days is {round(days, 4)} day.")
    
def get_days(hours,minutes, seconds):
    days = (hours/24) + (minutes/1440) + (seconds/86400)
    return days
    
convert_to_days()    