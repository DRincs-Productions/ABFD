﻿# The script of the game goes in this file.

# The game starts here.

label start:
    # enable a notify screen
    call enable_notifyEx

    # which_contents_to_enable
    $ set_flags('lesbian_sharing_content', True)
    $ set_flags('lesbian_ntr_content', True)
    $ set_flags('sharing_content', True)

    dv "Ehi giocatore."
    dv "Non mi piace!"
    dv "Forse dovrei darti un nome..."
    show bg profiles mc cartoon with dissolve
    call renaming_mc(mcI)
    dv "Benvenuto in [config.name]"
    dv "Ma prima di iniziare..."
    mc "La mia età è:"
    call set_valid_age(mcI)
    if mcI.is_adult:
        dv "Sembri abbastanza grande per giocare a questo gioco."
        dv "Quindi, iniziamo!"
    else:
        dv "Sembri troppo giovane per giocare a questo gioco."
        dv "Torna quando sarai maggiorenne."
        return
    call screen which_contents_to_enable
    pause
    show bg profiles mc with dissolve
    call intro

    # The real start of the game
    $ block_goout_dialogue = _("To get out you have to take the car keys, (talk to Alice)")

    call change_room(room_id = "enviroment_mc_home bedroom_mc")
    $ prev_room = rooms[0]

    # the first time it opens room navigation screen use after_spending_time
    # for update routine, event...
    call after_spending_time
    # open the room navigation screen
    call screen room_navigation

    return 
