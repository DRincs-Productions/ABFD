label after_deathA:
    scene black
    window hide
    pause
    hide black

    image bg dreams A01 = "/dreams/AfterdeathA01.webp"
    image bg dreams A02 = "/dreams/AfterdeathA02.webp"
    image bg dreams A03 = "/dreams/AfterdeathA03.webp"
    show bg dreams A01
    mc "{i}Huh?"
    mc "{i}What? What is this place?"
    show bg dreams A02
    mc "Hi, sorry but..."
    "old man" "Wait your turn."
    mc "Turn?!"
    menu:
        "old man" "Do not see are busy, when the time comes you can ask all the questions you want."
        "But am I the only one?":
            mc "Ehmm... But... am I the only one?"
            "old man" "You have to wait."
        "Ok":
            mc "Ok"
    scene black
    show text _("{size=120}A few hours later.")
    window hide
    pause
    hide black
    hide text
    show bg dreams A03
    "(From pc of old humo you start to hear a very faint sound)"
    "Cronist" "... Maradona takes off from the middle of the field... goes for goal... and it's... GOAL!!! GOAL!!! Maradona's hat-trick."
    "old man" "GOAL!!! GOAL!!!"
    mc "{i}Fucking old man..."
    "Cronist" "That's the end of this legendary match. It's over 6-0..."

label after_deathA_partA:
    image bg dreams A040 = "/dreams/AfterdeathA0400.webp"
    image bg dreams A041 = "/dreams/AfterdeathA0401.webp"
    image bg dreams A042 = "/dreams/AfterdeathA0402.webp"
    menu:
        "old man" "Come on, now it's your turn, if you have any questions start asking me."
        "The speaker?":
            mc "I didn't hear any speakers..."
            "old man" "Um... Yes, but you can't hear."
            mc "Bah!"
            jump after_deathA_partA
        "Where am I?":
            mc "Where am I?"
            "old man" "I thought you were smarter than that. I think you can figure it out for yourself."
            jump after_deathA_partA
        "Famous people?":
            mc "Can I meet any famous people?"
            "old man" "No, I'm sorry. It's not your area."
            jump after_deathA_partA
        "No questions":
            mc "I have no more questions"
    "old man" "Ok... I found your file... [mc] of [mcI.age] years old... "
    mc "Mhmm... yes?!"
    "old man" "Missing parents, still a virgin, no desire to strive, no good action in particular and not bad either...."
    "old man" "Mhmm... interesting... they haven't made any decisions yet. So... I should carefully inspect your file."
    "old man" "{i}I'm almost done with my shift, just didn't need your file. I should stay a few more hours."
    "old man" "Or..."
    mc "Or..."
    "old man" "Or?"
    "old man" "I have an idea! Boy come with me."
    show bg dreams A040
    "old man" "Come on, come closer. Don't be afraid, I won't bite. You can see the whole world from up here. And right down here is your neighborhood."
    mc "Oh! Wow! This view is terrifying and awesome at the same time."
    "old man" "Boy listen to an old man who has a little more experience than you. Up here it's an extremely boring place, it's all so repetitive. You don't have any freedom of choice."
    "old man" "While down there... eh down there it's great only you are the limit of your actions."
    "old man" "You can do anything you want. Drugs, alcohol, sex ... or if it makes you feel better you can help people. The choice is yours alone. You shouldn't have wasted all this time reflecting on your past, but taking action."
    mc "Yeah, too bad I can't do that anymore."
    "old man" "Yeah...too bad..."
    "old man" "If you lean a little more, you can see your body from up here."
    show bg dreams A041
    mc "Really?! Where?"
    "old man" "There!"
    show bg dreams A042
    mc "AAAAA!!!! aaaaaa!!!"
    "old man" "And another practice results just in time for the shift change."

    scene black
    window hide
    pause
    hide black
    return
