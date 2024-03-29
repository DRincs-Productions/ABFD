# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -10 python:
    from pythonpackages.ds.character_info import CharacterInfo
    from pythonpackages.ds.character_type import GenderEnum

init -1:
    # https://drincs-website.web.app/wiki?route=Characters
    # Special
    define dv = Character(_("{b}Developer{/b}"),
        color = "#f3a837", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    # Family
    default mcI = CharacterInfo(
        name = "Liam", surname = "Johnson", age = 19, gender = GenderEnum.MALE,
        relationships = {
            john: "dad",
            emily: "mom",
            victoria: "sister",
            arianna: "sister",
            mia: "sister",
        },
    )
    define mc = Character("{b}[mcI.name]{/b}",
        icon = None,
        color = "#37b3f3", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    # Housemates
    default johnI = CharacterInfo(
        name = "John", surname = "Davis", age = 53, gender = GenderEnum.MALE,
        relationships = {
            mc: "son",
            emily: "wife",
            victoria: "daughter",
            arianna: "daughter",
            mia: "daughter",
        },
    )
    define john = Character("{b}[johnI.name]{/b}",
        icon = None,
        color = "#0058ff", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    default emilyI = CharacterInfo(
        name = "Emily", surname = "Caruso", age = 49, gender = GenderEnum.FEMALE,
        relationships = {
            mc: "son",
            john: "husband",
            victoria: "daughter",
            arianna: "daughter",
            mia: "daughter",
        },
    )
    define emily = Character("{b}[emilyI.name]{/b}",
        icon = None,
        color = "#8a0086", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    default victoriaI = CharacterInfo(
        name = "Victoria", surname = "[johnI.surname]", age = (mcI.age+4), gender = GenderEnum.FEMALE,
        relationships = {
            mc: "brother",
            john: "dad",
            emily: "mom",
            arianna: "sister",
            mia: "sister",
        },
    )
    define victoria = Character("{b}[victoriaI.name]{/b}",
        icon = None,
        color = "#8000d0", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    default ariannaI = CharacterInfo(
        name = "Arianna", surname = "[johnI.surname]", age = (mcI.age), gender = GenderEnum.FEMALE,
        relationships = {
            mc: "brother",
            john: "dad",
            emily: "mom",
            victoria: "sister",
            mia: "sister",
        },
    )
    define arianna = Character("{b}[ariannaI.name]{/b}",
        icon = None,
        color = "#a800a3", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    default miaI = CharacterInfo(
        name = "Mia", surname = "[johnI.surname]", age = (mcI.age-1), gender = GenderEnum.FEMALE,
        relationships = {
            mc: "brother",
            john: "dad",
            emily: "mom",
            victoria: "sister",
            arianna: "sister",
        },
    )
    define mia = Character("{b}[miaI.name]{/b}",
        icon = None,
        color = "#d600d0", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    # Cops and thugs
    define beaver = Character(_("{b}Il Castoro{/b}"),
        icon = None,
        color = "#d7f337", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
