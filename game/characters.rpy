# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -10 python:
    from pythonpackages.ds.character_info import CharacterInfo
    from pythonpackages.ds.character_type import GenderEnum

init -1:
    # Special
    define dv = Character(_("{b}Developer{/b}"),
        color = "#f3a837", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    # Main
    default mcI = CharacterInfo(
        name = "Liam", surname = "Johnson", age = 19, gender = GenderEnum.MALE,
        relationships = {
            john: "dad",
        },
    )
    define mc = Character("{b}[mcI.name]{/b}",
        icon = None,
        info_screen = "mc_character_info",
        color = "#37b3f3", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    define beaver = Character(_("{b}Il Castoro{/b}"),
        icon = None,
        color = "#d7f337", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
    default johnI = CharacterInfo(
        name = "John", surname = "Davis", age = 53, gender = GenderEnum.MALE,
        relationships = {
            mc: "son",
        },
    )
    define john = Character("{b}[johnI.name]{/b}",
        icon = None,
        info_screen = "mc_character_info",
        color = "#0058ff", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )
