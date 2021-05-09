label intro:
    # Presentation of Liam
    play ambience "audio/ambience-train.ogg"
    show profile mc 01
    with dissolve
    call renaming_mc
    $ renpy.music.set_pause(False, channel='music')
    $ renpy.music.set_pause(False, channel='ambience')
    show profile mc 01
    with dissolve
    $ school_grades_mc.update_average()
    mc "Hi, I'm a normal [mcI.age] year old boy with classic problems and no desire to commit, but just to have fun. I don't have a {b}girlfriend{/b}, a {b}job{/b} or concrete plans for the future and my school situation is gross. In the {b}school report of the first quarter{/b} I have all [school_grades_mc.average]."
    mc "My family is worried about my poor results and some of my behaviors, which is why they are deciding whether to keep me at home or have me transferred to a hateful [catholic_institute]. I have to make sure that this will never happen."
    mc "To be honest, my real family died in a plane crash. After their death I moved from [old_city] to [city] where I started a new life."
    call live_with

label presentations:
    show profile mc 01
    "{color=#ec5c09}Patreon" "Some characters are still in development. I will use {b}public votes{/b} to decide their appearance. Check my {b}{a=https://www.patreon.com/posts/revisiting-of-37922891}Post{/b}."
    menu:
        "Rename the characters":
            call renaming_mc_family
            jump presentations
        "More about my family":
            hide profile
            pass
        "Continue with the intro":
            hide profile
            stop ambience fadeout 1.0
            stop music fadeout 1.0
            jump presentations_montell
            pass
        "Skip":
            call renaming_friend
            hide profile
            stop ambience fadeout 1.0
            stop music fadeout 1.0
            jump prologue
        mc "For me they are a second family."

    show profile jn 01
    mc "[jn] is married to [emy], for me he is like a second father. He is a former Navy Seals, with the last mission in [jnMission] he was awarded the pension. [jnMission] has changed him, he started drinking, he is never at home and when he is there he speaks very little. [emy] tried to help him, but she got only quarrels and insults."

    show profile emy 01
    mc "[emy] is the classic housewife, cooks, washes and takes care of the family. When she was young she was a {b}model{/b}, but she is very reserved about her past. Sometimes when I come home I see her flipping through old magazines. She leaves home very little, [jn] never takes her anywhere."

    show profile arn 01
    mc "[arn] is the same age as me, we attend the same {b}school{/b} and are in the same year, but in different classes. Her class is the best in the history of our school, while mine is probably the worst. That's why, 2 days ago, they left on a school trip while we didn't."

    show profile vct 01
    mc "[vct] is a {b}college freshman{/b}, she likes to go out in the evening and have fun with her friends. The last few days have been difficult for her too, she often comes back completely {b}drunk{/b} in the evening. Our relationship is mostly love and hate."

    show profile mia 01
    mc "[mia] is the youngest in the house and she is [for_emyR.MClabel]'s darling. Since she changed schools she has various difficulties and often asks me to {b}help her with her homework{/b}. Her big dream is to become an [influencer], but her [for_emyR.MClabel] forbids her to post pictures."
    hide profile
    jump presentations

label presentations_montell:
    show bg animated residential
    call travel_tammy_bff
    mc "{i}Now I'm on my way home, after spending the night at the {b}[tamI.sname]'s house{/b}. They are the only people from my old life that I still hang out with. Next to me there is:"
    call renaming_friend
    mc "{i}And this is his mother, [tam]. They too lost someone in the plane crash, her father and her husband {b}Mr. [mrJohnson] Johnson{/b}. He and my father were colleagues and that is why I have known them since childhood."
    mc "{i}And so, a few weeks after I left my old city, they preferred to create a new life by moving here to my own neighborhood, except his brother who preferred to stay."
    mc "{i}This neighborhood is a nice place to live, it is a quiet area, not far away there is the sea, some clubs and there are beautiful girls."
    tam "What's wrong with you guys!? You are so quiet."
    bff "All is well. It's just that yesterday we played at the [console] until late at night."
    tam "Who won in the end?"
    bff "I won, I literally shredded it. He is too scarce."
    mc "It's just luck."
    bff "Modestly this is talent, you have to train to reach my level."
    tam "Yeah! [bff] spends hours in front of a stupid screen after school."
    mc "Don't worry, [tam]. I convince him to go out. We also joined the school's [mcSport] team."
    bff "I don't know if that was a good idea and then mom, you know I don't go out much because I don't have many friends here."
    tam "Don't worry, honey. I'm sure when you start [mcSport] you'll make a few friends."
    tam "By the way [mc], did you give your to [emyR.NPClabel] your school report card?"
    mc "Not yet, I'm going to talk to her tonight."
    tam "Well, you have arrived."
    show bg 02 house mc
    call travel_tammy02
    tam "Wait [mc]. Remember that if you don't tell her, I will tell [emy] when I see her."
    mc "All right, [tam]. I will."
    tam "Well, you can go."
    show mc 02 get_out
    bff "Bye, [mc]. See you."
    mc "Bye"
    call clean_travel

label prologue:
    image bg prologue A01:
        "/intro/A01.webp" with dissolve
        pause 1.6
        "/intro/A02.webp"
        pause 0.8
        "/intro/A03.webp" with dissolve
    image mc prologue A01:
        pause 1.6
        pause 0.9
        "/intro/A03-MC.webp" with dissolve
        pause 2.0
        "/intro/c.webp" with dissolve
    image text animated title:
        pause 1.6
        pause 0.9
        "/intro/B01.webp"
        pause 0.5
        "/intro/B02.webp"
        pause 0.5
        "/intro/B03.webp"
        pause 0.5
        "/intro/c.webp"
        pause 0.5
        "/intro/B04.webp" with dissolve
        pause 5.0
        repeat
    image car prologue = "/intro/A01-car.webp"

    play ambience "audio/ambience-suburb.ogg"
    if renpy.variant("pc"):
        play sound "audio/sfx-engine_ignition.ogg"
    show bg prologue A01
    show text animated title
    if renpy.variant("pc"):
        show car prologue:
            pause 0.3
            xpos 0
            ypos 0
            linear 2.0 xpos -5000
    show mc prologue A01
    window hide
    pause
    hide car
    hide mc
    hide text

    image bg prologue C00 = "/intro/C00.webp"
    image mc prologue C00 = "/intro/C00-MC.webp"
    image bg prologue C01 = "/intro/C01.webp"
    image bg prologue C02 = "/intro/C02.webp"
    image bg prologue C02 blur = im.Blur("/intro/C02.webp", 7)
    image bg prologue C03 = "/intro/C03.webp"
    image bg prologue C04 = "/intro/C04.webp"
    image bg prologue C05 = "/intro/C05.webp"
    image note prologue = "/tools/note.webp"
    stop ambience fadeout 1.0
    play sound "audio/sfx-door1.ogg"
    $ x = 0
    show bg prologue C00
    mc "I am home!"
    show mc prologue C00
    with dissolve
    play music "audio/music-somber.ogg"
    mc "{i}What!? What is happening?"
    mc "{i}My [emyR.NPClabel] is crying!?"
    hide mc
    hide emy
    show bg prologue C01
    emy "Hey, honey."
    mc "Hi [emyR.NPClabel]. What happened?"
    emy "He is gone... [jn] is gone. This morning I woke up and he was gone. He left without even telling me anything."
    menu:
        "Where did he go?":
            $ x -= 1
            mc "He is gone!? Where?"
            emy "Eh, what do I know. He left home."
        "Why?":
            mc "What happened?"
        "Well":
            $ x -= 5
            mc "Oh finally! I couldn't take it anymore."
            emy "Hey! You can't talk about your [jnR.NPClabel] like that."
        "{i}I knew it...":
            mc "{i}I knew this would happen sooner or later."
    emy "Come on, sit down."
    show bg prologue C02
    with dissolve
    emy "When I woke up I found this in the kitchen. Do you realize... [mia] could have found it."
    show note prologue at center_delay(0.1)
    show text _("{color=#000}{size=120}{font=fonts/handwriting_alphabetizedcassettetapes-classic.ttf}My presence \n only causes problem. \n I will fix our problem, \n but then I will not come back \n\n    [jn]{/color}") at center_delay(0.1)
    if renpy.variant("pc"):
        show bg prologue C02 blur with dissolve
    window hide
    pause
    hide note
    hide text
    show bg prologue C02
    emy "Now how are we going to do without him!?"
    menu:
        "His loss":
            $ x += 5
            show bg prologue C03
            mc "[emyR.NPClabel] if anyone has lost, it's him. I could never leave a woman like you."
            emy "Honey, I'm lucky to have you who know how to cheer me up."
        "What happened? {color=#f00}(Probability 10\%)":
            $ val = False
            if (val):
                $ x += 1
                show bg prologue C03
                mc "What happened? Did he put his hands on you?"
                emy "No No, honey we just had a fight as usual. You know that since he came back from [jnMission] he has become a different person."
                mc "Yesterday I tried to hide the [jnAlcol], but it was useless. He found it and got drunk even more than usual."
                emy "Honey, you know, I tried to help him, but yesterday I couldn't take it anymore. I told him he could do what he wanted, but this is not a home for junkies or alcoholics. And if he wanted to continue, he could leave."
            else:
                $ x -= 1
                show bg prologue C04
                mc "Okay, but I wanted to understand what happened yesterday. If he left for some reason or something you told him."
                emy "So in your opinion it may be my fault that he left!?"
                mc "No! I didn't mean that. It's just that..."
                emy "Now I want to be alone for a while, go ahead."
                jump prologue_end
        "Go away":
            $ x -= 5
            show bg prologue C04
            mc "OK, [emyR.NPClabel]. Now I'm a little tired, I'm going to my room."
            jump prologue_end
    emy "I've kept you long enough, go ahead."

label prologue_end:
    show bg prologue C05 with dissolve
    $ stats['emy'].change('favour', x)
    mc "{i}Shit! I have enough problems on my own, that's all we needed."
    mc "{i}Who knows how is [mia]?! Maybe I should talk to her, she will probably tell me something more."
    stop music fadeout 1.0

    menu:
        mc "But first:"
        "Tutorial":
            call navigation_tuturial
        "Skip":
            pass
    # Start Main quest
    $ quests["main"].start()
    return
label introD_emy:
    $ cur_room = prev_room
    "For now it's better to dry her off. I could talk to [mia]..."
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

    show bg prologue D01A
    mc "Ehilà [mia]:"
    show screen countdown(timer_range=5, timer_call='menu_slow')

label introD_part2:
    menu:
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
    mia "However, this time [for_emyR.MClabel] started screaming and then went to bed. While [jn] stayed in the jump. Then around 3 o'clock I heard some unusual noises, then slamming the door of the house."
    mia "I thought it was a burglar or someone with bad intentions, but it was [jn]'s voice. I ran into the living room, but by then there was no one there. Except for a postit on the refrigerator... there was... there was writing on it."
    mc "Unfortunately, I already know what it said. [emy] made me read it."

    label introD_part3:
    image bg prologue D03A = "/intro/D03A.webp"
    image bg prologue D03B = "/intro/D03B.webp"
    menu:
        "What about [vct]?":
            mc "What about [vct]? I haven't seen her since yesterday."
            mia "She already knows everything, I wrote her what happened. Yesterday she stayed over at the college. Her friend's roommate was at her parents', so she had an extra bed."
            jump introD_part3
        "And then?":
            mc "And then what happened? Did you talk to [emy]?"
            mia "What could I do, I put the note back where it was and then played it cool. This night I hardly got a wink of sleep."
            mia "The next day you could tell [emy] had been crying a lot, but I didn't know what to do. She tried to play it cool."
            mia "I had breakfast and then stayed in my room. By lunch she had recovered a little. All she told me was that [jn] will be gone for a while. You know he doesn't talk to me about these things."
        "OK, that's enough.":
            mc "OK, OK, that's enough. "
    mc "I don't want to see you so sad. I know a remedy to cheer up that sad little face."
    mia "What's that? What is it?"
    show bg prologue D03A
    mia "Ha, haha... Stop it."
    mc "What did you say? I don't have to stop?! Ok..."
    mia "Ha, haha... Stop it."
    show bg prologue D03B
    "([mia] picks up the pillow and starts the fight.)"

    label introD_fight:

        "{color=#ec5c09}Patreon" "In development"

        image bg prologue D04 = "/combact/Final/Mia01.webp"
        show bg prologue D04
        menu:
            "Want to skip the \"dream\"?"
            "Continue":
                call after_deathA
            "Skip":
                pass

label introF:
    image bg prologue F01 = "/intro/F01.webp"
    image bg prologue F02A = "/intro/F02A.webp"
    image bg prologue F02B = "/intro/F02B.webp"
    image bg prologue F02C = "/intro/F02C.webp"

    show bg prologue F01
    pause
    show black with blink_transition
    pause 0.01
    hide black with blink_reverse
    mia "Hey, [for_emyR.MClabel]. He's opening his eyes."
    show black with blink_transition
    pause 0.01
    hide black with blink_reverse
    mc "{i}It was all a dream! Good thing."
    mia "[mc]. Sorry, I didn't do it on purpose."
    show black with blink_transition
    pause 0.01
    hide black with blink_reverse
    mc "{i}Huh? What?"
    emy "I told you with a little time and a little vinegar, you'll wake even a corpse."
    show black with blink_transition
    pause 0.01
    hide black with blink_reverse
    mc "Arg! What's that smell?!"
    emy "Honey, be quiet."
    show bg prologue F02A
    mc "Arg! What a headache. What happened?"
    mia "Don't you remember? We were playing and you tripped."
    show bg prologue F02B
    emy "Wow, that must have been a pretty bad beat. How are you feeling?"
    mc "{i}Wow, she got so worried about me. She didn't even notice that her big boobs were right in front of me."
    show screen countdown(timer_range=3, timer_call='menu_slow')
    menu:
        "Much better":
            hide screen countdown
            mc "Much better now."
        "Start to recover":
            hide screen countdown
            mc "I'm starting to get better."
        "Milk":
            hide screen countdown
            mc "Mhmm... I feel like milk."
        "Remain silent":
            hide screen countdown
            mc "Mhmm..."
    show bg prologue F02C
    with hpunch
    emy "Damn! It's so late! I'm going to...make something...in the kitchen. I have something in the oven..."
    emy "[mia], come down and come help me."
    mia "Ok, [for_emyR.MClabel]."
    mc "{i}Fuck what has gotten into me! Who knows what [emy] must have thought."
    emy "{i}Oh my god, [emy] why didn't you put your bra on. If you would have done that I wouldn't ... have seen ... that bulge in her pants. I just don't want to think about it anymore."
    emy "{i}I didn't think he was that gifted though."
    mia "{i}..."

    # $ sp_routine.pop("introD")
    $ sp_routine["at_table preparation"] = Commitment(chs={"mia" : TalkObject(bg_before_after="bg at_table preparation", label_talk="first_at_table_preparation")}, tm_start=19, tm_stop=21, id_location="house", id_room="livingroom")
    $ quests["main"].next_stage()

    $ del sp_routine["introD"]
    $ tm.new_hour(2)
    jump after_wait
    return

label intro_sleep:
    show bg mc sleep sl01A
    mc "{i}What a strange day today has been. With everything that's happened to me I keep thinking about what that old man said. There's only one life, I mustn't waste it."
    menu:
        mc "{i}Mhmm... I have too many thoughts in my head..."
        "Jerk off":
            mc "{i}A hand job might help."
            scene black
            mc "{i}It would be better, take a tissue."
            hide black
            call sleep_fap01
            scene black
            window hide
            pause
        "Try to sleep":
            pass
    # TODO: GTA5 sound when changing characters
    show bg mc sleep sl01A
    window hide
    pause
    show bg mc sleep sl01B
    window hide
    pause
    mc "zZz zZz ..."
    scene black
    show text _("{size=120}A few hours later.")
    window hide
    pause
    hide black
    show bg mc sleep sl01A
    window hide
    pause
    show bg mc sleep sl02
    with hpunch
    window hide
    pause
    mc "{i}Ehm... What was that noise!!! The wind or... the burglars...?"
    menu:
        mc "{i}Maybe I should go check it out:"
        "Yes":
            mc "{i}It would be better, take my baseball bat."
            $ tm.hour = 2
            $ tm.day = 1
            $ tm.update_image_time()
            $ sp_routine["victoria_intro"] = Commitment(chs={"unknown" : TalkObject()}, tm_start=0, tm_stop=3, id_location="house", id_room="livingroom", label_event="intro_victoria", day_deadline=2)
            jump after_wait
        "No":
            mc "{i}Na... Nothing came out."
            pass
    jump morning_intro

label intro_victoria:
    image bg prologue G01A = "/intro/G01A.webp"
    image bg prologue G01B = "/intro/G01B.webp"
    image bg prologue G02A = "/intro/G02A.webp"
    image bg prologue G02A2 = "/intro/G02A2.webp"
    image bg prologue G02B = "/intro/G02B.webp"
    image bg prologue G03 = "/intro/G03.webp"
    image bg prologue G04 vic = Composite( (gui.width, gui.height),
        (0, 0), "/intro/G04.webp",
        (0, 0), "/intro/G04-vic.webp")
    image bg prologue G04 = "/intro/G04.webp"
    image bg prologue G05 = "/intro/G05.webp"
    image bg prologue G06 = "/intro/G06.webp"

    show bg prologue G01A
    mc "{i}Oh Fuck! There's someone. This voice, though... it's familiar."
    mc "{i}Is that Victoria? Wow, that's the first time I've ever seen her so drunk. Nice little redheaded friend, though."
    show bg prologue G01B
    vct "Ha, haha... I'm drunk. Is this my house? Or yours?"
    vct "Ha, haha... I'm kidding. I know I'm funny. This night is still young. We'll knock back two more beers, then go throw bottles at some cars."
    "Red girl" "But if you can't even stand up. Ha, haha..."
    menu:
        "Go away":
            mc "{i}Better get back to bed today was a rough day."
            $ cur_room = prev_room
            call morning_intro_end
            return
        "Stay":
            pass

    vct "Hey! [krn] don't say what I can or what I... ... Oh my God, what was it like? A already! Or that I can not do."
    vct "Now you, beauty. You stay right here. And I'm going to go get those damn beers. And when I come back, let's do what I said. "
    "([vct] tries to walk on her own, but can't take a single step and falls on Kristen's back.)"
    show bg prologue G02A
    krn "Look out! [vct], are you okay?"
    vct "Okay, okay. I admit it. I'm a little too drunk. You win. Now let's do whatever you want."
    krn "I'd better take you to your room now."
    vct "No, I said what you want. We both know what you want."
    krn "[vct], I don't know what you're talking..."
    vct "Shut up! And let me taste your tongue."
    menu:
        mc "{i}Oh my God, It can't really happen. What do I do now:"
        "Intervene":
            mc "{i}Better intervene before it gets too late."
            jump morning_intro_part2
        "Stay and watch":
            mc "{i}Let's see! I'm really curious what happens next."
            pass
        "Go away":
            mc "{i}Mhmm, maybe it's better to give some privacy."
            $ cur_room = prev_room
            call morning_intro_end
            return
    show bg prologue G02A2
    krn "What? [vct] is too drunk. Haha..."
    vct "Come on. I know. You were glued to me the whole time."
    krn "[vct] you're drunk, you don't know what you're saying."
    vct "Kiss me, redhead. You won't get another chance."

    scene black
    "([krn] shyly approaches [vct]'s mouth)"
    hide black
    show bg prologue G03
    "([vct] very confidently takes charge and kisses her)"
    mc "{i}I can't believe this happened."
    show bg prologue G02B
    vct "Mhmm it tastes like cherry Big Babol. Not bad, it's my first time kissing a girl."
    krn "It's late, I'd better go."
    menu:
        mc "{i}And... now?"
        "Introduce yourself":
            mc "{i}Maybe it's best to introduce myself. It might be useful in the future."
            pass
        "Go away":
            mc "{i}Maybe it's best to leave some privacy."
            $ cur_room = prev_room
            call morning_intro_end
            return

label morning_intro_part2:
    show bg prologue G04 vic
    mc "Hi, everything okay?"
    krn "Hi, um yeah... [vct] had a bit too much to drink so I gave him a lift."
    mc "They understand each other. Sorry I haven't introduced myself. I'm [mc], the [vctR.MClabel] of [vct]."
    krn "[krn]. Nice to meet you. [vct] told me about you, I know you guys haven't had a bit that you've had ups and downs lately."
    mc "Already more downs than ups."
    vct "Hi. [krn], he's [mc], my [vctR.MClabel]. Sorry, I forgot... you have already introduced yourselves."
    mc "You go to college together?"
    vct "I'm going to sit down for a moment... You go ahead... Now I'll be back..."
    show bg prologue G04
    krn "Yes! We take the same class."
label morning_intro_part3:
    menu:
        "Party?":
            mc "Was there a party today?"
            krn "Yes, I guess you know a little bit about what college is like. By day on books and by night alcohol."
            krn "If you're of age you could come sometime."
            mc "Yeah, that's not a bad idea."
            jump morning_intro_part3
        "University?":
            mc "How's college going?"
            krn "Fine, for now."
            jump morning_intro_part3
        "Are you from here?":
            mc "Are you from here? Want to stay over?"
            krn "No thanks. I'm from North [city], but I'm staying in university housing."
            jump morning_intro_part3
        "End":
            pass
    show bg prologue G05
    mc "Well... It's getting late and I better get going."
    krn "Alright, it was nice to meet you."
    mc "Yeah... you too. Hi"
    scene black
    window hide
    pause
    mc "{i}What happened to [vct]?"
    hide black
    show bg prologue G06
    vct "zZz zZz ..."
    mc "{i}Wow, she must be drunk off her ass. Should I take her to bed! But I don't think I can do it, she's bigger than me."
    mc "{i}Whatever, she's asleep now."
label morning_intro_end:
    # TODO: cur_room = prev_room: I shouldn't do it: but if I don't do it victoria_druck will be deleted. then I have to solve the problem
    $ cur_room = prev_room
    $ tm.hour = 3
    $ tm.update_image_time()
    $ del sp_routine["victoria_intro"]
    $ sp_routine["victoria_druck"] = Commitment(chs={"vct" : TalkObject(bg_before_after="bg livingroom victoria drunk", label_talk="victoria_sleep_talk")}, tm_start=0, tm_stop=4, id_location="house", id_room="livingroom", day_deadline=2)
    return

label morning_intro:
    call temporary_end_game
    return
