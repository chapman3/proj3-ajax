import brevet_calc
#used actual brevet calculator for correct examples
correct = [[0,(0,0),(1,0)],
           [100,(2,56),(6,40)],
           [200,(5,53),(13,20)],
           [300,(9,0),(20,0)],
           [350,(10,34),(23,20)],
           [450,(13,48),(6,0)],
           [550,(17,8),(12,40)],
           [700,(22,22),(0,45)],
           [900,(5,31),(18,15)],
           [1000,(9,5),(3,0)],
           ]

def test_calc(dist):
    print(str(brevet_calc.get_times(dist)))

def test_new_time(start_date, start_time, hours, minutes):
    print(str(brevet_calc.handle_new_time(start_date,start_time,hours,minutes)))


if __name__ == "__main__":
    #test dist calculations
    print("test 200km")
    test_calc(200)
    print("correct" + str(correct[2]))
    print("test 700km")
    test_calc(700)
    print("correct" + str(correct[7]))
    #test handle_new_date
    print("add 6:45 to 18:45 -> 1:30")
    test_new_time("01/01/2016","18:45",6,45)
    print("add 24:45 to 0:00 -> 0:45")
    test_new_time("01/01/2016","00:00",24,45)