label intro:
    mc "Cazzo! Sembra passata una vita da quando mi sono trasferito qui a [city_name]. Pensavo che fosse la fine del mondo."
    mc "Ora sono un ragazzo normale di [mcI.age] con problemi classici e nessuna voglia di impegnarmi, ma solo di godermi questa lungha estate."
    mc "Non ho ne una {b}fidanzata{/b}, ne {b}soldi per pagare l'universita{/b} o piani concreti per il futuro e la mia situazione scolastica è pessima, ma ho tempo per rimediare."
    mc "Tutto normale... A parte il fatto che ogni tanto parlo con [beaver], una sorta di demone socratico o Grillo Parlante nelle vesti di un grasso {b}castoro{/b} con problemi di dipendenze che mi aiuta a prendere decisioni."
    show profiles family john
    mc "Abito in una {b}casa{/b} enorme con anche la piscina e mi sto trovando bene con la mia {b}famiglia{/b}."
    mc "Ad essere onesto, la mia vera famiglia è morta in un incidente aereo. Per questo mi sono trasferito qui, per iniziare una nuova vita."
    call live_with
    call presentations
    return

label live_with:
    show profiles family john
    menu:
        mc "Ora io vivo con/in:"
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
                    victoria: "housemate",
                    arianna: "housemate",
                    mia: "housemate",
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
                    mc: "housemate",
                    john: "landlord",
                    emily: "landlord",
                    arianna: "housemate",
                    mia: "housemate",
                }
                ariannaI.relationships = {
                    mc: "housemate",
                    john: "landlord",
                    emily: "landlord",
                    victoria: "housemate",
                    mia: "housemate",
                }
                miaI.relationships = {
                    mc: "housemate",
                    john: "landlord",
                    emily: "landlord",
                    victoria: "housemate",
                    arianna: "housemate",
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
    $ mcI.setRelationNameByCharacter(character = emily, relation_key = "landlord", relaction_types = relactions | relactions_female)
    "Io sono il suo:"
    $ emilyI.setRelationNameByCharacter(character = mc, relation_key = "tenant", relaction_types = relactions | relactions_male)
    show screen arrow((0.05, 0.15), 0)
    "Il nome di lui è:"
    $ johnI.changeName()
    "[john] è mio:"
    $ mcI.setRelationNameByCharacter(character = john, relation_key = "landlord", relaction_types = relactions | relactions_male)
    "Io sono il suo:"
    $ johnI.setRelationNameByCharacter(character = mc, relation_key = "tenant", relaction_types = relactions | relactions_male)
    show screen arrow((0.38, 0.32), 180)
    "Il nome di lei è:"
    $ miaI.changeName()
    "[mia] è mia:"
    $ mcI.setRelationNameByCharacter(character = mia, relation_key = "housemate", relaction_types = relactions | relactions_female)
    "Io sono il suo:"
    $ miaI.setRelationNameByCharacter(character = mc, relation_key = "housemate", relaction_types = relactions | relactions_male)
    
    python:
        mia_is_for_mc = mcI.getRelationKeyByCharacter(mia)
        mc_is_for_mia = miaI.getRelationKeyByCharacter(mc)

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
    $ emilyI.setRelationNameByCharacter(character = mc, relation_key = "tenant", relaction_types = relactions | relactions_female)
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
    $ emilyI.setRelationNameByCharacter(character = victoria, relation_key = "landlord", relaction_types = relactions | relactions_female)
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
    $ johnI.setRelationNameByCharacter(character = victoria, relation_key = "landlord", relaction_types = relactions | relactions_male)
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
    python:
        del mia_is_for_mc
        del mc_is_for_mia
        del victoria_is_for_emily
        del emily_is_for_victoria
        del john_is_for_victoria
    return

label presentations:
    show profiles family john
    menu:
        mc "Per me è come se fossero la mia nuova famiglia."
        "Di più sulla mia nuova famiglia":
            $ emily_for_mia = miaI.getRelationKeyByCharacter(emily)
            show profiles john
            mc "[john] è un ex Navy Seal, dopo la vita militare è caduto in depressione e alcol, iniziando una vita borderline."
            mc "Per me è come se fosse un secondo padre. È sposato con [emily], il loro rapporto ora è molto teso per colpa dell'alcolismo."
            show profiles emily
            mc "[emily] è la classica casalinga isterica che lava, stira, cucina, ecc... e si prende cura di me e delle sua famiglia. Dice sempre che sono esattamente il figlio maschio che ha sempre voluto."
            mc "Non si direbbe, ma da giovane faceva la {b}modella{/b}, ma è molto riservata riguardo al suo passato. A volte quando torno a casa la vedo sfogliare vecchie riviste."
            show profiles victoria
            mc "[victoria] è la più grande delle sorelle. Credo che io per lei sono di troppo qui, da quando sono arrivato qui mi chiama {b}piccolo sfigato{/b}, {b}piccolo idiota{/b}, {b}orfanello{/b} e altri nomignoli del genere."
            mc "È una {b}matricola del college{/b}, le piacciono i party e fare serate nei locali di zona. Spesso di giorno sta al pc, dice che sta studiando... ma non ci credo molto."
            show profiles arianna
            mc "[arianna] ha la mia stessa età, frequentiamo la stessa {b}scuola{/b} e siamo allo stesso anno, ma in classi diverse. In realtà è iscritta in una scuola privata, ma per problemi di spazio è stata trasferita nella nostra."
            mc "È una {b}ragazza molto intelligente{/b} e va molto bene a scuola, come tutta la sua classe. Qualche giorno fa lei e i suoi compagni sono partiti in gita scolastica a Parigi. Tornerà a casa presto."
            show profiles mia
            mc "[mia] è la piccola di casa ed è la cocca di [emily_for_mia]. È una ragazzina vivare e piena di vita, sembra uscita da un cartone manga."
            mc "Il suo grande sogno è diventare un {b}influencer{/b}, ma la per la sua [emily_for_mia] è ancora troppo piccola per avere un profilo social."
            mc "Da quando ha cambiato scuola ha diverse difficoltà e spesso mi chiede di {b}aiutarla con i compiti{/b}."
            $ del emily_for_mia
            jump presentations
        "Continua con l'introduzione":
            hide profile
            jump presentations_montell
        "Skip":
            call renaming_friend
            hide profile
            jump prologue
    return
