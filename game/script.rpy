# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:

    stop music fadeout 1.0
    call screen check_age
    "Welcome to [config.name]"

    return
