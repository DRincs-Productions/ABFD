# Tammy
image car tammy = "/car_travel/Tammy01.webp"
image car tammy 02 = "/car_travel/Tammy02.webp"
image mc bbf = "/car_travel/Tammy01-MC-BBF.webp"
image mc 02 get_out = "/car_travel/Tammy02-MC-get_out.webp"
image mc 02 talk_ahead = "/car_travel/Tammy02-MC-talk_ahead.webp"
image background 02 house mc = "/car_travel/background02/house-MC.webp"
# Background
image background animated car residential day:
    Composite( (gui.width, gui.height),
        (0, 0), im.Blur("/car_travel/residential_area.webp", 4),
        (0, 150), im.Blur("/car_travel/car.webp", 3)) with Dissolve(1, alpha = True)
    pause 3.0
    Composite( (gui.width, gui.height),
        (0, 0), im.Blur(im.Flip("/car_travel/background02/background02.webp", horizontal=True), 4),
        (0, 150), im.Blur("/car_travel/car.webp", 3)) with Dissolve(1, alpha = True)
    pause 3.0
    repeat

label travel_tammy_bbf:
    # play ambience "audio/ambience-car_inside.ogg"
    show car tammy
    show mc bbf
    with dissolve
    return

label travel_tammy02:
    call clean_travel
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

# animation
label play_animation_residential:
    show background animated car residential
    return

label stop_animation_residential:
    show background car residential
    return
