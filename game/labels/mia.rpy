image bg mia dress_up 01A = Composite( (gui.width, gui.height),
    (0, 0), "/Mia/Dress up/01.webp",
    (0, 0), "/Mia/Dress up/01B.webp")
image bg mia dress_up 01A mc = Composite( (gui.width, gui.height),
    (0, 0), "/Mia/Dress up/01.webp",
    (0, 0), "/Mia/Dress up/01B.webp",
    (0, 0), "/Mia/Dress up/01-MC.webp",)
image bg mia dress_up 01C = "/Mia/Dress up/01.webp"


label intro_mia_change_clothes:
    show bg door open
    menu:
        mc "{i}The door is closed... I think he's getting dressed."
        "Spy":
            show bg mia dress_up 01A
            pause
            show bg mia dress_up 01A mc
            mc "{i}I can't believe I'm actually doing this..."
            mc "{i}I'm so worked up. I'm starting to get hard."
            show bg mia dress_up 01A
            pause
            show bg mia dress_up 01C
            mia "Who is it?! [for_emyR.MClabel]?"
            mc "{i}Fuck! Just in time. Better leave before she suspects something."
            show bg mia dress_up 01A
            mia "{i}I could have sworn that there was someone.... Bah! It's just my imagination."
            $ cur_room = prev_room
            $ closed_rooms["mia_room"] = sp_routine["mia_change_clothes"]
            return
        "Back":
            "No! I'm not a pervert yet."
            $ cur_room = prev_room
            return
