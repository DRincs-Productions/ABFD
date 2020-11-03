init python:
    # Multi Game Persistent Character Names
    # Recommended: male_fname, male_sname, female_fname, female_sname, futa_fname, futa_sname, other_fname or other_sname (or any, or all of these).
    # Other recommendations: bigsis_fname, lilsis_fname, bigbro_fname, lilbro_fname, mom_fname, dad_fname, malebff_fname or femalebff_fname. (Again, use any or use none).
    mp_ndata = MultiPersistent("namedata.f95zone.to")

    class Relationships():
        def __init__(self):
            self.unknown = 0
            self.single = 1
            self.engaged = 2
            self.married = 3
            self.divorced = 4
            self.widow = 5
    ## Information about a character
    # to use: default ... = Information("NPC name", age)
    # exemple:
    # default girlI = Information("Eileen", 18, "university student" [or job.university_student if it is a registered job], rel.engaged, mc,
    # "she has always been before class. as a child they made fun of her because she had the appliance. ...")
    # default boyI = Information("Unknown Boy", "Unknown", job.unknown, rel.unknown, "Unknown", "Unknown")
    class Information():
        def __init__(self, name, sname, age, active, rel_status, rel_partner, story):
            self.name_default = name
            self.name = name
            self.sname_default = sname
            self.sname = sname
            self.age_default = age
            self.age = age
            self.active = active
            self.rel_status = rel_status
            self.rel_partner = rel_partner
            self.story = story
        def changeName(self):
            self.name = renpy.input("{i}(Default: " + self.name_default + "){/i}")
            self.name = self.name.strip() or self.name_default
        def changeSurname(self):
            self.sname = renpy.input("{i}(Default: " + self.sname_default + "){/i}")
            self.sname = self.sname.strip() or self.sname_default
        def changeAge(self):
            self.age = renpy.input("{i}(Default: " + str(self.age_default) + "){/i}")
            self.age = self.age.strip() or self.age_default
        def is_engaged(self):
            return (rel_status == rel.engaged or rel_status == rel.married)
        def setActive(self, amt):
            self.active = amt
    ## Type of relationship
    # to use: default ... = Relationship("type of relationship that NCP has with MC", 
    # "type of relationship that MC has with NCP", boolean (if this relationship is active))
    # exemple:
    # default girlR = Relationship("girlfriend", "boyfriend", True)
    class Relationship():
        def __init__(self, NPClabel, MClabel, active):
            self.NPClabel_default = NPClabel
            self.NPClabel = NPClabel
            self.MClabel_default = MClabel
            self.MClabel = MClabel
            self.active = active
        def changeNPClabel(self):
            self.NPClabel = renpy.input("{i}(Default: " + self.NPClabel_default + "){/i}")
            self.NPClabel = self.NPClabel.strip() or self.NPClabel_default
        def changeMClabel(self):
            self.MClabel = renpy.input("{i}(Default: " + self.MClabel_default + "){/i}")
            self.MClabel = self.MClabel.strip() or self.MClabel_default
        def setActive(self, amt):
            self.active = amt

define rel = Relationships()

label renaming_mc:
    # allow default name(s) to be saved across multiple games
    if renpy.variant("pc"):
        if mp_ndata.male_fname != None:
            $ mcI.name_default = mp_ndata.male_fname
        if mp_ndata.male_sname != None:
            $ mcI.sname_default = mp_ndata.male_sname

    "Player" "My name is:"
    $ mcI.changeName()
    "Player" "My surname is:"
    $ mcI.changeSurname()

    if renpy.variant("pc"):
        if mcI.name != mcI.name_default:
            $ mp_ndata.male_fname = mcI.name
        if mcI.sname != mcI.sname_default:
            $ mp_ndata.male_sname = mcI.sname
        $ mp_ndata.save()
    return

label live_with:
    # allow default name(s) to be saved across multiple games
    if renpy.variant("pc"):
        if mp_ndata.mom_fname != None:
            $ emyI.name_default = mp_ndata.mom_fname
        if mp_ndata.mom_sname != None:
            $ emyI.sname_default = mp_ndata.mom_sname
        if mp_ndata.dad_fname != None:
            $ jnI.name_default = mp_ndata.dad_fname
        if mp_ndata.dad_sname != None:
            $ jnI.sname_default = mp_ndata.dad_sname
        if mp_ndata.bigsis_fname != None:
            $ vctI.name_default = mp_ndata.bigsis_fname
        if mp_ndata.bigsis_sname != None:
            $ vctI.sname_default = mp_ndata.bigsis_sname
        if mp_ndata.lilsis_fname != None:
            $ miaI.name_default = mp_ndata.lilsis_fname
        if mp_ndata.lilsis_sname != None:
            $ miaI.sname_default = mp_ndata.lilsis_sname
        if mp_ndata.female_fname != None:
            $ arnI.name_default = mp_ndata.female_fname
        if mp_ndata.female_sname != None:
            $ arnI.sname_default = mp_ndata.female_sname
    menu:
        "Step family" if(incs):
            $ incs = True
            $ emyR.MClabel = __("son")
            $ emyR.NPClabel = __("mom")
            $ jnR.MClabel = emyR.MClabel
            $ jnR.NPClabel = __("dad")
            $ vctR.MClabel = __("brother")
            $ vctR.NPClabel = __("sister")
            $ miaR.MClabel = vctR.MClabel
            $ miaR.NPClabel = vctR.NPClabel
            $ arnR.MClabel = vctR.MClabel
            $ arnR.NPClabel = vctR.NPClabel
            $ for_emyR.MClabel = emyR.NPClabel
            $ for_emyR.NPClabel = __("daughter")
            $ for_jnR.MClabel = jnR.NPClabel
            $ for_jnR.NPClabel = for_emyR.NPClabel
            $ housemates = __("sisters")
        "Family friends":
            $ incs = False
            $ emyR.MClabel = __("friend's son")
            $ emyR.NPClabel = __("mom's friend")
            $ jnR.MClabel = emyR.MClabel
            $ jnR.NPClabel = __("dad's friend")
            $ vctR.MClabel = __("family friend")
            $ vctR.NPClabel = __("family friend")
            $ miaR.MClabel = vctR.MClabel
            $ miaR.NPClabel = vctR.NPClabel
            $ arnR.MClabel = vctR.MClabel
            $ arnR.NPClabel = vctR.NPClabel
            $ for_emyR.MClabel = __("mom")
            $ for_emyR.NPClabel = __("daughter")
            $ for_jnR.MClabel = __("dad")
            $ for_jnR.NPClabel = for_emyR.NPClabel
            $ housemates = __("housemates")
        "A rented house funded by the school":
            $ incs = False
            $ emyR.MClabel = __("landlord")
            $ emyR.NPClabel = __("leaseholder")
            $ jnR.MClabel = emyR.MClabel
            $ jnR.NPClabel = emyR.NPClabel
            $ vctR.MClabel = __("housemate")
            $ vctR.NPClabel = __("housemate")
            $ miaR.MClabel = vctR.MClabel
            $ miaR.NPClabel = vctR.NPClabel
            $ arnR.MClabel = vctR.MClabel
            $ arnR.NPClabel = vctR.NPClabel
            $ for_emyR.MClabel = emyR.NPClabel
            $ for_emyR.NPClabel = emyR.MClabel
            $ for_jnR.MClabel = jnR.NPClabel
            $ for_jnR.NPClabel = jnR.MClabel
            $ housemates = __("housemates")
        "{i}\"Customize\"":
            call customize_mc_family
        mc "Now I live with/in:"
    if renpy.variant("pc"):
        if emyI.name != emyI.name_default:
            $ mp_ndata.mom_fname = emyI.name
        if emyI.sname != emyI.sname_default:
            $ mp_ndata.mom_sname = emyI.sname
        if jnI.name != jnI.name_default:
            $ mp_ndata.dad_fname = jnI.name
        if jnI.sname != jnI.sname_default:
            $ mp_ndata.dad_sname = jnI.sname
        if vctI.name != vctI.name_default:
            $ mp_ndata.bigsis_fname = vctI.name
        if vctI.sname != vctI.sname_default:
            $ mp_ndata.bigsis_sname = vctI.sname
        if miaI.name != miaI.name_default:
            $ mp_ndata.lilsis_fname = miaI.name
        if miaI.sname != miaI.sname_default:
            $ mp_ndata.lilsis_sname = miaI.sname
        if arnI.name != arnI.name_default:
            $ mp_ndata.female_fname = arnI.name
        if arnI.sname != arnI.sname_default:
            $ mp_ndata.female_sname = arnI.sname
        $ mp_ndata.save()
    return

label renaming_mc_family:
    show photo family 01
    show arrow:
        xalign 0.7 yalign 0.2 rotate 180
    "My [emyR.NPClabel]'s name:"
    $ emyI.changeName()
    show arrow:
        xalign 0.3 yalign 0.2 rotate 0
    "My [jnR.NPClabel]'s name:"
    $ jnI.changeName()
    show photo family 02
    show arrow:
        xalign 0.2 yalign 0.2 rotate 0
    "My little [miaR.NPClabel]'s name:"
    $ miaI.changeName()
    show arrow:
        xalign 0.7 yalign 0.4 rotate 180
    "My (coetaneous) [arnR.NPClabel]'s name:"
    $ arnI.changeName()
    show arrow:
        xalign 0.2 yalign 0.2 rotate 0
    "My big [vctR.NPClabel]'s name:"
    $ vctI.changeName()
    hide arrow
    hide photo
    return

label customize_mc_family:
    show photo family 01
    show arrow:
        xalign 0.7 yalign 0.2 rotate 180
    "Her name is:"
    $ emyI.changeName()
    "She is my:"
    $ emyR.changeNPClabel()
    "I'm [emy]'s:"
    $ emyR.changeMClabel()
    show arrow:
        xalign 0.3 yalign 0.2 rotate 0
    "His name is:"
    $ jnI.changeName()
    "He is my:"
    $ jnR.changeNPClabel()
    "I'm [jn]'s:"
    $ jnR.changeMClabel()
    show photo family 02
    show arrow:
        xalign 0.7 yalign 0.1 rotate 180
    "Her name is:"
    $ miaI.changeName()
    "She is my:"
    $ miaR.changeNPClabel()
    "I'm [mia]'s:"
    $ miaR.changeMClabel()
    menu:
        "Yes":
            $ skip = 1
            $ vctR.MClabel = "[miaR.MClabel]"
            $ vctR.NPClabel = "[miaR.NPClabel]"
            $ arnR.MClabel = "[miaR.MClabel]"
            $ arnR.NPClabel = "[miaR.NPClabel]"
        "No":
            $ skip = 0
        "Do you want to assign the last two values to the other [housemates] too?"
    show arrow:
        xalign 0.7 yalign 0.4 rotate 180
    "Her name is:"
    $ arnI.changeName()
    if (skip != 1):
        "She is my:"
        $ arnR.changeNPClabel()
        "I'm [arn]'s:"
        $ arnR.changeMClabel()
    show arrow:
        xalign 0.2 yalign 0.2 rotate 0
    "Her name is:"
    $ vctI.changeName()
    if (skip != 1):
        "She is my:"
        $ vctR.changeNPClabel()
        "I'm [vct]'s:"
        $ vctR.changeMClabel()

    hide arrow
    "Who is [vct] to [emy] and [jn] (also applies to [mia] and [arn])?"
    $ for_emyR.changeNPClabel()
    $ for_jnR.NPClabel = for_emyR.NPClabel
    "For [vct], [mia] and [arn], [jn] is them:"
    $ for_jnR.changeMClabel()
    "For [vct], [mia] and [arn], [emy] is them:"
    $ for_emyR.changeMClabel()
    hide photo

    if (emyR.NPClabel.lower() == "mom" or emyR.NPClabel.lower() == "mother"):
        $ incs = True
        $ housemates = __("sisters")
    return

label renaming_friend:
    # allow default name(s) to be saved across multiple games
    if renpy.variant("pc"):
        if mp_ndata.malebff_fname != None:
            $ bbfI.name_default = mp_ndata.malebff_fname
        if mp_ndata.malebff_sname != None:
            $ bbfI.sname_default = mp_ndata.malebff_sname
    "[mc]'s [bbfR.NPClabel] is called:"
    $ bbfI.changeName()
    if renpy.variant("pc"):
        if bbfI.name != bbfI.name_default:
            $ mp_ndata.malebff_fname = bbfI.name
        if bbfI.sname != bbfI.sname_default:
            $ mp_ndata.malebff_sname = bbfI.sname
        $ mp_ndata.save()
    return
