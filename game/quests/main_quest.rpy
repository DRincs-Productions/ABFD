image quest main = "/intro/C01.webp"

label main_startstage:
    $ updateQuestsLevels()
    if (quests_levels["main"] == 0):
        $ quests_descriptions["main"] = _("[jn] walked away leaving us alone. In the postit that he left there was written that he has to solve some problems, but which ones? Apart from that I don't know much else, [emy] on the other hand seems to know what he was talking about or rather she doesn't ask too many questions as if she already has an idea about the answers. \nI just hope that the problems will not come looking for us.")
        $ sp_routine["introD"] = Commitment(chs={"mia" : TalkObject()}, tm_start=17, tm_stop=19, id_location="house", id_room="mia_room", label_event="introD")
    return
