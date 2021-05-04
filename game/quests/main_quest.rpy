image quest main = "/intro/C01.webp"

label main_startstage:
    $ updateQuestsLevels()
    if (quests_levels["main"] == 0):
        $ quests_descriptions["main"] = _("[jn] walked away leaving us alone. In the postit that he left there was written that he has to solve some problems, but which ones? Apart from that I don't know much else, [emy] on the other hand seems to know what he was talking about or rather she doesn't ask too many questions as if she already has an idea about the answers. \nI just hope that the problems will not come looking for us.")
        $ sp_routine["introD"] = Commitment(chs={"mia" : TalkObject()}, tm_start=17, tm_stop=19, id_location="house", id_room="mia_room", label_event="introD")
    return

label introD:
    show bg door open
    menu:
        "The door is closed:"
        "Knock":
            "knock-knock"
            pass
        "Back":
            $ cur_room = prev_room
            return

    image bg prologue D01A = "/intro/D01A.webp"
    image bg prologue D01B = "/intro/D01B.webp"
    image bg prologue D02 = "/intro/D02.webp"
    image bg prologue D03A = "/intro/D03A.webp"
    image bg prologue D03B = "/intro/D03B.webp"
    image bg prologue D04 = "/combact/Final/Mia01.webp"

    show bg prologue D01A
    show screen countdown(timer_range=5, timer_call='menu_slow')

label introD_part2:
    menu:
        "Ehilà [mia]:"
        "How is the study going?":
            hide screen countdown
            show bg prologue D01B
            mc "How is the study going?"
            mia "Ehilà, Yes...I was reviewing tomorrow I have a math test."
            mc "Are you ready?"
            mia "I mean, math is not my strong suit."
            mc "Ah, I hear you."
            jump introD_part2
        "Do you have a minute?":
            hide screen countdown
            show bg prologue D01B
            mc "Do you have a minute? I wanted to talk a little bit about [emyR.NPClabel]."
            mia "Yeah, you know about last night? About what... happened."
            mc "Eh  I already know, unfortunately."
        "How are you?":
            hide screen countdown
            show bg prologue D01B
            mc "How are you? I know what happened yesterday."
            mia "I'm fine, but..."
        "Be quiet":
            hide screen countdown
            show bg prologue D01B
            mia "[mc]?! You wanted to talk to me?"
            mc "Yes, yes, sorry. I was just thinking for a second..."
            mc "I wanted to ask you what happened last night."
            pass
    show bg prologue D02
    mia "Last night I overheard [emy] and [jn] discussing their relationship... their problems..."
    mc "Same as other days, nothing new."
    return
