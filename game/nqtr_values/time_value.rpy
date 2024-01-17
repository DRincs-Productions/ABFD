define timeslot_names = [
    (8, _("Mattina")),
    (14, _("Pomeriggio")),
    (19, _("Sera")),
    (22, _("Notte")),
]
define weekday_names = [
    "{#weekday}Monday",
    "{#weekday}Tuesday",
    "{#weekday}Wednesday",
    "{#weekday}Thursday",
    "{#weekday}Friday",
    "{#weekday}Saturday",
    "{#weekday}Sunday",
]
# ATTENTION here it is initialized
# when a save is loaded it is created with the updateTimeHandler() function
default tm = TimeHandler(
    hour_of_new_day = 5,
    hour = 14,
    weekday_weekend_begins = 6,
    day = 0,
    timeslot_names = timeslot_names,
    weekday_names = weekday_names
)
