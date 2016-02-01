import math

data = [[200,15,34], [400,15,32], [600,15,30], [800,11.428,28], [1000,11.428,28]]


def convert_time(int):
    hours = math.floor(int)
    minutes = round((int-hours)*60,0)
    return(hours, minutes)

def handle_new_time(start_date, start_time, hours, minutes):
    """

    :param start_date: string 'MM/DD/YYYY'
    :param start_time: string 'HH:MM'
    :param hours: int
    :param minutes: int
    :return: (string new_date, string new_time)
    """
    #convert start data to usable formats
    start_time_conv = convert_time(int(start_time[0:2])+(int(start_time[3:5])/60))
    start_date_month = int(start_date[0:2])
    start_date_day = int(start_date[3:5])
    start_date_year = int(start_date[6:10])

    #preserve original conversion for testing
    temp_time = start_time_conv
    temp_day = start_date_day
    temp_month = start_date_month
    temp_year = start_date_year
    temp_hours = 0
    temp_minutes = 0

    #if start minutes +new minutes greater than 60 then add an hour
    if start_time_conv[1] + minutes >=60:
        temp_hours += 1
        temp_minutes = start_time_conv[1] + minutes-60
    else:
        temp_minutes += minutes

    #add hours to temp_time
    temp_hours += temp_time[0] + hours

    #if more than 24 hours in temp_time, adjust day
    while temp_hours>=24:
        temp_day +=1
        temp_hours -=24

    time_result = str(temp_hours) + ':' + str(temp_minutes)

    #adjust date
    if temp_day < 29 :
        date_result = str(temp_month) + "/" + str(temp_day) + "/" + str(temp_year)

        return(date_result,time_result)
    #check leap day/year
    elif temp_day == 29 & temp_month == 2 & temp_year%4!=0:
        temp_day = 1
        temp_month = 3
        date_result = str(temp_month) + "/" + str(temp_day) + "/" + str(temp_year)
        return(date_result,time_result)
    #check greater than 31
    elif temp_day >31 & (temp_month == 1 | temp_month == 3 | temp_month == 5 | temp_month == 7 | temp_month == 8 | temp_month == 10):
        temp_month += 1
        temp_day -= 31
        date_result = str(temp_month) + "/" + str(temp_day) + "/" + str(temp_year)
        return(date_result,time_result)
    #check if a new year
    elif temp_day >31 & temp_month == 12:
        temp_month = 1
        temp_day -= 31
        temp_year += 1
        date_result = str(temp_month) + "/" + str(temp_day) + "/" + str(temp_year)
        return(date_result,time_result)
    #check greater 30 and not greater than 31
    elif temp_day >30 & (temp_month == 4 | temp_month == 6 | temp_month == 9 | temp_month == 11):
        temp_month += 1
        temp_day -= 30
        date_result = str(temp_month) + "/" + str(temp_day) + "/" + str(temp_year)
        return(date_result,time_result)


def get_times(dist):
    count = 0
    open_time = 0
    close_time = 0
    while dist > 200:
        dist -= 200
        open_time += 200/data[count][2]
        close_time += 200/data[count][1]
        count += 1
    open_time += dist/data[count][2]
    close_time += dist/data[count][1]
    return(convert_time(open_time), convert_time(close_time))