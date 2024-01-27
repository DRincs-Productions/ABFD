init python:
    from pythonpackages.nqtr.action import Act

default poster_type = "A"
default skateboard_type = "A"

# habitual actions
# dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Action#add-an-action-in-dictionary
define df_actions = {
    "bedroom_mc alarm" : Act(name = _("Svieglia"), picture_in_background = "action bedroom_mc alarm", label_name = "nap"),
    "bedroom_mc nap" : Act(name = _("Pisolino"), button_icon = "action icon alarm", picture_in_background = "action bedroom_mc bed", label_name = "nap", hour_start = 5, hour_stop = 23),
    "bedroom_mc sleep" : Act(name = _("Dormi"), button_icon = "action icon sleep", picture_in_background = "action bedroom_mc bed", label_name = "sleep", hour_start = 23, hour_stop = 5),
    "bedroom_mc katana" : Act(name = _("Katana"), picture_in_background = "action bedroom_mc katana", label_name = "nap"),
    "bedroom_mc memo" : Act(name = _("Appunti"), picture_in_background = "action bedroom_mc memo", label_name = "nap"),
    "bedroom_mc pc" : Act(name = _("PC"), button_icon = "action icon pc", picture_in_background = "action bedroom_mc pc", picture_in_background_selected = "action bedroom_mc pc selected", label_name = "nap"),
    "bedroom_mc photo" : Act(name = _("Foto"), picture_in_background = "action bedroom_mc photo", label_name = "nap"),
    "bedroom_mc poster" : Act(name = _("Poster"), picture_in_background = "action bedroom_mc poster", label_name = "nap"),
    "bedroom_mc skateboard" : Act(name = _("Skateboard"), picture_in_background = "action bedroom_mc skateboard", label_name = "nap"),
    "bedroom_mc tengu_ronam" : Act(name = "Tengu Ronam", picture_in_background = "action bedroom_mc tengu_ronan", label_name = "nap"),
    "bedroom_mc tv" : Act(name = _("TV"), picture_in_background = "action bedroom_mc tv", picture_in_background_selected = "action bedroom_mc tv selected", label_name = "nap"),
}
