default mc_dress_normal = ""
default mc_dress_home = ""

label mc_wardrobe:
    image bg mc dress_up 01 = "/MC/Dress up/01.webp"
    show bg mc dress_up 01
    menu:
        "What do you want to change?"
        "Usual clothes":
            call mc_wardrobe_normal
        "Home clothes":
            call mc_wardrobe_home
        "Close Wardrobe":
            hide mc
            pass
    jump after_wait

label mc_wardrobe_home:
    image mc home 01 = "/MC/Dress up/01-home.webp"
    image mc home 02 = "/MC/Dress up/01-home-sumtime.webp"
    menu:
        "Home clothes:"
        "Black T-shirt":
            show mc home 01
            $ mc_dress_home = ""
        "White T-shirt":
            show mc home 02
            $ mc_dress_home = "-sumtime"
        "Select and return":
            return
    jump mc_wardrobe_home

label mc_wardrobe_normal:
    image mc normal 01 = "/MC/Dress up/01-normal.webp"
    menu:
        "Usual clothes:"
        "Default":
            show mc normal 01
            $ mc_dress_normal = ""
        "Select and return":
            return
    jump mc_wardrobe_normal

label first_dress_up:
    image bg mc dress_up 02 = "/MC/Dress up/02.webp"
    show bg mc dress_up 02
    "{i}Better to put on something clean."
    $ bl_values["mc_wardrobe"] = True
    $ sp_actions.pop('mc_wardrobe')
    jump mc_wardrobe
