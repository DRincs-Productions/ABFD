init python:
    from pythonpackages.nqtr.navigation import Room
    from pythonpackages.nqtr.navigation import Location
    from pythonpackages.nqtr.navigation import Map

define city_name = "{b}Orlando{/b}"
define metro_name = "{b}Night City{/b}"
define ghetto_name = "{b}Grove City{/b}"
define peninsula_name = "{b}Wilson Beach{/b}"

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#room
define rooms = [
    Room(id="enviroment_mc_home attic", location_id="house", name=_("Soffitta"), button_icon="icon enviroment_mc_home attic", background="bg enviroment_mc_home attic"),
    Room(id="enviroment_mc_home bathroom", location_id="house", name=_("Bagno"), button_icon="icon enviroment_mc_home bathroom", background="bg enviroment_mc_home bathroom"),
    Room(id="enviroment_mc_home bedroom_emily", location_id="house", name=_("La stanza di [emilyI.name]"), button_icon="icon enviroment_mc_home bedroom_emily", background="bg enviroment_mc_home bedroom_emily"),
    Room(id="enviroment_mc_home bedroom_mc", location_id="house", name=_("La stanza di [mcI.name]"), button_icon="icon enviroment_mc_home bedroom_mc", background="bg enviroment_mc_home bedroom_mc"),
    Room(id="enviroment_mc_home bedroom_mia", location_id="house", name=_("La stanza di [miaI.name]"), button_icon="icon enviroment_mc_home bedroom_mia", background="bg enviroment_mc_home bedroom_mia"),
    Room(id="enviroment_mc_home bedroom_victoria", location_id="house", name=_("La stanza di [victoriaI.name]"), button_icon="icon enviroment_mc_home bedroom_victoria", background="bg enviroment_mc_home bedroom_victoria"),
    Room(id="enviroment_mc_home garage", location_id="house", name=_("Garage"), button_icon="icon enviroment_mc_home garage", background="bg enviroment_mc_home garage"),
    Room(id="enviroment_mc_home garden", location_id="house", name=_("Giardino"), button_icon="icon enviroment_mc_home garden", background="bg enviroment_mc_home garden"),
    Room(id="enviroment_mc_home kitchen", location_id="house", name=_("Cucina"), button_icon="icon enviroment_mc_home kitchen", background="bg enviroment_mc_home kitchen"),
    Room(id="enviroment_mc_home living_room", location_id="house", name=_("Sala"), button_icon="icon enviroment_mc_home living_room", background="bg enviroment_mc_home living_room"),
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#location
define locations = [
    Location(id = "house", map_id="map", external_room_id="bedroom_mc", name=_("Casa mia"), picture_in_background="icon map home", xalign=0.3, yalign=0.2),
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#map
define maps = {
    "map": Map(
        name = "[city_name]", background = "bg map",
        map_id_north = None,
        map_id_south = None,
        map_id_west = None,
        map_id_east = None,
    ),
}
