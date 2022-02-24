
from typing import final


def add_time(start_time, duration_time, day = False):
    # Dictionaries Containing Week and Containing am/pm flip
    Days_of_week = {'monday': '0', 'tuesday': '1', 'wednesday': '2', 'thursday': '3', 'friday': '4', 'saturday': '5', 'sunday': '6'}
    New_Day = {'0': 'Monday', '1': 'Tuesday', '2': 'Wednesday', '3': 'Thursday', '4': 'Friday', '5': 'Saturday', '6': 'Sunday'}
    am_pm_flip = {'AM': 'PM', 'PM': 'AM'}

    # Extracts Time and am/pm value from start_time
    start_time = start_time.split()
    am_pm = start_time[1]
    start_time = start_time[0]
    if len(start_time) < 5 :
        start_time = '0' + start_time
    
    start_hour = int(start_time[:2])
    star_minute = int(start_time[3:])
    
    # Extracts time from duration_time 
    if len(duration_time) < 5 : 
        duration_time = '0' + duration_time
    duration_time = duration_time.split(':')
    duration_hr = int(duration_time[0])
    duration_minute = int(duration_time[1])

    # Final Minutes
    final_minutes = duration_minute + star_minute
    if final_minutes >= 60:
        start_hour += 1
        final_minutes = final_minutes % 60
    if final_minutes <= 9:
        final_minutes = '0' + str(final_minutes)
    else: final_minutes

    # Final Hours 
    final_hour = (start_hour + duration_hr) % 12
    if final_hour == 0: final_hour = 12 
    else: final_hour

    # Final Time
    final_time = str(final_hour) + ':' + str(final_minutes)

    # If time is @ pm and there is a change into new day it counts that as one day passing 
    amount_of_days = int((duration_hr)/24)
    if am_pm == 'PM' and start_hour + (duration_hr % 12) >= 12:
        amount_of_days += 1

    # Flipping of am/pm
    am_pm_flip_amount = int((start_hour + duration_hr)/12) 

    if am_pm_flip_amount % 2 == 1: 
        am_pm = am_pm_flip[am_pm]
    else: am_pm

    return_time = final_time + ' ' + am_pm
    # Day Converter 
    if day:    
        day = day.lower()
        index = (int(Days_of_week[day]) + amount_of_days) % 7
        day = New_Day[str(index)]
        return_time += ',' + ' ' + day 

    # Returns the time, and date if excedes 
    if amount_of_days > 1:
        return return_time + " (" + str(amount_of_days) + ' ' + 'days later' ")"
    elif amount_of_days == 1:
        return return_time + ' ' + '(next day)'
    elif amount_of_days < 1:
        return return_time
    

    

print(add_time("8:16 PM", "466:02"))
