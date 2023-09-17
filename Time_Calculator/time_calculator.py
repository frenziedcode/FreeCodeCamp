
def add_time(start, duration, week = ""):

    # start, duration == str
    days_later = 0
    hours, mins = start.split(":")
    mins, period = mins.split(" ")
    durationHour, durationMin = duration.split(":")

    # Conversão de str; para int;
    hours = int(hours)
    mins = int(mins)
    durationHour = int(durationHour)
    durationMin = int(durationMin)

    week_names = [
    "monday",
    "tueday",
    "Wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
    ]

    #convMin_in_Hours = 0
    weekDay = ""

    if ( (hours + durationHour) < 12):
        mins = mins + durationMin
        hours = hours + durationHour

        return str(hours) + ":" + str(mins) + " " +  period

    elif ( (hours + durationHour) > 12 ):
        mins = mins + durationMin
        tempMins = mins
        if (period == "PM"):
            period = "AM"
        elif (period == "AM"):
            period = "PM"

        if (mins > 60):
            plusHours = int(mins / 60)
            if (plusHours > 1):
                mins = mins - (plusHours + 60)
            else:
                mins = mins - 60

            if( len(str(mins) ) < 2):
                mins = '0' + str(mins)
            hours = hours + durationHour + plusHours
            hours = hours - 12
            
        if (hours + durationHour) > 24 :
                hours = hours + 12
                days_later_num = (hours + durationHour) / 24 
                days_later = f"({int(days_later_num)} days later)"
                tempHours = hours

                hours =  int(durationHour / 24)
                hours = durationHour - (hours * 24)
                hours = hours + tempHours - 24

                return str(hours) + ':' + str(mins) + ' ' + period + ' ' + str(days_later)


        if ( week != ""):
            if week.lower() in week_names:
                weekDay =  week_names[week_names.index(week.lower())].capitalize()
                return str(hours) + ":" + str(tempMins) + " " + period + " " +  weekDay
           
        else:
            return str(hours) + ":" + str(mins) + " " + period

    '''
    elif ( (hours < 12) and (hours + durationHour) > 12):
        if (period == "PM"):
            period = "AM"
        elif ( period == "AM"):
            period = "PM"

        mins = mins + durationMin

        if (mins > 60):
            convMin_in_Hours = int(mins / 60)
            mins = mins - 60
            if (len(str(mins)) < 2):
                mins = '0' + str(mins) 
            hours = (hours + durationHour) - 12

        hours = hours + convMin_in_Hours

    '''

    return 0;

# Call Function
print( add_time("8:16 PM", "466:02")  )