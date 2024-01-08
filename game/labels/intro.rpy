label intro:
    mc "Cazzo! Sembra passata una vita da quando mi sono trasferito qui a [city_name]. Pensavo che fosse la fine del mondo."
    mc "Ora sono un ragazzo normale di [mcI.age] con problemi classici e nessuna voglia di impegnarmi, ma solo di godermi questa lungha estate."
    mc "Non ho ne una {b}fidanzata{/b}, ne {b}soldi per pagare l'universita{/b} o piani concreti per il futuro e la mia situazione scolastica è pessima, ma ho tempo per rimediare."
    mc "Tutto normale... A parte il fatto che ogni tanto parlo con [beaver], una sorta di demone socratico o Grillo Parlante nelle vesti di un grasso {b}castoro{/b} con problemi di dipendenze che mi aiuta a prendere decisioni."
    show bg profiles family john
    mc "Abito in una casa in collina enorme con anche la piscina, la citta è piena di {b}ragazze{/b} e {b}donne{/b} bellissime, e mi sto trovando bene con la mia {b}famiglia{/b}."
    mc "Ad essere onesto, la mia vera famiglia è morta in un incidente aereo. Per questo mi sono trasferito qui, per iniziare una nuova vita."
    call live_with
    call presentations
    call prologue
    return

label live_with:
    show bg profiles family john
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
    hide bg
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
    show bg profiles family john
    menu:
        mc "Per me è come se fossero la mia nuova famiglia."
        "Di più sulla mia nuova famiglia":
            $ emily_for_mia = miaI.getRelationKeyByCharacter(emily)
            show bg profiles john
            mc "[john] è un ex Navy Seal, dopo la vita militare è caduto in depressione e alcol, iniziando una vita borderline."
            mc "Per me è come se fosse un secondo padre. È sposato con [emily], il loro rapporto ora è molto teso per colpa dell'alcolismo."
            show bg profiles emily
            mc "[emily] è la classica casalinga isterica che lava, stira, cucina, ecc... e si prende cura di me e delle sua famiglia. Dice sempre che sono esattamente il figlio maschio che ha sempre voluto."
            mc "Non si direbbe, ma da giovane faceva la {b}modella{/b}, ma è molto riservata riguardo al suo passato. A volte quando torno a casa la vedo sfogliare vecchie riviste."
            show bg profiles victoria
            mc "[victoria] è la più grande delle sorelle. Credo che io per lei sono di troppo qui, da quando sono arrivato qui mi chiama {b}piccolo sfigato{/b}, {b}piccolo idiota{/b}, {b}orfanello{/b} e altri nomignoli del genere."
            mc "È una {b}matricola del college{/b}, le piacciono i party e fare serate nei locali di zona. Spesso di giorno sta al pc, dice che sta studiando... ma non ci credo molto."
            show bg profiles arianna
            mc "[arianna] ha la mia stessa età, frequentiamo la stessa {b}scuola{/b} e siamo allo stesso anno, ma in classi diverse. In realtà è iscritta in una scuola privata, ma per problemi di spazio è stata trasferita nella nostra."
            mc "È una {b}ragazza molto intelligente{/b} e va molto bene a scuola, come tutta la sua classe. Qualche giorno fa lei e i suoi compagni sono partiti in gita scolastica a Parigi. Tornerà a casa presto."
            show bg profiles mia
            mc "[mia] è la piccola di casa ed è la cocca di [emily_for_mia]. È una ragazzina vivare e piena di vita, sembra uscita da un cartone manga."
            mc "Il suo grande sogno è diventare un {b}influencer{/b}, ma la per la sua [emily_for_mia] è ancora troppo piccola per avere un profilo social."
            mc "Da quando ha cambiato scuola ha diverse difficoltà e spesso mi chiede di {b}aiutarla con i compiti{/b}."
            $ del emily_for_mia
            jump presentations
        "Continua con l'introduzione":
            hide bg
            call presentations_montell
        "Skip":
            hide bg
    return

label presentations_montell:
    show bg car_travel A00A animation
    mc_think "Ora sto tornando a casa, dopo aver passato la notte a casa dei [tammyI.surname]. Li conosco da quando sono piccolo, quando abitavo nella mia vecchia città."
    mc_think "A fianco a me c'è [erik] e lei è [tammy], sua mamma."
    mc_think "Si sono trasferiti qui da poco, per lo stesso mio motivo, cioè iniziare una nuova vita dopo la morte del marito cioè il padre di [erik], [erik_dad]."
    mc_think "Anche lui era un giornalista come mio padre, ma è morto nello stesso incidente aereo."

    window hide
    show screen line_info(
        "a",
        "DRincs",
        _("productions"),
        (0.99, 0.7)
    ) with dissolve
    pause

    tammy "Ehi, [mc]! [erik]! Siete svegli?! Qualcosa non va? Siete così silenziosi."
    window hide
    hide screen line_info with dissolve
    erik "Tutto bene. È che ieri abbiamo giocato a [card_game] fino a tardi."
    tammy "Ahahah, non siete abbastanza grandi per giocare a carte?"
    mc "[card_game] non è solo un gioco di carte..."
    erik "È un modo composto da 5 colori in cui maghi, soldati, orchi... si scontrano per la supremazia."
    erik "Ed io ho sopraffatto [mc] con la mia magia."
    mc "È stato solo fortuna."
    erik "Shhh... Questo è talento, devi allenarti per raggiungere il mio livello."
    erik "Esiste un videogioco per PC, puoi allenarti con quello."
    tammy "Ehh, [erik] passa ore e ore davanti a uno stupido schermo... o a giocare... o a segarsi davanti a strani cartoni giapponesi."
    mc_think "..."
    erik "Mamma! Non puoi dire queste cose!"
    tammy "Non essere anarchico, [erik]. Non c'è niente di male parlare di queste cose. Ora non è più un tabù."

    window hide
    show screen thanks(
        _("Un gioco nato per divertimento"),
        (0.2, 0.3)
    ) with dissolve
    pause
    window hide
    show screen thanks(
        _("Uno sfogo artistico/sessuale"),
        (0.4, 0.38)
    ) with dissolve
    pause
    window hide
    hide screen thanks with dissolve
    pause

    tammy "Comunque, non preoccuparti è una cosa naturale per un ragazzo della tua età."
    tammy "Vorrei solo che uscissi di più, non è sano stare chiusi in casa tutto il giorno."
    mc "Non ti preoccupare [tammy]. Usciremo in sieme e ci faremo degli amici. E magari [erik] si farà una ragazza..."
    tammy "Ahahah, [mc]! Mi faresti un gran regalo."
    mc "Allora è deciso, ora dovrò trovare una ragazza anche per [erik]. Cosi poi se trovo anche io una ragazza, potremo uscire tutti insieme."
    tammy "Guarda che ti stai prendendo un impegno?! Non me lo dimenticherò. Se solo riuscissi ti potrei dare anche un regalo..."
    mc_think "..."
    tammy "Ti potrei offrire una cena o regalare delle carte per giocare a [card_game]."
    mc "Ok, allora me lo segno negli appunti di cose da fare."
    dv "... Dimenticavo... Durante il gioco prenderai degli impegni con i personaggi che incontri. Questi impegni ti permetteranno di ottenere contenuti"
    # TODO: mostrare le immagini della Quest
    dv "Dovrai decidere in che modo portare a termine gli impegni, potrai anche ignorare alcuni di essi o terminare questi impegni in modo negativo. Ma non preoccuparti, sarai ben informato da [beaver] sulle conseguenze delle tue azioni."
    dv "Potrai vedere gli impegni presi negli appunti."
    dv "Questo è l'elenco degli impegni che hai preso. Qui troverai anche le informazioni su come portare a termine gli impegni."
    dv "Ogni impegno è diviso in fasi, per portare a termine un impegno dovrai completare tutte le fasi."
    dv "Alcuni impegni o fasi richiedono delle statistiche, il raggiungimento di alcune relazioni o il completamento di altri fasi/impegni."

    window hide
    show screen thanks_double_line(
        _("Non avrei mai iniziato senza l'aiuto di"),
        _("f95zone"),
        (0.7, 0.6)
    ) with dissolve
    pause

    tammy "[erik]?! Non dici nulla?!"
    window hide
    hide screen thanks_double_line with dissolve
    erik "No, no... Continuate pure a parlare della mia vita privata... Senza rendermi partecipe..."
    mc "Dai, stavamo solo prendendoti in giro. Non ti arrabbiare."
    mc "E neanch'io non ho avuto stringere grandi amicizie qui, ne farmi una ragazza."
    erik "Mmm... Ci servirebbe qualcosa da avere in comune oltre la scuola."
    mc "Esatto! ... Vediamo... A scuola stanno cercando di formare una squadra di basket! Potremmo inscriverci!"
    erik "Buona idea! Solo che... Io  non sono molto bravo a giocare a basket."
    mc "Uhm... So che è parecchio tempo che stanno cercando di formare la squadra, se non raggiungono un numero minimo di giocatori, non potrai partecipare al campionato."
    mc "Secondo me non preoccuparci molto."
    erik "Ok, allora ci proviamo."
    mc "E poi, si sa che le ragazze impazziscono per i giocatori di basket."
    erik "Ahahah, è vero! Se ci impegniamo diventeranno dei fighi con dei fisici da paura."
    tammy "I giocatori di basket sono gli sportivi più sexy... alti, snelli e con braccia muscolose."
    tammy_think "Con ogni parte del corpo slanciata... anche sotto... che bei ricordi..."

    window hide
    pause

    tammy "[mc]..."
    mc "Si?"
    tammy "Hai fatto vedere la pagella del primo quadrimestre a [emily]?"
    mc "No, ancora no... Glie la darò il prima possibile."
    tammy "... [mc]... Se non gliela dai, gliela darò io quando la vedrò."
    tammy "È meglio che gliela dai tu, altrimenti non so come reagirà."
    mc "Ok, ok... Gliela darò sta sera."
    erik "[mc], dobbiamo fare in modo che i nostri voti siano alti, altrimenti il college ci chiuderà la porta in faccia."
    mc "Già, hai ragione. Dobbiamo impegnarci di più."
    mc_think "Non ho proprio voglia di studiare, ma se non lo faccio, non potrò andare al college."
    mc_think "E poi, devo trovare un modo per per pagare le tasse universitarie. Non voglio che [emily] e [john] si facciano carico di queste spese."

    window hide
    pause

    tammy "Bene [mc], sei arrivato."
    tammy "Un momento, [mc]."
    tammy "Ricordo quando eri piccolo e venivi a giocare con [erik]."
    tammy "Poi restavi a cena e rimanevi a dormire. A volte d'estate rimanevi anche per una settimana."
    mc "Si, mi ricordo. Mia mamma cercava di farmi tornare a casa, per non darti troppo disturbo, ma non riusci a convincermi."
    mc "Alla fine lei ti portava la sua torta speciale e alla fine ci invitavi a cena."
    erik "Ahahah, si ricordo anche io. Era una torta al cioccolato con la panna."
    tammy "Già! Quello che ti volevo dire è che se vuoi rimanere a cena da noi o a dormire, non c'è problema. Fai come se fossi a casa tua."
    mc "Grazie [tammy]. Verrò a trovarti spesso."
    
    dv "Bene questo è il momento giusto per dirtelo. Quando [mc] ha un buon rapporto con tutti i membri di una famiglia, il capo famigliare potrebbe dirti che d'ora in poi farai parte della famiglia."
    dv "Questo significa che potrai rimanere a cena o a dormire a casa loro quando vuoi, proprio come se fosse una famiglia."

    window hide
    pause

    tammy "Bene, ti ho trattenuo abbastanza. Vai pure a casa."
    mc "Ok, grazie per tutto. A presto."
    erik "Ciao [mc], ci vediamo a scuola."

    hide bg

    window hide
    pause
    window hide
    show screen line_info(
        "",
        "",
        _("Scusate per il ritardo"),
        (0.99, 0.99)
    ) with dissolve
    pause
    hide screen line_info with dissolve
    window hide
    pause

    return

