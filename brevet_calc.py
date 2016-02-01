import math

data = [[200,15,34], [400,15,32], [600,15,30], [800,11.428,28], [1000,11.428,28]]


def convert_time(int):
    hours = math.floor(int)
    minutes = round((int-hours)*60,0)
    return(hours, minutes)



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