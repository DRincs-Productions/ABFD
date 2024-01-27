# enviroment_mc_home
## bedroom_mc
image action bedroom_mc alarm: 
    "enviroment_mc_home/bedroom_mc/button/alarm.webp"
    alpha 0.01
image action bedroom_mc bed:
    "enviroment_mc_home/bedroom_mc/button/bed.webp"
    alpha 0.01
image action bedroom_mc katana:
    "enviroment_mc_home/bedroom_mc/button/katana.webp"
    alpha 0.01
image action bedroom_mc memo:
    "enviroment_mc_home/bedroom_mc/button/memo.webp"
    alpha 0.01
image action bedroom_mc pc:
    "enviroment_mc_home/bedroom_mc/button/pc.webp"
    alpha 0.01
image action bedroom_mc pc selected = "enviroment_mc_home/bedroom_mc/pc[tm.timeslot_number].webp"
image action bedroom_mc photo:
    "enviroment_mc_home/bedroom_mc/button/photo.webp"
    alpha 0.01
image action bedroom_mc poster:
    "enviroment_mc_home/bedroom_mc/button/poster.webp"
    alpha 0.01
image action bedroom_mc skateboard:
    "enviroment_mc_home/bedroom_mc/button/skateboard[skateboard_type].webp"
    alpha 0.01
image action bedroom_mc tengu_ronan:
    "enviroment_mc_home/bedroom_mc/button/tengu-ronan.webp"
    alpha 0.01
image action bedroom_mc tv:
    "enviroment_mc_home/bedroom_mc/button/tv.webp"
    alpha 0.01
image action bedroom_mc tv selected = "enviroment_mc_home/bedroom_mc/tv[tm.timeslot_number].webp"


# icon
# Action
image pre action alarm = Transform("/nqtr_interface/alarm.webp", xysize=(gui.sprite_size, gui.sprite_size))
image action icon alarm = LayeredImageMask("pre action alarm",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
image pre action pc = Transform("/nqtr_interface/pc.webp", xysize=(gui.sprite_size, gui.sprite_size))
image action icon pc = LayeredImageMask("pre action pc",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
