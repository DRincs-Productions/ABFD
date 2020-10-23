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
        mc "For me they are a second family and I'll tell you a little about them."

    show profile jn 01
    mc "[jn] is married to [emy] and for me he is like a second father. He [jn] is a former Navy Seals, with the last mission in [jnMission] he was awarded the pension. [jnMission] has changed him, he started drinking, he is never home and when he is there he speaks very little. [emy] tried to help him, but she got only quarrels and insults."

    show profile emy 01
    mc "[emy] is the classic housewife, cooks, washes and takes care of the family. When she was young she was a {b}model{/b}, but she is very reserved about her past. Sometimes when I come home I see her flipping through old magazines. She leaves home very little, [jn] never takes her anywhere."

    show profile arn 01
    mc "[arn] is the same age as me, we attend the same {b}school{/b} and are in the same year, but in different classes. Her class is the best in the history of our school, while mine is probably the worst. That's why they left 2 days ago on a trip while we didn't."

    show profile vct 01
    mc "[victoria] Victoria is a {b}college freshman{/b}, she likes to go out in the evening and have fun with her friends. The last few days have been difficult for her too, she often comes back completely {b}drunk{/b} in the evening. Our relationship is mostly love and hate."

    show profile mia 01
    mc "[mia] is the youngest in the house and she is mommy's darling. Since she changed schools she has various difficulties and often asks me to {b}help her with her homework{/b}. Her big dream is to become an [influencer], but her [for_emyR.MClabel] forbids her to post pictures."
    hide profile
    jump presentations

label presentations_montell:

label prologue:
    return
