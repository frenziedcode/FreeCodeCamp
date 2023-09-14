
HOURS_IN_ONE_DAY = 24
HOURS_IN_HALF_DAY = 12
WEEK_DAYS = {
    "monday",
    "tuesday",
    "Wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
}


def get_days(days):
    return ""



def add_time(start, duration, week = False):

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

    convMin_in_Hours = 0

    if ((hours > 12) and (hours < 24)):
        hours = hours + durationHour
        mins = mins + durationMin
        if (period == "PM"):
            period = "AM"
        elif (period == "AM"):
            period = "PM"

        hours = hours - 12
        if (mins > 60):
            plusHours = int(mins / 60)
            mins = mins - 60
            if( len(str(mins)) < 2):
                mins = '0' + str(mins)
            hours = hours + (plusHours * 1)

        return str(hours) + ':' + str(mins) + ' ' + period

    elif (hours + durationHour) > 24 :
        if (period == "PM"):
            period = 'AM'
            hours = hours + 12
            days_later_num = (hours + durationHour) / 24 
            days_later = f"({int(days_later_num)} days later)"
            tempHours = hours

            hours =  int(durationHour / 24)
            hours = durationHour - (hours * 24)
            mins = mins + durationMin
            hours = hours + tempHours - 24

            return str(hours) + ':' + str(mins) + ' ' + period + ' ' + days_later

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