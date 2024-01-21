# maps
image bg map grove = "/interface/map/grove[convert_to_int(tm.timeslot_number/2)].webp"
image bg map night_city = "/interface/map/night_city.webp"
image bg map tampa_beach = "/interface/map/tampa_beach[convert_to_int(tm.timeslot_number/2)].webp"
image bg map tampa = "/interface/map/tampa[convert_to_int(tm.timeslot_number/2)].webp"

# rooms
## enviroment_mc_home
### attic
image bg enviroment_mc_home attic = "enviroment_mc_home/attic[tm.timeslot_number].webp"
image pre icon enviroment_mc_home attic = Transform("bg enviroment_mc_home attic", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon enviroment_mc_home attic = LayeredImageMask("pre icon enviroment_mc_home attic",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
### bathroom
image bg enviroment_mc_home bathroom = "enviroment_mc_home/bathroom[tm.timeslot_number].webp"
image pre icon enviroment_mc_home bathroom = Transform("bg enviroment_mc_home bathroom", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon enviroment_mc_home bathroom = LayeredImageMask("pre icon enviroment_mc_home bathroom",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
### bedroom_emily
image bg enviroment_mc_home bedroom_emily = "enviroment_mc_home/bedroom_emily[tm.timeslot_number].webp"
image pre icon enviroment_mc_home bedroom_emily = Transform("bg enviroment_mc_home bedroom_emily", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon enviroment_mc_home bedroom_emily = LayeredImageMask("pre icon enviroment_mc_home bedroom_emily",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
### bedroom_mc
image bg enviroment_mc_home bedroom_mc = "enviroment_mc_home/bedroom_mc[tm.timeslot_number].webp"
image pre icon enviroment_mc_home bedroom_mc = Transform("bg enviroment_mc_home bedroom_mc", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon enviroment_mc_home bedroom_mc = LayeredImageMask("pre icon enviroment_mc_home bedroom_mc",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
### bedroom_mia
image bg enviroment_mc_home bedroom_mia = "enviroment_mc_home/bedroom_mia[tm.timeslot_number].webp"
image pre icon enviroment_mc_home bedroom_mia = Transform("bg enviroment_mc_home bedroom_mia", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon enviroment_mc_home bedroom_mia = LayeredImageMask("pre icon enviroment_mc_home bedroom_mia",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
### bedroom_victoria
image bg enviroment_mc_home bedroom_victoria = "enviroment_mc_home/bedroom_victoria[tm.timeslot_number].webp"
image pre icon enviroment_mc_home bedroom_victoria = Transform("bg enviroment_mc_home bedroom_victoria", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon enviroment_mc_home bedroom_victoria = LayeredImageMask("pre icon enviroment_mc_home bedroom_victoria",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
### garage
image bg enviroment_mc_home garage = "enviroment_mc_home/garage[tm.timeslot_number].webp"
image pre icon enviroment_mc_home garage = Transform("bg enviroment_mc_home garage", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon enviroment_mc_home garage = LayeredImageMask("pre icon enviroment_mc_home garage",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
### garden
image bg enviroment_mc_home garden = "enviroment_mc_home/garden[tm.timeslot_number].webp"
image pre icon enviroment_mc_home garden = Transform("bg enviroment_mc_home garden", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon enviroment_mc_home garden = LayeredImageMask("pre icon enviroment_mc_home garden",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
### kitchen
image bg enviroment_mc_home kitchen = "enviroment_mc_home/kitchen[tm.timeslot_number].webp"
image pre icon enviroment_mc_home kitchen = Transform("bg enviroment_mc_home kitchen", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon enviroment_mc_home kitchen = LayeredImageMask("pre icon enviroment_mc_home kitchen",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
### living_room
image bg enviroment_mc_home living_room = "enviroment_mc_home/living_room[tm.timeslot_number].webp"
image pre icon enviroment_mc_home living_room = Transform("bg enviroment_mc_home living_room", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon enviroment_mc_home living_room = LayeredImageMask("pre icon enviroment_mc_home living_room",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
