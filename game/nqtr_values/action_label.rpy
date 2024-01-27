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
