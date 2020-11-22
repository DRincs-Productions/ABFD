# Tammy
image car tammy = "/car_travel/Tammy01.webp"
image car tammy 02 = "/car_travel/Tammy02.webp"
image mc bbf = "/car_travel/Tammy01-MC-BBF.webp"
image mc 02 get_out = "/car_travel/Tammy02-MC-get_out.webp"
image mc 02 talk_ahead = "/car_travel/Tammy02-MC-talk_ahead.webp"
image bg 02 house mc = "/car_travel/background02/house-MC.webp"
# Background
image bg animated residential:
    "/car_travel/background02/residential_area0.webp"
    pause 0.7
    "/car_travel/background02/residential_area1.webp"
    pause 0.7
    "/car_travel/background02/residential_area2.webp"
    pause 0.7
    "/car_travel/background02/residential_area3.webp"
    pause 0.7
    repeat

label travel_tammy_bbf:
    play ambience "audio/ambience-car_inside.ogg"
    show car tammy
    show mc bbf
    with dissolve
    return

label travel_tammy02:
    call clean_travel
    play ambience "audio/ambience-house_entrance.ogg"
    show car tammy 02
    show mc 02 talk_ahead
    with dissolve
    return

label clean_travel:
    stop ambience fadeout 1.0
    hide passenger_back
    hide passenger_ahead
    hide mc
    hide car
    return
