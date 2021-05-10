image to_be_continued = "/coming_soon.webp"
define to_be_continued_path = "images/coming_soon.webp"

# Temporary end of the story (then play other stories)
label temporary_end_story:
    "This is the temporary end (current version: [config.version]). You'll have to wait new update."
    "If you want more updates, support me on {a=https://www.patreon.com/m/4135825}Patreon"
    return

# Temporary end of the game
label temporary_end_game:
    show to_be_continued
    show screen patreon_button
    call temporary_end_story
    $ old_version = config.version
    "Save the game now and not later."
    $ ShowMenu('save')()

    if (old_version == config.version):
        "Pressing ENTER will return to the Main Menu."
        $ renpy.run(MainMenu(confirm=False))
    hide to_be_continued
    hide screen patreon_button
    return

# Coming soon text
label coming_soon:
    "(Coming soon)"
    "Support me on {a=https://www.patreon.com/m/4135825}Patreon"
    return

screen patreon_button():
    add Frame(to_be_continued_path, xfill=True, yfill=True)
    vbox:
        anchor (1.0, 1.0)
        pos (0.999, 0.25) # setting both to 1.0 will put the all logos on the very edge
        xsize 455 # X patreon icon
        spacing 5
        imagebutton:
            idle Frame(patreon_idle, xfill=True, yfill=True)
            hover Frame(patreon_hover, xfill=True, yfill=True)
            action OpenURL("https://www.patreon.com/m/4135825")
            ysize 128 # Y patreon icon
            xalign 0.5
