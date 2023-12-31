label intro:
    mc "Cazzo! Sembra passata una vita da quando mi sono trasferito qui a [city_name]. Pensavo che fosse la fine del mondo."
    mc "Ora sono un ragazzo normale di [mcI.age] con problemi classici e nessuna voglia di impegnarmi, ma solo di divertirmi."
    mc "Non ho una {b}fidanzata{/b}, un {b}lavoro{/b} o piani concreti per il futuro e la mia situazione scolastica è pessima, ma ho tempo per rimediare."
    mc "Tutto normale... A parte il fatto che ogni tanto parlo con [beaver], una sorta di demone socratico o Grillo Parlante nelle vesti di un grasso {b}castoro{/b} con problemi di dipendenze che mi aiuta a prendere decisioni."
    show profiles family john
    mc "Abito in una {b}casa{/b} enorme con anche la piscina e mi sto trovando bene con la mia {b}famiglia{/b}."
    mc "Ad essere onesto, la mia vera famiglia è morta in un incidente aereo. Per questo mi sono trasferito qui, per iniziare una nuova vita."
    call live_with
    return

label live_with:
    menu:
        mc "Ora io vivo con/in"
        "Step family":
            python:
                mcI.relationships = {
                    john: "dad",
                    emily: "mom",
                    victoria: "sister",
                    arianna: "sister",
                    mia: "sister",
                }
                johnI.relationships = {
                    mc: "son",
                    emily: "wife",
                    victoria: "daughter",
                    arianna: "daughter",
                    mia: "daughter",
                }
                emilyI.relationships = {
                    mc: "son",
                    john: "husband",
                    victoria: "daughter",
                    arianna: "daughter",
                    mia: "daughter",
                }
                victoriaI.relationships = {
                    mc: "brother",
                    john: "dad",
                    emily: "mom",
                    arianna: "sister",
                    mia: "sister",
                }
                ariannaI.relationships = {
                    mc: "brother",
                    john: "dad",
                    emily: "mom",
                    victoria: "sister",
                    mia: "sister",
                }
                miaI.relationships = {
                    mc: "brother",
                    john: "dad",
                    emily: "mom",
                    victoria: "sister",
                    arianna: "sister",
                }
        "Una casa in affitto finanziata dalla scuola":
            python:
                mcI.relationships = {
                    john: "landlord",
                    emily: "landlord",
                    victoria: "tenant",
                    arianna: "tenant",
                    mia: "tenant",
                }
                johnI.relationships = {
                    mc: "tenant",
                    emily: "wife",
                    victoria: "tenant",
                    arianna: "tenant",
                    mia: "tenant",
                }
                emilyI.relationships = {
                    mc: "tenant",
                    john: "husband",
                    victoria: "tenant",
                    arianna: "tenant",
                    mia: "tenant",
                }
                victoriaI.relationships = {
                    mc: "tenant",
                    john: "landlord",
                    emily: "landlord",
                    arianna: "tenant",
                    mia: "tenant",
                }
                ariannaI.relationships = {
                    mc: "tenant",
                    john: "landlord",
                    emily: "landlord",
                    victoria: "tenant",
                    mia: "tenant",
                }
                miaI.relationships = {
                    mc: "tenant",
                    john: "landlord",
                    emily: "landlord",
                    victoria: "tenant",
                    arianna: "tenant",
                }
        "( Personalizzata )":
            call customize_mc_family
    hide profiles
    return

label customize_mc_family:
    show screen arrow((0.25, 0.15), 180)
    "Il nome di lei è:"
    $ emilyI.changeName()
    "[emily] è mia:"
    $ mcI.setRelationNameByCharacter(character = emily, relation_key = "mom", relaction_types = relactions | relactions_female)
    "Io sono il suo:"
    $ emilyI.setRelationNameByCharacter(character = mc, relation_key = "son", relaction_types = relactions | relactions_male)
    show screen arrow((0.05, 0.15), 0)
    "Il nome di lui è:"
    $ johnI.changeName()
    "[john] è mio:"
    $ mcI.setRelationNameByCharacter(character = john, relation_key = "dad", relaction_types = relactions | relactions_male)
    "Io sono il suo:"
    $ johnI.setRelationNameByCharacter(character = mc, relation_key = "son", relaction_types = relactions | relactions_male)
    show screen arrow((0.38, 0.32), 180)
    "Il nome di lei è:"
    $ miaI.changeName()
    "[mia] è mia:"
    $ mcI.setRelationNameByCharacter(character = mia, relation_key = "sister", relaction_types = relactions | relactions_female)
    "Io sono il suo:"
    $ miaI.setRelationNameByCharacter(character = mc, relation_key = "brother", relaction_types = relactions | relactions_male)

    $ mia_is_for_mc = mcI.getRelationKeyByCharacter(mia)
    $ mc_is_for_mia = miaI.getRelationKeyByCharacter(mc)

    show screen arrow((0.72, 0.25), 180)
    "Il nome di lei è:"
    $ ariannaI.changeName()
    "[arianna] è mia:"
    $ mcI.setRelationNameByCharacter(character = arianna, relation_key = mia_is_for_mc, relaction_types = relactions | relactions_female)
    "Io sono il suo:"
    $ ariannaI.setRelationNameByCharacter(character = mc, relation_key = mc_is_for_mia, relaction_types = relactions | relactions_male)
    show screen arrow((0.9, 0.13), 180)
    "Il nome di lei è:"
    $ victoriaI.changeName()
    "[victoria] è mia:"
    $ mcI.setRelationNameByCharacter(character = victoria, relation_key = mia_is_for_mc, relaction_types = relactions | relactions_female)
    "Io sono il suo:"
    $ victoriaI.setRelationNameByCharacter(character = mc, relation_key = mc_is_for_mia, relaction_types = relactions | relactions_male)

    hide arrow

    "Per [emily], [john] chi è [victoria] (la stessa cosa per [arianna] e [mia])?"
    $ emilyI.setRelationNameByCharacter(character = mc, relation_key = "daughter", relaction_types = relactions | relactions_female)
    python:
        victoria_is_for_emily = emilyI.getRelationKeyByCharacter(victoria)
        emilyI.relationships = {
            victoria: victoria_is_for_emily,
            arianna: victoria_is_for_emily,
            mia: victoria_is_for_emily,
        }
        johnI.relationships = {
            victoria: victoria_is_for_emily,
            arianna: victoria_is_for_emily,
            mia: victoria_is_for_emily,
        }

    "Per [victoria], [arianna] e [mia] chi è [emily]?"
    $ emilyI.setRelationNameByCharacter(character = victoria, relation_key = "mom", relaction_types = relactions | relactions_female)
    python:
        emily_is_for_victoria = victoriaI.getRelationKeyByCharacter(emily)
        victoriaI.relationships = {
            emily: emily_is_for_victoria,
        }
        ariannaI.relationships = {
            emily: emily_is_for_victoria,
        }
        miaI.relationships = {
            emily: emily_is_for_victoria,
        }
    
    "Per [victoria], [arianna] e [mia] chi è [john]?"
    $ johnI.setRelationNameByCharacter(character = victoria, relation_key = "dad", relaction_types = relactions | relactions_male)
    python:
        john_is_for_victoria = victoriaI.getRelationKeyByCharacter(john)
        victoriaI.relationships = {
            john: john_is_for_victoria,
        }
        ariannaI.relationships = {
            john: john_is_for_victoria,
        }
        miaI.relationships = {
            john: john_is_for_victoria,
        }
    return
