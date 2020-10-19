define NTR = True

label NTR_enabler:
    "Do you want to enable {b}NTR{/b}?"
    menu:
        "Yes":
            $ NTR = True
            "Okay, NTR has been enabled."
        "No":
            $ NTR = False
            "Ok, you will no longer see references to NTR."
        "Remember: You can enable/disable it from your pc."
    return
