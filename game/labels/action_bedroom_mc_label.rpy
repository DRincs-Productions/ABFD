menu nap:
    "Pisolino per 3 ore":
        call wait(3)
        return
    "Dormi":
        jump sleep
        return
    "Return":
        return

menu sleep:
    "A che ora voi impostare la sveglia?"
    "[tm.hour_of_new_day]:00":
        call new_day(is_check_event=True)
        return
    "7:00":
        call new_day(time_of_new_day = 7, is_check_event=True)
        return
    "9:00":
        call new_day(time_of_new_day = 9, is_check_event=True)
        return
    "Return":
        return

label allarm_info:
    show bg enviroment_mc_home bedroom_mc with dissolve:
        blur 7
    show alarm
    window hide
    pause
    if tm.timeslot_number == 0:
        mc "Sono le [tm.hour_of_new_day]:[tm.minute_of_new_hour] e sono pronto per iniziare la giornata!"
    elif tm.timeslot_number == 1:
        mc "Una sveglia posso impostarla per fare un pisolino."
    else:
        mc "Meglio impostarla prima di andare a dormire."

    hide alarm
    show bg enviroment_mc_home bedroom_mc with dissolve:
        blur 0
    return