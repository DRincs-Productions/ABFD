# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -10 python:
    from pythonpackages.ds.character_info import CharacterInfo
    from pythonpackages.ds.character_type import GenderEnum

init -1:
    define mister_text = _("Mr.")
    define missus_text = _("Mrs.")
    # https://drincs-website.web.app/wiki?route=Characters
    # Special
    define dv = Character(_("{b}Professore Oak{/b}"),
        color = "#f3a837", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    define unknown = Character(_("{b}Sconosciuto{/b}"),
        color = "#292929", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    # Family
    default mcI = CharacterInfo(
        name = "Liam", surname = "Johnson", age = 19, gender = GenderEnum.MALE,
        relationships = {
            john: "landlord",
            emily: "landlord",
            victoria: "housemate",
            arianna: "housemate",
            mia: "housemate",
        },
    )
    define mc = Character("{b}[mcI.name]{/b}",
        icon = None,
        color = "#37b3f3", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    define mc_think = Character("{b}[mcI.name]{/b}",
        icon = None,
        color = "#37b3f3", who_outlines = [(2,"#000000")], what_prefix = "( {i}", what_suffix = "{/i} )", what_outlines = [(2,"#000000")]
    )
    # Housemates
    default johnI = CharacterInfo(
        name = "John", surname = "Davis", age = 53, gender = GenderEnum.MALE,
        relationships = {
            mc: "tenant",
            emily: "wife",
            victoria: "tenant",
            arianna: "tenant",
            mia: "tenant",
        },
    )
    define john = Character("{b}[johnI.name]{/b}",
        icon = None,
        color = "#0058ff", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    default emilyI = CharacterInfo(
        name = "Emily", surname = "Caruso", age = 49, gender = GenderEnum.FEMALE,
        relationships = {
            mc: "tenant",
            john: "husband",
            victoria: "tenant",
            arianna: "tenant",
            mia: "tenant",
        },
    )
    define emily = Character("{b}[emilyI.name]{/b}",
        icon = None,
        color = "#8a0086", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    default victoriaI = CharacterInfo(
        name = "Victoria", surname = "[johnI.surname]", age = (mcI.age+4), gender = GenderEnum.FEMALE,
        relationships = {
            mc: "housemate",
            john: "landlord",
            emily: "landlord",
            arianna: "housemate",
            mia: "housemate",
        },
    )
    define victoria = Character("{b}[victoriaI.name]{/b}",
        icon = None,
        color = "#8000d0", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    default ariannaI = CharacterInfo(
        name = "Arianna", surname = "[johnI.surname]", age = (mcI.age), gender = GenderEnum.FEMALE,
        relationships = {
            mc: "housemate",
            john: "landlord",
            emily: "landlord",
            victoria: "housemate",
            mia: "housemate",
        },
    )
    define arianna = Character("{b}[ariannaI.name]{/b}",
        icon = None,
        color = "#a800a3", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    default miaI = CharacterInfo(
        name = "Mia", surname = "[johnI.surname]", age = (mcI.age-1), gender = GenderEnum.FEMALE,
        relationships = {
            mc: "housemate",
            john: "landlord",
            emily: "landlord",
            victoria: "housemate",
            arianna: "housemate",
        },
    )
    define mia = Character("{b}[miaI.name]{/b}",
        icon = None,
        color = "#d600d0", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    # Family Friends
    default erikI = CharacterInfo(
        name = "Erik", surname = "Johnson", age = (mcI.age), gender = GenderEnum.MALE,
        relationships = {
            tammy : "mom",
            natalia : "sister",
        },
    )
    define erik = Character("{b}[erikI.name]{/b}",
        icon = None,
        color = "#00d62e", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    define erik_dad = mister_text + " Johnson"
    default tammyI = CharacterInfo(
        name = "Tammy", surname = "Bouvier", age = 51, gender = GenderEnum.FEMALE,
        relationships = {
            erik : "son",
            natalia : "daughter",
        },
    )
    define tammy = Character("{b}[tammyI.name]{/b}",
        icon = None,
        color = "#ad2727", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    define tammy_think = Character("{b}[tammyI.name]{/b}",
        icon = None,
        color = "#ad2727", who_outlines = [(2,"#000000")], what_prefix = "( {i}", what_suffix = "{/i} )", what_outlines = [(2,"#000000")]
    )
    default nataliaI = CharacterInfo(
        name = "Natalia", surname = "Johnson", age = (erikI.age+2), gender = GenderEnum.FEMALE,
        relationships = {
            erik : "brother",
            tammy : "mom",
        },
    )
    define natalia = Character("{b}[tammyI.name]{/b}",
        icon = None,
        color = "#b84776", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )

    # Cops and thugs
    define beaver = Character(_("{b}Il Castoro{/b}"),
        icon = None,
        color = "#d7f337", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
