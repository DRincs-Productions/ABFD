# The script of the game goes in this file.

# The game starts here.

label start:
    # which_contents_to_enable
    $ set_flags('lesbian_sharing_content', True)
    $ set_flags('lesbian_ntr_content', True)
    $ set_flags('sharing_content', True)
    call screen which_contents_to_enable

    # The real start of the game

    return 
