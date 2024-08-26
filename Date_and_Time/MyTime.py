# Epoch - Time since 1st Jan 1970 till now
# Ticks - seconds in floating point representation
# DST - Daylight Savings Time
# Time module stores time in the form of tuple

# Index             Field                           Representation

# 0                 Year(4 digits)                  2024
# 1                 Month(s)                        1 to 12
# 2                 Day(s)                          1 to 31
# 3                 Hour(s)                         0 to 23
# 4                 Minute(s)                       0 to 59
# 5                 Seconds(s)                      0 to 61 (if its a leap year)
# 6                 Day of Week                     0 to 6  (Monday to Sunday)
# 7                 Day of the year                 1 to 366
# 8                 DST                             -1 0 1


import time
# import calendar
# print(time.time())

# print(time.localtime())
# day = time.localtime().tm_wday
# wday = None
# if day == 0:
#     wday = 'Mon'
# months = time.localtime().tm_mon
# mon =None
# if months == 8:
#     mon = 'Aug'
# print(f"{wday} {mon} {time.localtime().tm_mday} {time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec} {time.localtime().tm_year} ")

# print(time.asctime())

# print(calendar.calendar(2026))

for i in range (1,6):
    print (i,end="")
    print(".", end="")
    time.sleep(0.5) 
    print(".", end="")
    time.sleep(0.5) 
    print(".", end="")
    time.sleep(0.5) 
       

    
