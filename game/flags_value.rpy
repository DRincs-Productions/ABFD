# Wiki: https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags
define flag_keys = [
    # Block all spend_time
    "not_can_spend_time",
    # which_contents_to_enable
    "lesbian_sharing_content",
    "lesbian_ntr_content",
    "sharing_content",
    "ntr_content",
    # Olther flags
    "goout",
    "weekend",
]

# Wiki: https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags#update_current_flags
label update_current_flags_custom:
    # Custom code
    if tm.is_weekend:
        $ set_flags("weekend", True)
    else:
        $ set_flags("weekend", False)
    return
