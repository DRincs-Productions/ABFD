# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# MC's family
default mcI = Information(name = "Liam", sname = "Brown", age = 19, active = True, rel_status = rel.get('single'))
define mc = Character("{b}[mcI.name]{/b}", color="#09f")
default jnI = Information(name = "John", sname = mcI.sname, age = 47, active = True, rel_status = rel.get('married'), rel_partner = emy)
define jn = Character("{b}[jnI.name]{/b}", color="#0058ff")
default jnR = Relationship("landlord", "leaseholder", True)
default for_jnR = Relationship("leaseholder", "landlord", True)
default emyI = Information(name = "Emily", sname = "Bernard", age = 43, active = True, rel_status = rel.get('married'), rel_partner = jn)
define emy = Character("{b}[emyI.name]{/b}", color="#8a0086")
default emyR = Relationship("landlord", "leaseholder", True)
default for_emyR = Relationship("leaseholder", "landlord", True)
default vctI = Information(name = "Victoria", sname = jnI.sname, age = (mcI.age+4), active = True, rel_status = rel.get('single'))
define vct = Character("{b}[vctI.name]{/b}", color="#a800a3")
default vctR = Relationship("housemate", "housemate", True)
default vctN = Relationship("housemate", "Little bastard", True)
default miaI = Information(name = "Mia", sname = jnI.sname, age = (mcI.age-1), active = True, rel_status = rel.get('single'))
define mia = Character("{b}[miaI.name]{/b}", color="#d600d0")
default miaR = Relationship(vctR.NPClabel, vctR.NPClabel, True)
default arnI = Information(name = "Arianna", sname = jnI.sname, age = mcI.age, active = True, rel_status = rel.get('single'))
define arn = Character("{b}[arnI.name]{/b}", color="#8000d0")
default arnR = Relationship(vctR.NPClabel, vctR.NPClabel, True)
# Friend's family
default bffI = Information(name = "Erik", sname = "Johnson", age = mcI.age, active = True, rel_status = rel.get('single'))
define bff = Character("{b}[bffI.name]{/b}", color="#19bb2c")
default bffR = Relationship("best friend", "best friend", True)
# Friend's family
default tamI = Information(name = "Tammy", sname = "Johnson", age = (emyI.age-2), active = True, rel_status = rel.get('widow'), rel_partner = mrJohnson)
define tam = Character("{b}Mrs. [tamI.name]{/b}", who_color="#bf5fec")
# TV
default kstI = Information(name = "Kirstin", sname = "O'Connor", age = (emyI.age), active = True, rel_status = rel.get('single'))
define kst = Character("{b}[kstI.name]{/b}", who_color="#bf5fec")

## Functions for discord
# https://arianeb.com/2019/07/19/adding-discord-rich-presence-to-renpy-games/
init -20 python:
    if renpy.variant("pc"):
        import discord_rpc
        import time

        def readyCallback(current_user):
            print('Our user: {}'.format(current_user))

        def disconnectedCallback(codeno, codemsg):
            print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
                codeno, codemsg
            ))

        def errorCallback(errno, errmsg):
            print('An error occurred! Error {}: {}'.format(
                errno, errmsg
            ))

label before_main_menu:
    if renpy.variant("pc"):
        python:
            # Note: 'event_name': callback
            callbacks = {
                'ready': readyCallback,
                'disconnected': disconnectedCallback,
                'error': errorCallback,
            }
            discord_rpc.initialize('807939960769609798', callbacks=callbacks, log=False)
            start = time.time()
            print(start)
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()
            discord_rpc.update_presence(
                **{
                    'details': 'Main Menu',
                    'start_timestamp': start,
                    'large_image_key': 'ABFD'
                }
            )
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()

    return
## END Functions for discord


# The game starts here.

label start:
    ## Adding Discord Rich
    if renpy.variant("pc"):
        python:
            callbacks = {
                'ready': readyCallback,
                'disconnected': disconnectedCallback,
                'error': errorCallback,
            }
            discord_rpc.initialize('807939960769609798', callbacks=callbacks, log=False)
            start = time.time()
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()
            discord_rpc.update_presence(
                **{
                    'details': 'At College',
                    'state': 'Lecture Hall',
                    'large_image_key': 'ABFD',
                    'start_timestamp': start
                }
            )

            discord_rpc.update_connection()
            discord_rpc.run_callbacks()

    # The real start of the game
    call screen check_age
    "Welcome to [config.name]"
    call NTR_enabler

    call stats_default_family
    call stats_default_bfffamily

    call intro

    $ cur_room = rooms[0]
    $ cur_location = locations[cur_room.id_location]
    $ prev_room = rooms[0]
    $ updateBL()
    $ bl_values["block_spendtime"] = True

    ## call screen room_navigation
    call after_wait

    return
