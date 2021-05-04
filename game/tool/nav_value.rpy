define rooms = [
        Room(id="mc_room", id_location="house", name=_("[mc] room"), icon="icon mcroom", bg="bg mcroom", id_actions = ["sleep","nap",]), 
        Room(id="mia_room", id_location="house", name=_("[mia] room"), icon="icon miaroom", bg="bg miaroom"), 
        Room(id="livingroom", id_location="house", name=_("Lounge"), icon="icon livingroom", bg="bg livingroom"), 
    ]

define locations = {
        "house"     :   Location(id = "house", key_map="map", id_externalroom="terrace", name=_("MC house"), icon="icon map home", xalign=0.3, yalign=0.2), 
    }

define map_images = {
        "map"       :   "bg map",
    }

define ch_icons = {
        "emy"       :   "icon/Emily.webp",
        "mia"       :   "icon/Mia.webp",
        "vct"       :   "icon/Victoria.webp",
    }

default cur_room = rooms[0]
default cur_location = locations[cur_room.id_location]
# Variable to check the map screen: if it is True then the player is viewing the map.
default map_looking = False
