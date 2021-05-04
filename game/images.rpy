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
