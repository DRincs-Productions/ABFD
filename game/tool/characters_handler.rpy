init python:
    # Multi Game Persistent Character Names
    # Recommended: male_fname, male_sname, female_fname, female_sname, futa_fname, futa_sname, other_fname or other_sname (or any, or all of these).
    # Other recommendations: bigsis_fname, lilsis_fname, bigbro_fname, lilbro_fname, mom_fname, dad_fname, malebff_fname or femalebff_fname. (Again, use any or use none).
    mp_ndata = MultiPersistent("namedata.f95zone.to")

    class Information():
        """Information about a character
        to use: default ... = Information("NPC name", age)
        exemple:
        default girlI = Information("Eileen", 18, "university student" [or job.university_student if it is a registered job], rel.get('engaged'), mc,
        "she has always been before class. as a child they made fun of her because she had the appliance. ...")
        default boyI = Information("Unknown Boy")"""
        def __init__(self,
            name,
            sname = None,
            age = None,
            active = True,
            rel_status = None,
            rel_partner = None,
            story = None,
            other_values = {}):
            # I use a dictionary because it is the best solution for compatibility and not to create variables that may not be used.
            self.memory = {}
            self.memory.update(other_values)
            # Great for reporting that a character has not yet been discovered
            self.active = active

            self.name = name
            self.sname = sname
            self.age = age
            # default values
            self.set("name_default", name)
            self.set("sname_default", sname)
            self.set("age_default", age)
            # default values
            self.set("rel_status", rel_status)
            self.set("rel_partner", rel_partner)
            self.set("story", story)

        def changeName(self):
            """Rename character name"""
            self.name = renpy.input("{i}(Default: " + self.get("name_default") + "){/i}")
            self.name = self.name.strip() or self.get("name_default")
            if (self.get("name_default") == "Unknown"):
                self.set("name_default", self.name)
        def changeSurname(self):
            """Rename the character's last name"""
            self.sname = renpy.input("{i}(Default: " + self.get("sname_default") + "){/i}")
            self.sname = self.sname.strip() or self.get("sname_default")
            if (self.get("sname_default") == "Unknown"):
                self.set("sname_default", self.sname)
        def changeAge(self):
            """Age changes"""
            self.age = renpy.input("{i}(Default: " + str(self.get("age_default")) + "){/i}")
            self.age = self.age.strip() or self.get("age_default")
            if (self.get("age_default") == "Unknown"):
                self.set("age_default", self.age)
        def get(self, text):
            """Returns the value "text", in case it does not exist returns \"Unknown\""""
            if text in self.memory:
                return self.memory[text]
            else:
                return "Unknown"
        def set(self, text, value):
            """Function to set or add a new value"""
            if (text != None and text != ""):
                self.memory[text] = value
            else:
                remove(text)
        def remove(self, text):
            """Delete the text value"""
            del memory[text]
        def setActive(self, amt):
            """Cabia the active value according to the parameter (Tip: True/False)"""
            self.active = amt
        def getRelStatus(self, amt):
            """Returns the state of the character relationship (I recommend using rel values)"""
            return self.get("rel_status")
        def getRelPartner(self, amt):
            """It recalls the name of the character with whom it has a relationship"""
            return self.get("rel_partner")
        def is_engaged(self):
            """Return True if the character is currently in a romantic relationship with someone"""
            return (rel_status == rel.get('engaged') or rel_status == rel.get('married'))

    class Relationship():
        """Type fi relationship between you (MClabel) and NPC NPClabel
        to use: default ... = Relationship("type of relationship that NCP has with MC", 
        "type of relationship that MC has with NCP", boolean (if this relationship is active))
        exemple:
        default girlR = Relationship("girlfriend", "boyfriend", True)"""
        def __init__(self,
            NPClabel = None,
            MClabel = None,
            active = True):

            self.memory = {}
            # nickname by which MC calls NCP
            self.NPClabel = NPClabel
            # nickname by which NCP calls MC
            self.MClabel = MClabel
            # default values
            self.set("NPClabel_default", NPClabel)
            self.set("MClabel_default", MClabel)

            self.active = active
        def changeNPClabel(self):
            """Change the nickname of the PCN"""
            self.NPClabel = renpy.input("{i}(Default: " + self.get("NPClabel_default") + "){/i}")
            self.NPClabel = self.NPClabel.strip() or self.get("NPClabel_default")
            if (self.get("NPClabel_default") == "Unknown"):
                self.set("NPClabel_default", self.NPClabel)
        def changeMClabel(self):
            """Edit the nickname of the MC"""
            self.MClabel = renpy.input("{i}(Default: " + self.get("MClabel_default") + "){/i}")
            self.MClabel = self.MClabel.strip() or self.get("MClabel_default")
            if (self.get("MClabel_default") == "Unknown"):
                self.set("MClabel_default", self.MClabel)
        def get(self, text):
            """Returns the value "text", in case it does not exist returns \"Unknown\""""
            if text in self.memory:
                return self.memory[text]
            else:
                return "Unknown"
        def set(self, text, value):
            """Function to set or add a new value"""
            if (text != None and text != ""):
                self.memory[text] = value
            else:
                remove(text)
        def remove(self, text):
            """Delete the text value"""
            del memory[text]
        def setActive(self, amt):
            """Change the active value according to the parameter (Tip: True/False)"""
            self.active = amt

define rel = {
        'rel_single'    :   0,
        'rel_engaged'   :   1,
        'rel_married'   :   2,
        'rel_divorced'  :   3,
        'rel_widow'     :   4,
    }


label renaming_mc:
    # allow default name(s) to be saved across multiple games
    if renpy.variant("pc"):
        if mp_ndata.male_fname != None:
            $ mcI.set("name_default", mp_ndata.male_fname)
        if mp_ndata.male_sname != None:
            $ mcI.set("sname_default", mp_ndata.male_sname)

    "Player" "My name is:"
    $ renpy.music.set_pause(True, channel='music')
    $ renpy.music.set_pause(True, channel='ambience')
    $ mcI.changeName()
    "Player" "My surname is:"
    $ mcI.changeSurname()

    if renpy.variant("pc"):
        if mcI.name != mcI.get("name_default"):
            $ mp_ndata.male_fname = mcI.name
        if mcI.sname != mcI.get("sname_default"):
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
            $ bffI.name_default = mp_ndata.malebff_fname
        if mp_ndata.malebff_sname != None:
            $ bffI.sname_default = mp_ndata.malebff_sname
    "[mc]'s [bffR.NPClabel] is called:"
    $ bffI.changeName()
    if renpy.variant("pc"):
        if bffI.name != bffI.name_default:
            $ mp_ndata.malebff_fname = bffI.name
        if bffI.sname != bffI.sname_default:
            $ mp_ndata.malebff_sname = bffI.sname
        $ mp_ndata.save()
    return
