months = ["January", "February", "March", "April", "May", "June", "July", 
              "August", "September", "October", "November", "December"]
while True:
    date = input("Date: ")
    try:
        if "/" in date:
           month, day, year = date.split("/")
           m = int(month)
           d = int(day)
           y = int(year)

        elif "," in date:
            date = date.replace(",", "")
            month, day, year = date.split(" ")
            if month in months:
                month = months.index(month) + 1
                m = int(month)
                d = int(day)
                y = int(year)
                
        if (0 < m <= 12) and (0 < d <= 31) and (1000 <= y <= 9999):
            break
        else: 
            continue   
                                                      
    except (NameError, ValueError):
        pass    
    
print(f"{y}-{m:02}-{d:02}")
