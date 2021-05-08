image mc TV = "/family/TV/TV-mc.webp"
image emy tv = "/family/TV/TV-emy.webp"
image emy tv change = "/family/TV/TV-emy-change.webp"
image bg tv = "/family/TV/TV-back.webp"

image bg tv EMM0 final = Composite( (gui.width, gui.height),
    (0, 0), "/family/TV/EMM0final.webp",
    (0, 0), "/family/TV/EMM0final[mc_dress_normal].webp")
image bg tv EMM01 A = Composite( (gui.width, gui.height),
    (0, 0), "/family/TV/EMM01A-MC-wach_tv.webp",
    (0, 0), "/family/TV/EMM01A-MC-wach_tv[mc_dress_normal].webp")
image bg tv EMM01 B = Composite( (gui.width, gui.height),
    (0, 0), "/family/TV/EMM01B-MC-wach_tv.webp",
    (0, 0), "/family/TV/EMM01B-MC-wach_tv[mc_dress_normal].webp")
image mia tv EMM01 B intro = "/family/TV/EMM01B-Mia-intro.webp"
image mia tv EMM01 B wach_tv = "/family/TV/EMM01B-Mia-wach_tv.webp"

image bg tv EMM01 change = "/family/TV/EMM01-change.webp"
image bg tv Emily01 = "/family/TV/Emily01.webp"

image tv News 01 = Composite( (gui.width, gui.height),
    (0, 0), "/TV/News01.webp",
    (0, 0), "/TV/News-Icon.webp")
image tv Meteo01 1 = "/TV/Meteo01-1.webp"
image tv Meteo01 2 = "/TV/Meteo01-2.webp"
image tv Meteo01 2B = Composite( (gui.width, gui.height),
    (0, 0), "/TV/Meteo01-2.webp",
    (0, 0), "/TV/Meteo01-2B.webp")
image tv Meteo01 3 = "/TV/Meteo01-3.webp"

label intro_wach_tv:
    show bg tv Emily01
    mc "Has the movie started yet?"
    emy "No, there's still time"
    menu:
        "Have a seat":
            pass 
        "Back": 
            mc "I'll go brush my teeth first."
            emy "As you wish"
            $ cur_room = prev_room
            return 

    show bg tv EMM01 A
    "Advertisement" "Do you want to have a better life? Do you want to really enjoy life? Whether at the beach or in the mountains?"
    "Advertisement" "Now you can! With the new Audi, don't mind the price with Audi you can."
    "Advertisement" "(The classic movie introduction begins)"
    emy "[mia], hurry up! The movie is starting."
    mia "I'm coming!!!"
    show bg tv EMM01 B
    show mia tv EMM01 B intro
    mia "What kind of movie is it?"
    mc "I don't know, it looks good from the commercial."
    show mia tv EMM01 B wach_tv
    mia "Ok, I'll just stand here."
    emy "Why? We have such a big couch."
    mia "Because from here it looks huge it looks huge."
    "TV" "We break into the broadcast, to air an extraordinary live broadcast of the [city] news."
    mia "Phew, I wanted to see the movie."
    emy "Shh!"
    hide mia
    call News01
    return
