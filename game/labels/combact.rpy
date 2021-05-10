image bg miaroom combact = "/combact/background/miaroom.webp"

## MC
image mc normal joking 01 = "/combact/MC Normal Joking 01.webp"
# attack
image mc funny face 01:
    "/combact/MC funny face 01.webp"
    pause 0.50
    "mc normal joking 01"
image mc mia laughter cushion 01:
    "/combact/Mia Laughter Cushion 01 MC.webp"
    pause 0.25
    "/combact/Mia Laughter Cushion 02 MC.webp"
    pause 0.25
    "mc normal joking 01"
# loses
image mc loses left 01:
    "mc normal joking 01"
    pause 0.25
    "/combact/MC loses left 01.webp"
    pause 0.25
    "mc normal joking 01"
image mc loses left dying 01 = "/combact/MC loses left dying 01.webp"
image mc loses right 01:
    "mc normal joking 01"
    pause 0.25
    "/combact/MC loses right 01.webp"
    pause 0.25
    "mc normal joking 01"

## Mia
image mia normal = "/combact/Mia Normal Pillow 01.webp"
# attack
image mia attack cushion left 01:
    "/combact/Mia attack Cushion left A 01.webp"
    pause 0.25
    "/combact/Mia attack Cushion left B 01.webp"
    pause 0.25
    "mia normal"
image mia attack cushion right 01:
    "/combact/Mia attack Cushion right A 01.webp"
    pause 0.25
    "/combact/Mia attack Cushion right B 01.webp"
    pause 0.25
    "mia normal"
image mia final attack cushion left 01 = "/combact/Mia final attack Cushion left A 01.webp"
# loses
image mia laughter cushion 01:
    "/combact/Mia Laughter Cushion 01.webp"
    pause 0.25
    "/combact/Mia Laughter Cushion 02.webp"
    pause 0.25
    "mia normal"

label combact_mia_intro:
    $ mia_fun = 0

    show bg miaroom combact
label combact_mia_intro_part2:
    show mia normal
    show mc normal joking 01
    menu:
        mc "{i}Hmmm...what could I do to her:"
        "Funny face":
            hide mc
            hide mia
            $ mia_fun += 10
            show mc funny face 01
            show mia laughter cushion 01
        "Lethal Tickling":
            hide mc
            hide mia
            $ mia_fun += 20
            show mia laughter cushion 01
            show mc mia laughter cushion 01
    window hide
    pause
    if mia_fun > 90:
        show mia final attack cushion left 01
        show mc loses left dying 01
        window hide
        pause
        $ del mia_fun
        hide mia
        hide mc
        return
    hide mc
    hide mia
    $ val = renpy.random.randint(1, 2)
    if (val == 1):
        show mia attack cushion left 01
        show mc loses left 01
    else:
        show mc loses right 01
        show mia attack cushion right 01
    window hide
    pause
    "[mia]'s Happiness: [mia_fun]"
    hide mc
    hide mia
    jump combact_mia_intro_part2
