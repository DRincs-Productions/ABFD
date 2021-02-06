# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# MC's family
default mcI = Information(name = "Liam", sname = "Brown", age = 19, active = True, rel_status = rel.get('single'))
define mc = Character("{b}[mcI.name]{/b}", color="#09f")
default jnI = Information(name = "John", sname = mcI.sname, age = 47, active = True, rel_status = rel.get('married'), rel_partner = emy)
define jn = Character("{b}[jnI.name]{/b}", color="#0058ff")
default jnR = Relationship("landlord", "leaseholder", True)
default for_jnR = Relationship("leaseholder", "landlord", True)
default emyI = Information(name = "Emily", sname = "Bernard", age = 43, active = True, rel_status = rel.get('married'), rel_partner = jn)
define emy = Character("{b}[emyI.name]{/b}", color="#8a0086")
default emyR = Relationship("landlord", "leaseholder", True)
default for_emyR = Relationship("leaseholder", "landlord", True)
default vctI = Information(name = "Victoria", sname = jnI.sname, age = (mcI.age+4), active = True, rel_status = rel.get('single'))
define vct = Character("{b}[vctI.name]{/b}", color="#a800a3")
default vctR = Relationship("housemate", "housemate", True)
default vctN = Relationship("housemate", "Little bastard", True)
default miaI = Information(name = "Mia", sname = jnI.sname, age = (mcI.age-1), active = True, rel_status = rel.get('single'))
define mia = Character("{b}[miaI.name]{/b}", color="#d600d0")
default miaR = Relationship(vctR.NPClabel, vctR.NPClabel, True)
default arnI = Information(name = "Arianna", sname = jnI.sname, age = mcI.age, active = True, rel_status = rel.get('single'))
define arn = Character("{b}[arnI.name]{/b}", color="#8000d0")
default arnR = Relationship(vctR.NPClabel, vctR.NPClabel, True)
# Friend's family
default bffI = Information(name = "Erik", sname = "Johnson", age = mcI.age, active = True, rel_status = rel.get('single'))
define bff = Character("{b}[bffI.name]{/b}", color="#19bb2c")
default bffR = Relationship("best friend", "best friend", True)
# Friend's family
default tamI = Information(name = "Tammy", sname = "Johnson", age = (emyI.age-2), active = True, rel_status = rel.get('widow'), rel_partner = mrJohnson)
define tam = Character("{b}Mrs. [tamI.name]{/b}", who_color="#bf5fec")

# The game starts here.

label start:

    stop music fadeout 1.0
    call screen check_age
    "Welcome to [config.name]"
    call NTR_enabler

    call intro

    return
