default smartphone_porn = 1
default cur_porn = "A0"
default porn_artist = "Lexx228"
define smartphone01_path = "images/tools/Smartphone01.webp"
default smartphone01_porn_path = "images/tools/[porn_artist]/[cur_porn][smartphone_porn].webp"
default smartphone01_porn_icon_idle = "images/tools/Lexx228/00icon.webp"
default smartphone01_porn_icon_hover = im.MatrixColor("images/tools/Lexx228/00icon.webp", im.matrix.brightness(0.1))

default porn_icon_url = "https://www.patreon.com/m/4135825"
default smartphone01_path = "images/tools/Smartphone01.webp"

label sleep_fap01:
    # TODO: button to move cell phone
    $ smartphone_porn = 1
    show bg mc FAP01A 01
    show face mc FAP01A
    menu optional_name:
        mc "{i}Mhmm... Which one of these porns?"
        "Black on blonde":
            $ porn_artist = "SneakyBastard"
            $ cur_porn = "A0"
            $ smartphone01_porn_icon_idle = "images/tools/SneakyBastard/00icon.webp"
            $ smartphone01_porn_icon_hover = im.MatrixColor("images/tools/SneakyBastard/00icon.webp", im.matrix.brightness(0.1))
        "Milfing":
            $ porn_artist = "Lexx228"
            $ cur_porn = "A0"
            $ smartphone01_porn_icon_idle = "images/tools/Lexx228/00icon.webp"
            $ smartphone01_porn_icon_hover = im.MatrixColor("images/tools/Lexx228/00icon.webp", im.matrix.brightness(0.1))
        "MILFToon":
            $ porn_artist = "MILFToon"
            $ cur_porn = "A0"
            $ smartphone01_porn_icon_idle = "images/tools/MILFToon/00icon.webp"
            $ smartphone01_porn_icon_hover = im.MatrixColor("images/tools/MILFToon/00icon.webp", im.matrix.brightness(0.1))

    show screen smartphone01_porn
    window hide
    pause
    $ smartphone_porn = 2
    show bg mc FAP01A 02
    hide screen smartphone01_porn
    show screen smartphone01_porn
    window hide
    pause
    $ smartphone_porn = 3
    show bg mc FAP01A 03
    hide screen smartphone01_porn
    show screen smartphone01_porn
    window hide
    pause
    $ smartphone_porn = 4
    show bg mc FAP01A 04
    hide screen smartphone01_porn
    show screen smartphone01_porn
    window hide
    pause
    show bg mc FAP01A cum
    $ smartphone_porn = 5
    hide screen smartphone01_porn
    show screen smartphone01_porn
    window hide
    pause
    hide screen smartphone01_porn
    hide face
    window hide
    pause
    mc "{i}Oh, YES! Oh, shit!"
    return

screen smartphone01_porn():
    add Frame(smartphone01_porn_path, xfill=True, yfill=True)
    add Frame(smartphone01_path, xfill=True, yfill=True)
    imagebutton:
        pos (0.74, 0.5)
        idle Frame(smartphone01_porn_icon_idle, xfill=True, yfill=True)
        hover Frame(smartphone01_porn_icon_hover, xfill=True, yfill=True)
        action OpenURL(porn_icon_url)
        ysize 70
        xsize 70
