init python:
    from pythonpackages.nqtr.action import Act

default poster_type = "A"
default skateboard_type = "A"

# habitual actions
# dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Action#add-an-action-in-dictionary
define df_actions = {
    "bedroom_mc alarm" : Act(name = _("Svieglia"),  picture_in_background = "action bedroom_mc alarm", label_name = "nap"),
    "bedroom_mc sleep" : Act(name = _("Dormi"),  picture_in_background = "action bedroom_mc bed", label_name = "nap"),
    "bedroom_mc katana" : Act(name = _("Katana"),  picture_in_background = "action bedroom_mc katana", label_name = "nap"),
    "bedroom_mc memo" : Act(name = _("Appunti"),  picture_in_background = "action bedroom_mc memo", label_name = "nap"),
    "bedroom_mc pc" : Act(name = _("PC"),  picture_in_background = "action bedroom_mc pc", label_name = "nap"),
    "bedroom_mc photo" : Act(name = _("Foto"),  picture_in_background = "action bedroom_mc photo", label_name = "nap"),
    "bedroom_mc poster" : Act(name = _("Poster"),  picture_in_background = "action bedroom_mc poster", label_name = "nap"),
    "bedroom_mc skateboard" : Act(name = _("Skateboard"),  picture_in_background = "action bedroom_mc skateboard", label_name = "nap"),
    "bedroom_mc tengu_ronam" : Act(name = "Tengu Ronam",  picture_in_background = "action bedroom_mc tengu_ronan", label_name = "nap"),
    "bedroom_mc tv" : Act(name = _("TV"),  picture_in_background = "action bedroom_mc tv", label_name = "nap"),
}
