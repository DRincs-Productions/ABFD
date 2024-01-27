init python:
    from pythonpackages.nqtr.navigation import Room
    from pythonpackages.nqtr.navigation import Location
    from pythonpackages.nqtr.navigation import Map

define city_name = "{b}Tampa{/b}"
define metro_name = "{b}Night City{/b}"
define ghetto_name = "{b}Grove City{/b}"
define peninsula_name = "{b}Tampa Beach{/b}"

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#room
define rooms = [
    Room(id="enviroment_mc_home attic", location_id="house", name=_("Soffitta"), button_icon="icon enviroment_mc_home attic", background="bg enviroment_mc_home attic"),
    Room(id="enviroment_mc_home bathroom", location_id="house", name=_("Bagno"), button_icon="icon enviroment_mc_home bathroom", background="bg enviroment_mc_home bathroom"),
    Room(id="enviroment_mc_home bedroom_emily", location_id="house", name=_("La stanza di [emilyI.name]"), button_icon="icon enviroment_mc_home bedroom_emily", background="bg enviroment_mc_home bedroom_emily"),
    Room(id="enviroment_mc_home bedroom_mc", location_id="house", name=_("La stanza di [mcI.name]"), button_icon="icon enviroment_mc_home bedroom_mc", background="bg enviroment_mc_home bedroom_mc",
        action_ids = ["bedroom_mc alarm", "bedroom_mc nap", "bedroom_mc sleep", "bedroom_mc katana", "bedroom_mc memo", "bedroom_mc pc", "bedroom_mc photo", "bedroom_mc poster", "bedroom_mc skateboard", "bedroom_mc tengu_ronam", "bedroom_mc tv"]
    ),
    Room(id="enviroment_mc_home bedroom_mia", location_id="house", name=_("La stanza di [miaI.name]"), button_icon="icon enviroment_mc_home bedroom_mia", background="bg enviroment_mc_home bedroom_mia"),
    Room(id="enviroment_mc_home bedroom_victoria", location_id="house", name=_("La stanza di [victoriaI.name]"), button_icon="icon enviroment_mc_home bedroom_victoria", background="bg enviroment_mc_home bedroom_victoria"),
    Room(id="enviroment_mc_home garage", location_id="house", name=_("Garage"), button_icon="icon enviroment_mc_home garage", background="bg enviroment_mc_home garage"),
    Room(id="enviroment_mc_home garden", location_id="house", name=_("Giardino"), button_icon="icon enviroment_mc_home garden", background="bg enviroment_mc_home garden"),
    Room(id="enviroment_mc_home kitchen", location_id="house", name=_("Cucina"), button_icon="icon enviroment_mc_home kitchen", background="bg enviroment_mc_home kitchen"),
    Room(id="enviroment_mc_home living_room", location_id="house", name=_("Sala"), button_icon="icon enviroment_mc_home living_room", background="bg enviroment_mc_home living_room"),
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#location
define locations = [
    Location(id = "house", map_id="map", external_room_id="enviroment_mc_home living_room", name=_("Casa mia"), picture_in_background="icon map home", xalign=0.3, yalign=0.2),
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#map
define maps = {
    "map": Map(
        name = "[city_name]", background = "bg map grove",
        map_id_north = None,
        map_id_south = None,
        map_id_west = None,
        map_id_east = None,
    ),
    "night_city": Map(
        name = "[metro_name]", background = "bg map night_city",
        map_id_north = None,
        map_id_south = None,
        map_id_west = None,
        map_id_east = None,
    ),
    "tampa_beach": Map(
        name = "[peninsula_name]", background = "bg map tampa_beach",
        map_id_north = None,
        map_id_south = None,
        map_id_west = None,
        map_id_east = None,
    ),
    "grove": Map(
        name = "[ghetto_name]", background = "bg map grove",
        map_id_north = None,
        map_id_south = None,
        map_id_west = None,
        map_id_east = None,
    ),
}
