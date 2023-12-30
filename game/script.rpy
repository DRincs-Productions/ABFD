# The script of the game goes in this file.

# The game starts here.

label start:
    # which_contents_to_enable
    $ set_flags('lesbian_sharing_content', True)
    $ set_flags('lesbian_ntr_content', True)
    $ set_flags('sharing_content', True)

    dv "Ehi giocatore."
    dv "Non mi piace!"
    dv "Forse dovrei darti un nome..."
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

    call intro

    # The real start of the game

    return 
