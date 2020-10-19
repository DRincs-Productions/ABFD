# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# MC's family
default mcI = Information("Liam", "Brown", 19, True, rel.single, "", mcStry)
define mc = Character("{b}[mcI.name]{/b}", color="#09f")
default jnI = Information("John", mcI.sname, 47, True, rel.married, emy, jnStry)
define jn = Character("{b}[jnI.name]{/b}", color="#0058ff")
default jnR = Relationship("landlord", "leaseholder", True)
default for_jnR = Relationship("leaseholder", "landlord", True)
default emyI = Information("Emily", "Bernard", 43, True, rel.married, jn, emyStry)
define emy = Character("{b}[emyI.name]{/b}", color="#8a0086")
default emyR = Relationship("landlord", "leaseholder", True)
default for_emyR = Relationship("leaseholder", "landlord", True)
default vctI = Information("Victoria", jnI.sname, (mcI.age+4), True, rel.single, "", vctStry)
define vct = Character("{b}[vctI.name]{/b}", color="#a800a3")
default vctR = Relationship("housemate", "housemate", True)
default vctN = Relationship("housemate", "Little bastard", True)
default miaI = Information("Mia", jnI.sname, (mcI.age-1), True, rel.single, "", miaStry)
define mia = Character("{b}[miaI.name]{/b}", color="#d600d0")
default miaR = Relationship(vctR.NPClabel, vctR.NPClabel, True)
default arnI = Information("Arianna", jnI.sname, mcI.age, True, rel.single, "", arnStry)
define arn = Character("{b}[arnI.name]{/b}", color="#8000d0")
default arnR = Relationship(vctR.NPClabel, vctR.NPClabel, True)
# Friend's family
default bbfI = Information("Erik", "Johnson", mcI.age, True, rel.single, "", bbfStry)
define bbf = Character("{b}[bbfI.name]{/b}", color="#19bb2c")
default bbfR = Relationship("best friend", "best friend", True)
# Friend's family
default tamI = Information("Tammy", "Johnson", mcI.age, True, rel.widow, "", bbfStry)
define tam = Character("{b}Mrs. [bbfI.name]{/b}", who_color="#19bb2c")

# The game starts here.

label start:

    stop music fadeout 1.0
    call screen check_age
    "Welcome to [config.name]"

    call intro

    return
