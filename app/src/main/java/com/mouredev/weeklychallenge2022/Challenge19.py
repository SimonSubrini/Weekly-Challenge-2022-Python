def time(days,hours,minutes,seconds):
    miliDays=days*24*60*60*1000
    miliHours=hours*60*60*1000
    miliMinutes=minutes*60*1000
    miliSeconds=seconds*1000
    return miliDays+miliHours+miliMinutes+miliSeconds
print(time(1,1,1,1))
