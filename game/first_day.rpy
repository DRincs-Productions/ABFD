label intro:
    # Presentation of Liam
    play ambience "audio/ambience-train.ogg"
    show profile mc 01
    with dissolve
    call renaming_mc
    $ grade.update_average()
    mc "Hi, I'm a normal [mcI.age] year old boy with classic problems and no desire to commit, but just to have fun. I don't have a {b}girlfriend{/b}, a {b}job{/b} or concrete plans for the future and my school situation is gross. In the {b}school report of the first quarter{/b} I have all [grade.average]."
    mc "My family is worried about my poor results and some of my behaviors, which is why they are deciding whether to keep me at home or have me transferred to a hateful [catholic_institute]. I have to make sure that this will never happen."
    mc "To be honest, my real family died in a plane crash. After their death he moved me from [old_city] to [city] where I started a new life."
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
            jump presentations_montell
            pass
        "Skip":
            call renaming_friend
            hide profile
            stop ambience fadeout 1.0
            jump prologue
        mc "For me they are a second family."

    show profile jn 01
    mc "[jn] is married to [emy], for me he is like a second father. He is a former Navy Seals, with the last mission in [jnMission] he was awarded the pension. [jnMission] has changed him, he started drinking, he is never at home and when he is there he speaks very little. [emy] tried to help him, but she got only quarrels and insults."

    show profile emy 01
    mc "[emy] is the classic housewife, cooks, washes and takes care of the family. When she was young she was a {b}model{/b}, but she is very reserved about her past. Sometimes when I come home I see her flipping through old magazines. She leaves home very little, [jn] never takes her anywhere."

    show profile arn 01
    mc "[arn] is the same age as me, we attend the same {b}school{/b} and are in the same year, but in different classes. Her class is the best in the history of our school, while mine is probably the worst. That's why, 2 days ago, they left on a school trip while we didn't."

    show profile vct 01
    mc "[victoria] is a {b}college freshman{/b}, she likes to go out in the evening and have fun with her friends. The last few days have been difficult for her too, she often comes back completely {b}drunk{/b} in the evening. Our relationship is mostly love and hate."

    show profile mia 01
    mc "[mia] is the youngest in the house and she is [for_emyR.MClabel]'s darling. Since she changed schools she has various difficulties and often asks me to {b}help her with her homework{/b}. Her big dream is to become an [influencer], but her [for_emyR.MClabel] forbids her to post pictures."
    hide profile
    jump presentations

label presentations_montell:
    show background animated residential
    call travel_tammy_bbf
    mc "{i}Now I'm on my way home, after spending the night at the {b}[tamI.sname]'s house{/b}. They are the only people from my old life that I still hang out with. Next to me there is:"
    call renaming_friend
    mc "{i}And this is his mother, [tam]. They too lost someone in the plane crash, her father and her husband {b}Mr. [mrJohnson] Johnson{/b}. He and my father were colleagues and that is why I have known them since childhood."
    mc "{i}And so, a few weeks after I left my old city, they preferred to create a new life by moving here to my own neighborhood, except his brother who preferred to stay."
    mc "{i}This neighborhood is a nice place to live, it is a quiet area, not far away there is the sea, some clubs and there are beautiful girls."
    tam "What's wrong with you guys!? You are so quiet."
    bbf "All is well. It's just that yesterday we played at the [console] until late at night."
    tam "Who won in the end?"
    bbf "I won, I literally shredded it. He is too scarce."
    mc "It's just luck."
    bbf "Modestly this is talent, you have to train to reach my level."
    tam "Yeah! [bbf] spends hours in front of a stupid screen after school."
    mc "Don't worry, [tam]. I convince him to go out. We also joined the school's [mcSport] team."
    bbf "I don't know if this was a good idea and then mom, you know I don't go out much because I don't have many friends here."
    tam "Don't worry, honey. I'm sure when you start [mcSport] you'll make a few friends."
    tam "By the way [mc], did you give your [emyR.NPClabel] your school report card?"
    mc "Not yet, I'm going to talk to her tonight."
    tam "Well, you have arrived."
    show background 02 house mc
    call travel_tammy02
    tam "Wait [mc]. Remember that if you don't tell her, I will tell [emy] when I see her."
    mc "All right, [tam]. I will."
    tam "Well, you can go."
    show mc 02 get_out
    bbf "Bye, [mc]. See you."
    mc "Bye"
    call clean_travel

label prologue:
    image background prologue A01:
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

    show background prologue A01
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

    image background prologue C01 = "/intro/C01.webp"
    image background prologue C02 = "/intro/C02.webp"
    image background prologue C02 blur = im.Blur("/intro/C02.webp", 7)
    image background prologue C03 = "/intro/C03.webp"
    image background prologue C04 = "/intro/C04.webp"
    image background prologue C05 = "/intro/C05.webp"
    image note prologue = "/intro/note.webp"
    $ emyP.favour = 20
    $ x = 0
    show background living_room spydoor01
    show emy living_room spydoor01 cries
    mc "I am home!"
    show mc living_room spydoor01 look01
    with dissolve
    mc "{i}What!? What is happening?"
    mc "{i}My [emyR.NPClabel] is crying!?"
    hide mc
    hide emy
    show background prologue C01
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
            emy "Ehi! You can't talk about your [jnR.NPClabel] like that."
        "{i}I knew it...":
            mc "{i}I knew this would happen sooner or later."
    emy "Come on, sit down."
    show background prologue C02
    with dissolve
    emy "When I woke up I found this in the kitchen. Do you realize... [mia] could have found it."
    show note prologue
    if renpy.variant("pc"):
        show background prologue C02 blur with dissolve
    window hide
    pause
    jn "{i}My presence only causes problem. I will fix our problem, but then I will not come back. John"
    hide note
    show background prologue C02
    emy "Now how are we going to do without him!?"
    menu:
        "His loss":
            $ x += 5
            show background prologue C03
            mc "Mom if anyone has lost, it's him. I could never leave a woman like you."
            emy "Honey, I'm lucky to have you who know how to cheer me up."
        "What happened? {color=#f00}(Probability 10\%)":
            $ val = False
            if (val):
                $ x += 1
                show background prologue C03
                mc "What happened? Did he put his hands on you?"
                emy "No No, honey we just had a fight as usual. You know that since he came back from [jnMission] he has become a different person."
                mc "Yesterday I tried to hide the [jnAlcol], but it was useless. He found it and got drunk even more than usual."
                emy "Honey, you know, I tried to help him, but yesterday I couldn't take it anymore. I told him he could do what he wanted, but this is not a home for junkies and alcoholics. And if he wanted to continue, he could leave."
            else:
                $ x -= 1
                show background prologue C04
                mc "Okay, but I wanted to understand what happened yesterday. If he left for some reason or something you told him."
                emy "So in your opinion it may be my fault that he left!?"
                mc "No! I didn't mean that. It's just that..."
                emy "Now I want to be alone for a while, go ahead."
                jump prologue_end
        "Go away":
            $ x -= 5
            show background prologue C04
            emy "OK, [emyR.NPClabel]. Now I'm a little tired, I'm going to my room."
            jump prologue_end
    emy "I've kept you long enough, go ahead."

label prologue_end:
    show background prologue C05 with dissolve
    $ emyP.changeFavour(x)
    mc "{i}Shit! I've got enough problems of my own, now I need this too."
    mc "{i}Who knows how mine is?! maybe I should talk to her, she will probably tell me something more."
    call temporary_end_game
    return
