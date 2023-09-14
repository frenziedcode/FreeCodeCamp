def add_time(start, duration):

    amPM = ["AM", "PM"]
    hour = "12:00"
    minDuration = "00:00"


    print(hour + amPM[1], minDuration)

    time = start + duration


    return time

# Call Function
print(add_time("11:06 PM", "2:02"))