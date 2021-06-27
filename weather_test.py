from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


def tommorrow_weather1():
    owm = OWM("658a73671e103407771e2e4324a78edb")
    mgr = owm.weather_manager()

    three_h_forecaster = mgr.forecast_at_place('Athens,GR', '3h')
    tomorrow = timestamps.tomorrow()

    # ------------------------------------------------------------------------------------------------
    # THE WEATHER FORECAST FOR TOMMORROW
    print("-----------------WEATHER COND-----------------")
    print("The forecast for tommorrow is gonna be: ")
    tomorrow_at_eight = timestamps.tomorrow(8, 0)
    weather = three_h_forecaster.get_weather_at(tomorrow_at_eight)
    print('At 08:00 ' + weather.detailed_status)

    tomorrow_at_twelve = timestamps.tomorrow(12, 0)
    weather2 = three_h_forecaster.get_weather_at(tomorrow_at_twelve)
    print('At 12:00 ' + weather2.detailed_status)

    tomorrow_at_seventeen = timestamps.tomorrow(17, 0)
    weather3 = three_h_forecaster.get_weather_at(tomorrow_at_seventeen)
    print("At 17:00 " + weather3.detailed_status)

    tomorrow_at_twentytwo = timestamps.tomorrow(22, 0)
    weather4 = three_h_forecaster.get_weather_at(tomorrow_at_twentytwo)
    print('At 22:00 ' + weather4.detailed_status)

    one_call = mgr.one_call(lat=37.983810, lon=23.727539)
    avg = 0
    i = 3
    max_a = -999999
    min_a = 999999
    print('------------------ANALYTICS------------------- ')
    while i <= 24:
        a = one_call.forecast_hourly[i].temperature('celsius').get('temp')
        avg = avg + a
        if a > max_a:
            max_a = a
        if a < min_a:
            min_a = a
        i = i + 3
    avg = avg / 8
    print("The Max Temp is going to be " + str(max_a) + " \nThe Min temp " + str(min_a) + "\nThe Average temp will be " + str(int(avg)))
    print("-------------------PRO TIP-------------------- ")

    day_night_diff = max_a - min_a
    if avg > 32:
        print("Oh boy... your bold head is gonna boil like an egg better take a hat")
    elif avg > 25 and avg < 32:
        if day_night_diff > 7:
            print("The weather is going to be hot but high difference between day to night expected")
        else:
            print("The weather is going to be hot but with small changes in the weather")
    elif avg > 19 and avg < 25:
        if day_night_diff > 7:
            print("The weather is going to be good at some point but high difference between day to night expected")
        elif day_night_diff < 7:
            print("The weather seems good with small changes in the weather")
    elif avg < 19 and avg > 13:
        if day_night_diff > 7:
            print("Hmm... i see it's going to be a bit cold outside and i expect high difference between day to night so be cautius")
        elif day_night_diff < 7:
            print("Hmm... i see it's going to be a bit cold outside but dont expect high difference between day to night, be cautius")
    elif avg < 13 and avg > 6:
        if day_night_diff > 7:
            print("WARNING the weather is going to be really cold and watch out because high difference between day and night is expected")
        elif day_night_diff < 7:
            print("WARNING the weather is going to be really cold but it won't have high difference between day and night")
    elif avg < 6:
        print("WARNING the weather is going to be extremelly cold.... Is it so important afterall? Or are you visiting a mountain?")


    # -----------------------------------------------------------------------
    # WEATHER FORECAST ENDING


def tommorrow_weather2():
    owm = OWM("658a73671e103407771e2e4324a78edb")
    mgr = owm.weather_manager()

    three_h_forecaster = mgr.forecast_at_coords(lat=40.6403, lon=22.9439, interval="3h")
    tomorrow = timestamps.tomorrow()

    # ------------------------------------------------------------------------------------------------
    # THE WEATHER FORECAST FOR TOMMORROW
    print("-----------------WEATHER COND-----------------")
    print("The forecast for tommorrow is gonna be: ")
    tomorrow_at_eight = timestamps.tomorrow(8, 0)
    weather = three_h_forecaster.get_weather_at(tomorrow_at_eight)
    print('At 08:00 ' + weather.detailed_status)

    tomorrow_at_twelve = timestamps.tomorrow(12, 0)
    weather2 = three_h_forecaster.get_weather_at(tomorrow_at_twelve)
    print('At 12:00 ' + weather2.detailed_status)

    tomorrow_at_seventeen = timestamps.tomorrow(17, 0)
    weather3 = three_h_forecaster.get_weather_at(tomorrow_at_seventeen)
    print("At 17:00 " + weather3.detailed_status)

    tomorrow_at_twentytwo = timestamps.tomorrow(22, 0)
    weather4 = three_h_forecaster.get_weather_at(tomorrow_at_twentytwo)
    print('At 22:00 ' + weather4.detailed_status)

    one_call = mgr.one_call(lat=40.6403, lon=22.9439)
    avg = 0
    i = 3
    max_a = -999999
    min_a = 999999
    print('------------------ANALYTICS------------------- ')
    while i <= 24:
        a = one_call.forecast_hourly[i].temperature('celsius').get('temp')
        avg = avg + a
        if a > max_a:
            max_a = a
        if a < min_a:
            min_a = a
        i = i + 3
    avg = avg / 8
    print("The Max Temp is going to be " + str(max_a) + " \nThe Min temp " + str(min_a) + "\nThe Average temp will be " + str(int(avg)))
    print("-------------------PRO TIP-------------------- ")

    day_night_diff = max_a - min_a
    if avg > 32:
        print("Oh boy... your bold head is gonna boil like an egg better take a hat")
    elif avg > 25 and avg < 32:
        if day_night_diff > 7:
            print("The weather is going to be hot but high difference between day to night expected")
        else:
            print("The weather is going to be hot but with small changes in the weather")
    elif avg > 19 and avg < 25:
        if day_night_diff > 7:
            print("The weather is going to be good at some point but high difference between day to night expected")
        elif day_night_diff < 7:
            print("The weather seems good with small changes in the weather")
    elif avg < 19 and avg > 13:
        if day_night_diff > 7:
            print("Hmm... i see it's going to be a bit cold outside and i expect high difference between day to night so be cautius")
        elif day_night_diff < 7:
            print("Hmm... i see it's going to be a bit cold outside but dont expect high difference between day to night, be cautius")
    elif avg < 13 and avg > 6:
        if day_night_diff > 7:
            print("WARNING the weather is going to be really cold and watch out because high difference between day and night is expected")
        elif day_night_diff < 7:
            print("WARNING the weather is going to be really cold but it won't have high difference between day and night")
    elif avg < 6:
        print("WARNING the weather is going to be extremelly cold.... Is it so important afterall? Or are you visiting a mountain?")


    # -----------------------------------------------------------------------
    # WEATHER FORECAST ENDING


def tommorrow_weather3():
    owm = OWM("658a73671e103407771e2e4324a78edb")
    mgr = owm.weather_manager()

    three_h_forecaster = mgr.forecast_at_coords(lat=38.155811, lon=23.720341, interval='3h')
    tomorrow = timestamps.tomorrow()

    # ------------------------------------------------------------------------------------------------
    # THE WEATHER FORECAST FOR TOMMORROW
    print("-----------------WEATHER COND-----------------")
    print("The forecast for tommorrow is gonna be: ")
    tomorrow_at_eight = timestamps.tomorrow(8, 0)
    weather = three_h_forecaster.get_weather_at(tomorrow_at_eight)
    print('At 08:00 ' + weather.detailed_status)

    tomorrow_at_twelve = timestamps.tomorrow(12, 0)
    weather2 = three_h_forecaster.get_weather_at(tomorrow_at_twelve)
    print('At 12:00 ' + weather2.detailed_status)

    tomorrow_at_seventeen = timestamps.tomorrow(17, 0)
    weather3 = three_h_forecaster.get_weather_at(tomorrow_at_seventeen)
    print("At 17:00 " + weather3.detailed_status)

    tomorrow_at_twentytwo = timestamps.tomorrow(22, 0)
    weather4 = three_h_forecaster.get_weather_at(tomorrow_at_twentytwo)
    print('At 22:00 ' + weather4.detailed_status)

    one_call = mgr.one_call(lat= 38.155811, lon=23.720341)
    avg = 0
    i = 3
    max_a = -999999
    min_a = 999999
    print('------------------ANALYTICS------------------- ')
    while i <= 24:
        a = one_call.forecast_hourly[i].temperature('celsius').get('temp')
        avg = avg + a
        if a > max_a:
            max_a = a
        if a < min_a:
            min_a = a
        i = i + 3
    avg = avg / 8
    print("The Max Temp is going to be " + str(max_a) + " \nThe Min temp " + str(min_a) + "\nThe Average temp will be " + str(int(avg)))
    print("-------------------PRO TIP-------------------- ")

    day_night_diff = max_a - min_a
    if avg > 32:
        print("Oh boy... your bold head is gonna boil like an egg better take a hat")
    elif avg > 25 and avg < 32:
        if day_night_diff > 7:
            print("The weather is going to be hot but high difference between day to night expected")
        else:
            print("The weather is going to be hot but with small changes in the weather")
    elif avg > 19 and avg < 25:
        if day_night_diff > 7:
            print("The weather is going to be good at some point but high difference between day to night expected")
        elif day_night_diff < 7:
            print("The weather seems good with small changes in the weather")
    elif avg < 19 and avg > 13:
        if day_night_diff > 7:
            print("Hmm... i see it's going to be a bit cold outside and i expect high difference between day to night so be cautius")
        elif day_night_diff < 7:
            print("Hmm... i see it's going to be a bit cold outside but dont expect high difference between day to night, be cautius")
    elif avg < 13 and avg > 6:
        if day_night_diff > 7:
            print("WARNING the weather is going to be really cold and watch out because high difference between day and night is expected")
        elif day_night_diff < 7:
            print("WARNING the weather is going to be really cold but it won't have high difference between day and night")
    elif avg < 6:
        print("WARNING the weather is going to be extremelly cold.... Is it so important afterall? Or are you visiting a mountain?")


    # -----------------------------------------------------------------------
    # WEATHER FORECAST ENDING

def tommorrow_weather4():
    owm = OWM("658a73671e103407771e2e4324a78edb")
    mgr = owm.weather_manager()

    three_h_forecaster = mgr.forecast_at_coords(lat=37.942986, lon=23.646982, interval="3h")
    tomorrow = timestamps.tomorrow()

    # ------------------------------------------------------------------------------------------------
    # THE WEATHER FORECAST FOR TOMMORROW
    print("-----------------WEATHER COND-----------------")
    print("The forecast for tommorrow is gonna be: ")
    tomorrow_at_eight = timestamps.tomorrow(8, 0)
    weather = three_h_forecaster.get_weather_at(tomorrow_at_eight)
    print('At 08:00 ' + weather.detailed_status)

    tomorrow_at_twelve = timestamps.tomorrow(12, 0)
    weather2 = three_h_forecaster.get_weather_at(tomorrow_at_twelve)
    print('At 12:00 ' + weather2.detailed_status)

    tomorrow_at_seventeen = timestamps.tomorrow(17, 0)
    weather3 = three_h_forecaster.get_weather_at(tomorrow_at_seventeen)
    print("At 17:00 " + weather3.detailed_status)

    tomorrow_at_twentytwo = timestamps.tomorrow(22, 0)
    weather4 = three_h_forecaster.get_weather_at(tomorrow_at_twentytwo)
    print('At 22:00 ' + weather4.detailed_status)

    one_call = mgr.one_call(lat=37.942986, lon=23.646982)
    avg = 0
    i = 3
    max_a = -999999
    min_a = 999999
    print('------------------ANALYTICS------------------- ')
    while i <= 24:
        a = one_call.forecast_hourly[i].temperature('celsius').get('temp')
        avg = avg + a
        if a > max_a:
            max_a = a
        if a < min_a:
            min_a = a
        i = i + 3
    avg = avg / 8
    print("The Max Temp is going to be " + str(max_a) + " \nThe Min temp " + str(min_a) + "\nThe Average temp will be " + str(int(avg)))
    print("-------------------PRO TIP-------------------- ")

    day_night_diff = max_a - min_a
    if avg > 32:
        print("Oh boy... your bold head is gonna boil like an egg better take a hat")
    elif avg > 25 and avg < 32:
        if day_night_diff > 7:
            print("The weather is going to be hot but high difference between day to night expected")
        else:
            print("The weather is going to be hot but with small changes in the weather")
    elif avg > 19 and avg < 25:
        if day_night_diff > 7:
            print("The weather is going to be good at some point but high difference between day to night expected")
        elif day_night_diff < 7:
            print("The weather seems good with small changes in the weather")
    elif avg < 19 and avg > 13:
        if day_night_diff > 7:
            print("Hmm... i see it's going to be a bit cold outside and i expect high difference between day to night so be cautius")
        elif day_night_diff < 7:
            print("Hmm... i see it's going to be a bit cold outside but dont expect high difference between day to night, be cautius")
    elif avg < 13 and avg > 6:
        if day_night_diff > 7:
            print("WARNING the weather is going to be really cold and watch out because high difference between day and night is expected")
        elif day_night_diff < 7:
            print("WARNING the weather is going to be really cold but it won't have high difference between day and night")
    elif avg < 6:
        print("WARNING the weather is going to be extremelly cold.... Is it so important afterall? Or are you visiting a mountain?")


    # -----------------------------------------------------------------------
    # WEATHER FORECAST ENDING


def tommorrow_weather5():
    owm = OWM("658a73671e103407771e2e4324a78edb")
    mgr = owm.weather_manager()

    three_h_forecaster = mgr.forecast_at_coords(lat=37.456520, lon=23.490641, interval='3h')
    tomorrow = timestamps.tomorrow()

    # ------------------------------------------------------------------------------------------------
    # THE WEATHER FORECAST FOR TOMMORROW
    print("-----------------WEATHER COND-----------------")
    print("The forecast for tommorrow is gonna be: ")
    tomorrow_at_eight = timestamps.tomorrow(8, 0)
    weather = three_h_forecaster.get_weather_at(tomorrow_at_eight)
    print('At 08:00 ' + weather.detailed_status)

    tomorrow_at_twelve = timestamps.tomorrow(12, 0)
    weather2 = three_h_forecaster.get_weather_at(tomorrow_at_twelve)
    print('At 12:00 ' + weather2.detailed_status)

    tomorrow_at_seventeen = timestamps.tomorrow(17, 0)
    weather3 = three_h_forecaster.get_weather_at(tomorrow_at_seventeen)
    print("At 17:00 " + weather3.detailed_status)

    tomorrow_at_twentytwo = timestamps.tomorrow(22, 0)
    weather4 = three_h_forecaster.get_weather_at(tomorrow_at_twentytwo)
    print('At 22:00 ' + weather4.detailed_status)

    one_call = mgr.one_call(lat=37.456520, lon=23.490641)
    avg = 0
    i = 3
    max_a = -999999
    min_a = 999999
    print('------------------ANALYTICS------------------- ')
    while i <= 24:
        a = one_call.forecast_hourly[i].temperature('celsius').get('temp')
        avg = avg + a
        if a > max_a:
            max_a = a
        if a < min_a:
            min_a = a
        i = i + 3
    avg = avg / 8
    print("The Max Temp is going to be " + str(max_a) + " \nThe Min temp " + str(min_a) + "\nThe Average temp will be " + str(int(avg)))
    print("-------------------PRO TIP-------------------- ")

    day_night_diff = max_a - min_a
    if avg > 32:
        print("Oh boy... your bold head is gonna boil like an egg better take a hat")
    elif avg > 25 and avg < 32:
        if day_night_diff > 7:
            print("The weather is going to be hot but high difference between day to night expected")
        else:
            print("The weather is going to be hot but with small changes in the weather")
    elif avg > 19 and avg < 25:
        if day_night_diff > 7:
            print("The weather is going to be good at some point but high difference between day to night expected")
        elif day_night_diff < 7:
            print("The weather seems good with small changes in the weather")
    elif avg < 19 and avg > 13:
        if day_night_diff > 7:
            print("Hmm... i see it's going to be a bit cold outside and i expect high difference between day to night so be cautius")
        elif day_night_diff < 7:
            print("Hmm... i see it's going to be a bit cold outside but dont expect high difference between day to night, be cautius")
    elif avg < 13 and avg > 6:
        if day_night_diff > 7:
            print("WARNING the weather is going to be really cold and watch out because high difference between day and night is expected")
        elif day_night_diff < 7:
            print("WARNING the weather is going to be really cold but it won't have high difference between day and night")
    elif avg < 6:
        print("WARNING the weather is going to be extremelly cold.... Is it so important afterall? Or are you visiting a mountain?")

    # -----------------------------------------------------------------------
    # WEATHER FORECAST ENDING


def tommorrow_weather6():
    owm = OWM("658a73671e103407771e2e4324a78edb")
    mgr = owm.weather_manager()

    three_h_forecaster = mgr.forecast_at_coords(lat=37.825279, lon=15.266790, interval="3h")
    tomorrow = timestamps.tomorrow()

    # ------------------------------------------------------------------------------------------------
    # THE WEATHER FORECAST FOR TOMMORROW
    print("-----------------WEATHER COND-----------------")
    print("The forecast for tommorrow is gonna be: ")
    tomorrow_at_eight = timestamps.tomorrow(8, 0)
    weather = three_h_forecaster.get_weather_at(tomorrow_at_eight)
    print('At 08:00 ' + weather.detailed_status)

    tomorrow_at_twelve = timestamps.tomorrow(12, 0)
    weather2 = three_h_forecaster.get_weather_at(tomorrow_at_twelve)
    print('At 12:00 ' + weather2.detailed_status)

    tomorrow_at_seventeen = timestamps.tomorrow(17, 0)
    weather3 = three_h_forecaster.get_weather_at(tomorrow_at_seventeen)
    print("At 17:00 " + weather3.detailed_status)

    tomorrow_at_twentytwo = timestamps.tomorrow(22, 0)
    weather4 = three_h_forecaster.get_weather_at(tomorrow_at_twentytwo)
    print('At 22:00 ' + weather4.detailed_status)

    one_call = mgr.one_call(lat=37.825279, lon=15.266790,)
    avg = 0
    i = 3
    max_a = -999999
    min_a = 999999
    print('------------------ANALYTICS------------------- ')
    while i <= 24:
        a = one_call.forecast_hourly[i].temperature('celsius').get('temp')
        avg = avg + a
        if a > max_a:
            max_a = a
        if a < min_a:
            min_a = a
        i = i + 3
    avg = avg / 8
    print("The Max Temp is going to be " + str(max_a) + " \nThe Min temp " + str(min_a) + "\nThe Average temp will be " + str(int(avg)))
    print("-------------------PRO TIP-------------------- ")

    day_night_diff = max_a - min_a
    if avg > 32:
        print("Oh boy... your bold head is gonna boil like an egg better take a hat")
    elif avg > 25 and avg < 32:
        if day_night_diff > 7:
            print("The weather is going to be hot but high difference between day to night expected")
        else:
            print("The weather is going to be hot but with small changes in the weather")
    elif avg > 19 and avg < 25:
        if day_night_diff > 7:
            print("The weather is going to be good at some point but high difference between day to night expected")
        elif day_night_diff < 7:
            print("The weather seems good with small changes in the weather")
    elif avg < 19 and avg > 13:
        if day_night_diff > 7:
            print("Hmm... i see it's going to be a bit cold outside and i expect high difference between day to night so be cautius")
        elif day_night_diff < 7:
            print("Hmm... i see it's going to be a bit cold outside but dont expect high difference between day to night, be cautius")
    elif avg < 13 and avg > 6:
        if day_night_diff > 7:
            print("WARNING the weather is going to be really cold and watch out because high difference between day and night is expected")
        elif day_night_diff < 7:
            print("WARNING the weather is going to be really cold but it won't have high difference between day and night")
    elif avg < 6:
        print("WARNING the weather is going to be extremelly cold.... Is it so important afterall? Or are you visiting a mountain?")
    # -----------------------------------------------------------------------
    # WEATHER FORECAST ENDING



###WEATHER CALCULATIONS AND SETUP----------------------------
print("             ---WEATHER CALCULATOR---")
locations = ["1  Athens, GR",
             "2  Thessaloniki, GR",
             "3  Parnitha, GR",
             "4  Piraeus, GR",
             "5  Saronida, GR",
             "6  Naxos, GR"
             ]
#-------------------------------------------------------------
i = 0
#ASK THE USER WHAT EXACTLY HE NEEDS
print("-------For which of the following places?-------")
while i <= 5:
    print(locations[i])
    i = i + 1
locselect = input("Select number ")
if locselect == "1":
    tommorrow_weather1()
if locselect == "2":
    tommorrow_weather2()
if locselect == "3":
    tommorrow_weather3()
if locselect == "4":
    tommorrow_weather4()
if locselect == "5":
    tommorrow_weather5()
if locselect == "6":
    tommorrow_weather6()
