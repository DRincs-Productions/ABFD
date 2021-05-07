image bg at_table preparation = Composite( (gui.width, gui.height),
    (0, 0), "/family/at_table/preparation01.webp",
    (0, 0), "/family/at_table/preparation01A.webp")
image bg at_table preparation A = Composite( (gui.width, gui.height),
    (0, 0), "/family/at_table/preparation01.webp",
    (0, 0), "/family/at_table/preparation01B.webp")

# Dinner
image bg at_table dinner = "/family/at_table/dinner.webp"

image mc at_table dinner:
    "/family/at_table/dinner-MC01A[mc_dress_normal].webp"
    pause 0.3
    "/family/at_table/dinner-MC01B[mc_dress_normal].webp"
    pause 0.1
    repeat

image mc at_table dinner home:
    "/family/at_table/dinner-MC01A[mc_dress_home].webp"
    pause 0.3
    "/family/at_table/dinner-MC01B[mc_dress_home].webp"
    pause 0.1
    repeat

image mia at_table dinner:
    "/family/at_table/dinner-MiaA-.webp"
    pause 0.5
    "/family/at_table/dinner-MiaB-.webp"
    pause 0.1
    repeat

image emily at_table dinner:
    pause 0.1
    "/family/at_table/dinner-EmilyA-.webp"
    pause 0.10
    "/family/at_table/dinner-EmilyB-.webp"
    pause 0.1
    repeat

# help
image bg at_table help A = Composite( (gui.width, gui.height),
    (0, 0), "/family/at_table/help.webp",
    (0, 0), "check:/family/at_table/help[mc_dress_normal].webp")

label dinner_family_emy_mia:
    show bg at_table dinner
    show mc at_table dinner home
    show mia at_table dinner
    show emily at_table dinner
    window hide
    pause
    return

label clean_dinner_family:
    window hide
    pause
    return

label first_at_table_preparation:
    if (bl_values["mc_wardrobe"]):
        emy "Ok. it's ready, let's have dinner."
        jump at_table_dinner_A
    else:
        show bg at_table preparation A
        emy "Here it is ready! Go change if you want to eat."
        mia "Ah ah! Get a move on here we are hungry."
        $ sp_actions["mc_wardrobe"] = Action(_("Wardrobe"), "/interface/menu-wardrobe.webp", label = "first_dress_up", sp_room='mc_room')
        show bg at_table preparation
        call screen room_navigation

label helpA:
    hide bg
    window hide
    pause
    show bg at_table help A
    window hide
    pause
    mc "{i}It's a boring job, but someone had to do it."
    window hide
    pause
    return

label at_table_dinner_A:
    call dinner_family_emy_mia

    "(Silence a very awkward)"
    mc "{i}Mhmm, maybe I should break the ice by congratulating [emy] on dinner. But I don't know if that's appropriate."
    window hide
    pause
    emy "Sorry honey, I didn't even ask you how it went at [bff]'s house today."
    mc "Don't apologize, you don't have to."
    mc "Yesterday... If I remember correctly... We played some [console], and talked a little bit about school and old times."
    emy "What did you guys eat?"
    mc "Last night [tam] wasn't home, so we ordered pizza from [pizzeria]. While for breakfast/lunch we got takeout at mcdonald with [tam]."
    emy "It sounds like [tam] didn't really want to sew Ah Ah. However, it's not very salty like they eat... so don't get used to it."
    emy "You and [bff] have a good friendship, you seem almost like brothers. Even though you are very different."
    menu:
        "Yeah, because...":
            mc "Yeah, we're very close. I've known him for a long time and also because we have a very similar background."
        "[bbf]'s not that great":
            mc "Yes, he's a reliable friend. if a bit awkward and boring."
        "For now":
            mc "Yes, also because I haven't been here long. But I'm sure I'll be making more."
    mia "Do you miss [old_city]? I mean you left everyone you knew behind."
    emy "[mia]! You don't have to ask those questions. It makes sense that you're still in some pain."
    menu:
        "Yeah":
            mc "Yeah, I miss it a little bit. But it's not bad here."
        "No":
            mc "Absolutely not, it was a horrible place."
        "Fuck [old_city]":
            mc "Fuck [old_city] and whoever lives there. It brought me nothing but trouble."
        "I do not want to talk about it":
            mc "I'd rather not talk about it yet, I think you'll understand."
    mia "Mhmm, I understand."

    emy "What about you [mia]! Are you ready for the exam tomorrow?"
    mia "Mhmm, yes... but... the professor is up too strict. I'm sure he hates me."
    emy "Ah Ah yes of course, of course."
    mia "But he does."
    emy "And... Why would he hate you?"
    mia "I don't know, that's the problem."
    emy "I'm sure if you studied you'll get through it."

    window hide
    pause

    mc "Great dinner. everything is great."
    emy "You mean \"was\"."
    mc "AhAh. Yeah, everything was great."
    emy "Honey, I'm glad you enjoyed it."
    menu:
        "[mia] If you need to come back, go ahead. Help me clear the table. Right?!"
        "Yes":
            mc "Okay, that's good."
            $ stats['emy'].change('favour', 2)
        "No":
            mc "No, I don't really want to."
            emy "What?! No... You make it come."
            mc "Okay, [mom]."
            $ stats['emy'].change('favour', -2)
        "If I have to...":
            emy "If I have to..."
            mc "Yes, honey. Thank you."
            $ stats['emy'].change('favour', 1)

    call clean_dinner_family
    call helpA

    hide bg
    mc "This is the last dish."
    emy "Wait a minute."
    mc "{i}Why are you looking at me like that?"
    show bg emily kitchen talk
    emy "Honey, I called [tam]..."
    mc "{i}Oh no! She probably told her about the school report."
    emy "Tomorrow morning, she'll give you a ride to school. Because that bastard took the car away too."
    mc "{i}Phew, danger averted."
    emy "But I don't want to be too much trouble. You're a big boy now. Tomorrow she'll give you a ride, but then you'll have to make your own arrangements. You should get a season ticket for public transportation, I'll give you the money tomorrow."
    mc "Beh... we could use your car."
    emy "That piece of crap!? Honey it hasn't been turned on in years, I don't think it still works. I should get it checked out first."

label at_table_dinner_A_part2:
    menu:
        emy "I'm not gonna tell you again, so we're good?"
        "Where do I go?":
            mc "All clear, however I don't know where to get subscriptions."
            emy "Any store or tobacconist. I know the sandwich shop at your school sells them."
            jump at_table_dinner_A_part2
        "I would like the money now":
            mc "Could you give me the money right away? I'm afraid I might forget."
            if (stats['emy'].get('favour') < 2):
                emy "Do you see any pockets? I don't have any money on me"
            else:
                emy "No, honey. I'll remember it."
            jump at_table_dinner_A_part2
        "Talk about [jn]":
            mc "Have you heard from [-------------dad]?"
            emy "No! And I don't want to talk about him for a while. I could use a little distraction."
        "No questions":
            mc "Okay, all clear."
    hide bg
    mc "There should be a good movie on tonight."
    emy "A good movie is just what you need. I'm going to start sitting on the couch, as soon as you want to join me. Thanks again for the help, honey."

    $ tm.new_hour(2)
    jump after_wait
