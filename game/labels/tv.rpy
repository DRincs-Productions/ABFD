image mc TV = "/family/TV/TV-mc.webp"
image emy tv = "/family/TV/TV-emy.webp"
image emy tv change = "/family/TV/TV-emy-change.webp"
image bg tv = "/family/TV/TV-back.webp"

image bg tv EMM0 final = Composite( (gui.width, gui.height),
    (0, 0), "/family/TV/EMM0final.webp",
    (0, 0), "/family/TV/EMM0final[mc_dress_home].webp")
image bg tv EMM01 A = Composite( (gui.width, gui.height),
    (0, 0), "/family/TV/EMM01A-MC-wach_tv.webp",
    (0, 0), "/family/TV/EMM01A-MC-wach_tv[mc_dress_home].webp")
image bg tv EMM01 B = Composite( (gui.width, gui.height),
    (0, 0), "/family/TV/EMM01B-MC-wach_tv.webp",
    (0, 0), "/family/TV/EMM01B-MC-wach_tv[mc_dress_home].webp")
image mia tv EMM01 B intro = "/family/TV/EMM01B-Mia-intro.webp"
image mia tv EMM01 B wach_tv = "/family/TV/EMM01B-Mia-wach_tv.webp"

image bg tv EMM01 change = "/family/TV/EMM01-change.webp"
image bg tv Emily01 = "/family/TV/Emily01.webp"

image tv deadpool = "/TV/DeadPool.webp"
image tv ciaodarwin = "/TV/CiaoDarwin.webp"
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

label News01:
    hide bg
    show tv News 01
    show bg tv
    show emy tv
    show mc TV
    mia "Look at [for_emyR.MClabel]! There's [nnc]. She was an old classmate of [for_emyR.MClabel]."
    emy "Yeah! By now, all you have to do to work in this macho TV is sleep with the right people.... That's why he had so much practice in high school in high school."
    mc "{i}Wow, I've never heard [emy] say that. They must have been enemies in high school."
    mia "Eh... [for_emyR.MClabel] I didn't understand. What did you practice with? Maybe I could do it too to become famous."
    emy "Haha... [mia]... you're still too young to understand these things. You don't need to be like her to become famous."
    nnc "Good evening, [city] viewers. We interrupted the normal live broadcast because to report a shooting in [city] north."
    nnc "The police have already intervened. Police suspect that the shooting that occurred is the clash between two gangs, but the reason is still unclear."
    nnc "Some sources say that these gangs are going to sell new drugs on the black market."
    mia "Oh no! [for_jnR.MClabel] is out there by himself...."
    emy "Yeah! I don't want anything to happen to him. But [for_emyR.NPClabel], don't worry. He's seen worse things than a little gunfight."
    nnc "We take advantage of this time to announce other news as well.... blah blah...."
    nnc "This extraordinary live broadcast is over, I leave you the vision of the weather."
    show tv Meteo01 1
    "Young girl" "Good morning ... Emm ... good evening television viewers."
    emy "And good night... TV has now reached the bottom."
    show tv Meteo01 2
    "Young girl" "Blah... blah... blah..."
    window hide
    pause
    show tv Meteo01 2B
    window hide
    pause
    show tv Meteo01 3
    "Young girl" "Opss shrug...my earring fell out. Where are you? Stupid thing..."
    window hide
    pause
    mc "{i}Wow I can't believe that just happened."
    window hide
    pause
    show emy tv change
    window hide
    pause
    show tv ciaodarwin
    mc "{i}NOOO!!! Where did you go nice ass...."
    hide tv
    hide mc
    hide emy
    show bg tv EMM01 change
    emy "This channel has really tired me out. There must at least be something decent around here."
    mc "{i}[emyR.NPClabel]?! Fuck [emyR.NPClabel]."
    show bg tv EMM0 final
    emy "Enough! I'm tired. I'm going to bed."
    mc "{i}Shit, she's so weird today."
    emy "[mia], it's late! go brush your teeth and let's go to bed. you're sleeping with me today, you'll keep me company."
    emy "[mc], don't be too late."
    mia "Uffa! Why can you stay and I can't?! I'm a big girl now."

    hide bg
    show tv deadpool
    show bg tv
    show mc TV
    window hide
    pause
    hide tv
    hide mc
    hide bg

    scene black
    show text _("{size=70}A few hours later.")
    window hide
    pause
    hide black

    $ del sp_routine["mia_change_clothes"]
    $ tm.new_hour(2)
    return
