# Tool
image arrow = "/arrow.webp"
## Photo
# Family
image photo family 01 = "/family/photo01.webp"
image photo family 02 = "/family/photo02.webp"
## Profile
# Family
image profile mc 01 = "/MC/profile01.webp"
image profile mc 01 pause = "/MC/profile01-pause.webp"
image profile jn 01 = "/John/profile01.webp"
image profile arn 01 = "/Arianna/profile01.webp"
image profile vct 01 = "/Victoria/profile01.webp"
image profile mia 01 = "/Mia/profile01.webp"
image profile emy 01 = "/Emily/profile01.webp"

## Icon
# location
image icon mcroom = "location/mcroom-icon.webp"
image icon miaroom = "location/miaroom-icon.webp"
image icon livingroom = "location/livingroom-icon.webp"
# ---
image icon mcroom a = im.MatrixColor("location/mcroom-icon.webp", im.matrix.brightness(-0.5))
image icon miaroom a = im.MatrixColor("location/miaroom-icon.webp", im.matrix.brightness(-0.5))
image icon livingroom a = im.MatrixColor("location/livingroom-icon.webp", im.matrix.brightness(-0.5))
# map
image icon map home = "/interface/map-home.webp"
image icon map home a = im.MatrixColor("/interface/map-home.webp", im.matrix.brightness(-0.5))

## Background
# map
image bg map = "location/map-[tm.image_time].webp"
# door
image bg door = "location/door.webp"
image bg door open = "location/door-open.webp"
# location
image bg mcroom = "location/mcroom-[tm.image_time].webp"
image bg miaroom = "location/miaroom-[tm.image_time].webp"
image bg livingroom = "location/livingroom-[tm.image_time].webp"
image bg livingroom victoria drunk = Composite( (gui.width, gui.height),
    (0, 0), "/location/livingroom-2.webp",
    (0, 0), "/location/livingroom-2-victoriadrunk.webp")

## Effect
define blink_transition = ImageDissolve("location/door.webp", 0.2, ramplen=128)
define blink_reverse = ImageDissolve("location/door.webp", 0.2, reverse=True, ramplen=128)

## Emily
image bg emily kitchen talk = Composite( (gui.width, gui.height),
    (0, 0), "/Emily/kitchen/talk.webp",
    (0, 0), "check:/Emily/kitchen/talk[mc_dress_home].webp")

## MC
# FAP01A
image bg mc FAP01A dick00 = "MC/sleep/FAP01A.webp"
image bg mc FAP01A dick01 = Composite( (gui.width, gui.height),
    (0, 0), "/MC/sleep/FAP01A.webp",
    (0, 0), "/MC/sleep/FAP01A-dick01.webp")
image bg mc FAP01A dick02 = Composite( (gui.width, gui.height),
    (0, 0), "/MC/sleep/FAP01A.webp",
    (0, 0), "/MC/sleep/FAP01A-dick02.webp")
image bg mc FAP01A 01:
    "bg mc FAP01A dick00"
    pause 0.25
    "bg mc FAP01A dick01"
    pause 0.25
    "bg mc FAP01A dick02"
    pause 0.5
    "bg mc FAP01A dick01"
    pause 0.5
    "bg mc FAP01A dick02"
    pause 0.5
    "bg mc FAP01A dick01"
    pause 0.25
    repeat
image bg mc FAP01A 02:
    "bg mc FAP01A dick02"
    pause 0.4
    "bg mc FAP01A dick01"
    pause 0.3
    "bg mc FAP01A dick00"
    pause 0.3
    "bg mc FAP01A dick01"
    pause 0.3
    "bg mc FAP01A dick00"
    pause 0.3
    "bg mc FAP01A dick01"
    pause 0.3
    "bg mc FAP01A dick00"
    pause 0.25
    "bg mc FAP01A dick01"
    pause 0.25
    "bg mc FAP01A dick00"
    pause 0.25
    "bg mc FAP01A dick01"
    pause 0.25
    "bg mc FAP01A dick00"
    pause 0.25
    "bg mc FAP01A dick01"
    pause 0.05
    repeat
image bg mc FAP01A 03:
    "bg mc FAP01A dick02"
    pause 0.3
    "bg mc FAP01A dick01"
    pause 0.3
    repeat
image bg mc FAP01A 04:
    "bg mc FAP01A dick02"
    pause 0.2
    "bg mc FAP01A dick01"
    pause 0.2
    repeat
image bg mc FAP01A cum = "MC/sleep/FAP01B.webp"
image face mc FAP01A:
    "/intro/c.webp"
    pause 6
    "/MC/sleep/FAP01A-face01.webp"
    pause 6
    "/MC/sleep/FAP01A-face02.webp"
    pause 6
    repeat
# Sleep
image bg mc sleep sl01A = "MC/sleep/sl01A.webp"
image bg mc sleep sl01B = "MC/sleep/sl01B.webp"
image bg mc sleep sl02  = "MC/sleep/sl02.webp"

## Tools
# Smartphone
image tools smartphone 01   = "/tools/Smartphone01.webp"

## Porn
# Smartphone
image porn Lexx228 A        = "/MC/Lexx228/A0[smartphone_porn].webp"
image porn MILFToon A       = "/MC/MILFToon/A0[smartphone_porn].webp"
image porn SneakyBastard A  = "/MC/SneakyBastard/A0[smartphone_porn].webp"
image icon Lexx228 A        = "/MC/Lexx228/00icon.webp"
image icon MILFToon A       = "/MC/MILFToon/00icon.webp"
image icon SneakyBastard A  = "/MC/SneakyBastard/00icon.webp"
