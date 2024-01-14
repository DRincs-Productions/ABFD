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
    call prologue_2
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
            $ emily_for_mia = miaI.getRelationNameByCharacter(emily)
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
            call presentations_montell
        "Skip":
            pass
    hide bg car_travel A00B0B
    return

label presentations_montell:
    hide bg with dissolve
    window hide
    pause
    
    mc_think "Ora sto tornando a casa, dopo aver passato la notte a casa dei [erikI.surname]. Li conosco da quando sono piccolo, quando abitavo nella mia vecchia città."
    show bg car_travel A00A animation with dissolve
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
    # TODO: aggiungere appunti

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
    show screen thanks(
        _("Ispirato da:") + " Milfy City, Timestamps, Man of the House, Loser, F.I.L.F.",
        (0.5, 0.05)
    ) with dissolve
    pause
    window hide
    show screen thanks(
        "Summertime Saga, Big Brother, Lucky Mark, The Twist, The Tyrant",
        (0.5, 0.15)
    ) with dissolve
    pause
    window hide
    show screen thanks(
        "A Family Venture, Photo Hunt and Bones' Tales",
        (0.5, 0.25)
    ) with dissolve
    pause
    window hide
    hide screen thanks with dissolve
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

    show bg car_travel A00A3B
    tammy "Bene [mc], sei arrivato."
    show bg car_travel A01A
    tammy "Un momento, [mc]."
    tammy "Ricordo quando eri piccolo e venivi a giocare con [erik]."
    tammy "Poi restavi a cena e rimanevi a dormire. A volte d'estate rimanevi anche per una settimana."
    show bg car_travel A01B
    mc "Si, mi ricordo. Mia mamma cercava di farmi tornare a casa, per non darti troppo disturbo, ma non riusci a convincermi."
    mc "Alla fine lei ti portava la sua torta speciale e alla fine ci invitavi a cena."
    erik "Ahahah, si ricordo anche io. Era una torta al cioccolato con la panna."
    tammy "Già! Quello che ti volevo dire è che se vuoi rimanere a cena da noi o a dormire, non c'è problema. Fai come se fossi a casa tua."
    # TODO: aggiungere notifica
    mc "Grazie [tammy]. Verrò a trovarti spesso."
    show bg car_travel A01A
    tammy "Bene, ti ho trattenuo abbastanza. Vai pure a casa."
    mc "Ok, grazie per tutto. A presto."
    erik "Ciao [mc], ci vediamo a scuola."

    $ _skipping = False

    hide bg with dissolve

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

    image bg intro A01B animation:
        "bg intro A01A"
        pause 0.2
        "bg intro A01B"
        pause 2.7
        "bg intro A01C"
        pause 0.7
        "bg intro A01D"
        pause 0.7
        "bg intro A01E"
        pause 0.7
        "bg intro A01F"
    show bg intro A01B animation
    show car intro A01A:
        xalign 0
        ypos convert_to_int(3 * gui.dr_multiplicateur)
        linear 0.2 ypos 0
        pause 0.2
        linear 0.2 ypos convert_to_int(2 * gui.dr_multiplicateur)
        linear 0.2 ypos convert_to_int(0 * gui.dr_multiplicateur)
        linear 0.2 yalign 0
        linear 1.0 xpos convert_to_int(-599 * gui.dr_multiplicateur)
        linear 0.5 xpos convert_to_int(-1499 * gui.dr_multiplicateur)

    window hide
    pause

    show bg intro A01F
    hide car
    image logo animation:
        "logo abig"
        pause 0.7
        "logo family"
        pause 0.7
        "logo indebit"
        pause 0.7
        "logo texts"
        pause 1.0
        "logo all" with dissolve
        pause 0.5
    show logo animation:
        align (0.9, 0.1)

    window hide
    pause
    hide bg with dissolve
    window hide
    pause
    hide logo with dissolve
    window hide
    pause

    $ _skipping = True

    return

label prologue_2:
    $ emily_for_mc = mcI.getRelationNameByCharacter(emily)
    $ john_for_mc = mcI.getRelationNameByCharacter(john)

    show bg intro A04A with dissolve
    mc "Heilà, sono tornato a casa."
    window hide
    pause
    show bg intro A04B
    unknown "Sigh sigh sigh..."
    mc_think "Hey, ma chi sta piangendo?"
    show bg intro A04C with Dissolve(1.7)
    mc_think "Cosa? Cosa è successo? La [emily_for_mc] sta piangendo?!"
    show bg intro A04A
    emily "Oh, tesoro."
    mc "Cosa è successo? Perché piangi?"
    emily "Lui... [john]... se n'è andato!"
    show bg intro A05
    emily "Non so cosa fare, non so dove sia andato. Non mi ha detto nulla."
    emily "Non... Non so nulla..."
    emily "Solo... che..."

    menu:
        emily "Questa mattina mi sono svegliata e lui non c'era più. È andato via senza neanche dirmi nulla."
        "Dove è andato?":
            mc "Lui è andato!? Dove?"
            emily "Eh, cosa ne so... È andato via di casa!"
        "Perché?":
            mc "Cosa è successo? Perché è andato via?"
        "È un bene":
            mc "Oh finalmente! È un bene che se ne sia andato. Non ne potevo più."
            emily "Come puoi dire una cosa del genere?!"
            mc_think "..."
            emily "Tu non puoi parlare così di tuo [john_for_mc]! Lui ti ha ospitato in casa sua, ti ha dato un tetto e ti ha aiutato a superare la morte dei tuoi genitori."
        "{i} ( Lo sapevo... ) {/i}":
            mc "Mi dispiace, [emily_for_mc]."
            mc_think "Lo sapevo che prima o poi sarebbe successo."
    
    emily "Avanti, siediti."
    show bg intro A06
    mc_think "..."
    emily "Quando mi sono svegliata questa mattina, ho visto [mia] sconvolta..."
    emily "Lei ha... trovato questa lettera... in cucina. Doveva essere per me, ma lei l'ha trovata per prima."
    show bg intro A06 with dissolve:
        blur 7
    # TODO: mostra lettera
    show text "Mi dispiace [emily] ma non posso vivere qui in questo modo. \n Dopo che ho l'asciato l'esercito non sono più l'uomo di una volta, ora sono un fallito. \n Ho cercato di far finta di niente. \n Il nostro rapporto è diventato strano. \n Non parlamo più, e non ti ho detto molte cose. \n Non voglio che tu e le bambine mi vediate com un peso o un alcolizzato. \n Per questo ho deciso di andarmene. \n Non so se tornerò, ma non voglio più essere un peso per voi."
    window hide
    pause
    hide text
    show bg intro A06 with dissolve:
        blur 0
    emily "Non posso credere che che lui mi abbia lasciato. Non posso perdonarlo. Ma..."
    python:
        probably_game = 50
        text_color = get_probability_color(probably_game)
    menu:
        emily "Ora come possiamo fare senza di lui!?"
        "Ci ha perso lui":
            show bg intro A07
            mc "[emily_for_mc] se qualcuno ha perso, è lui. Io non avrei mai lasciato una donna come te."
            emily "Tesoro, sono fortunata ad avere te. Tu si che sai come farmi sentire meglio una donna."
        "Cosa è successo? {color=[text_color]}(Probabilità [probably_game]\%)":
            $ val = renpy.random.randint(0, 100)
            if (val >= probably_game):
                show bg intro A07
                mc "Cosa è successo? Lui ti ha messo le mani addosso?"
                emily "No no, tesoro. Abbiamo solo litigato come al solito. Sa che da quando ha lasciato l'esercito il nostro rapporto è cambiato."
                emily "Ieri ho cercato di parlargli dei suoi problemi con l'alcol, ma è inutile. Non ha voluto parlare e si è ubriacato ancora più del solito."
                # TODO: Add love
                emily "Tesoro, sai che ho cercato di aiutarlo, ma ieri non ce l'ho fatta più. Gli ho detto che poteva fare quello che voleva, ma questa non è una casa per drogati o alcolizzati. E se voleva continuare, poteva andarsene."
            else:
                mc "Ok, ma volevo capire cosa è successo ieri. Se lui è andato via per qualche motivo... o qualcosa che gli hai detto."
                emily "Quindi secondo te è colpa mia se lui se n'è andato?!"
                mc "No! Non volevo dire questo. È solo che..."
                emily "Ora voglio stare sola per un po', vai pure via."
                jump prologue_end
        "Vai via":
            mc "Ok, [emily_for_mc]. Ora sono un po' stanco, vado in camera mia."
            jump prologue_end

    emily "Tesoro, ti ho trattenuo abbastanza. Vai pure a fare quello che devi fare."
    mc "Ok, [emily_for_mc]. Cerca di riprenderti."

    python:
        del john_for_mc
        del emily_for_mc

label prologue_end:
    hide bg
    show bg intro A09 with dissolve
    window hide
    pause

    mc_think "Cazzo! Ho già abbastanza problemi per conto mio, non ci voleva anche questo."
    mc_think "Chissà come sta [mia]? Forse dovrei andare a parlarle. Probabilmente mi dirà qualcosa di più."

    hide bg with dissolve
    menu:
        dv "Ma prima..."
        "Tutorial":
            call tuturial
        "Continua":
            return
    return

label tuturial:
    show bg intro tutorial A01
    show mc intro tutorial A01 01
    show REC:
        align (0.95, 0.05)
        ysize convert_to_int(100 * gui.dr_multiplicateur)
        xsize convert_to_int(200 * gui.dr_multiplicateur)
    mc "Wow, sembra che funzioni. Questa vecchia videocamera dà un po' di problemi, ma sembra più resistente del previsto."
    mc "Questo è il video diario del 08/06/2019... Ed è anche il video conclusivo della mia ricerca sulle espressioni facciali. Sembra un ottimo modo per barare a poker... o almeno lo sembra su \"Lite to Me\"."
    show mc intro tutorial A01 03
    mc "Bene... questo... è l'ultimo video. Perché sono giunto alla conclusione che..."
    mc "È uno studio molto complesso e lungo du cui... non ci ho capito niente. Quindi ho deciso di non continuare."
    mc "Ma dopo un po' di ricerche in sociopsicologia. Ho scoperto qualcosa di interessante sulla società..."
    mc "Le relazione tra persone alla fine sono solo una questione di scambi di favori, denaro, affetto, sesso, ecc..."
    mc "Per questo ho iniziato a segnarmi sull'aggenda tutte le necessità delle persone che incontro e gli impegni che prendo con loro."
    mc "In questo modo posso ricordarmi di fare quello che devo fare e risquotere le mie ricompense che mi spettano."
    mc "Questa è la mia agenda."
    mc "Questo è l'elenco degli impegni che ho preso."
    mc "Qui ci sono anche le istruzioni per portare a termine gli impegni."
    mc "Ogni impegno è diviso in fasi, per portare a termine un impegno dovrai completare tutte le fasi."
    mc "Non cancello mai le fasi precedenti. Se voglio rileggerle possp sfogliare le pagine precedenti."
    beaver "Ricorda dovrai anche decidere in che modo terminare gli impegni. Potrai anche ignorare alcuni di essi o terminare questi impegni in modo negativo. Ma non preoccuparti, ti informero sempre sulle conseguenze delle tue azioni."
    mc "Ok, grazie [beaver]."

    mc "Alcuni impegni o fasi richiedono delle statistiche, il raggiungimento di alcune relazioni o il completamento di altri fasi/impegni."
    mc "Qui posso vedere le statistiche e le relazioni che ho con le persone che conosco."
    mc "Ho notato che se ho una buona relazione con tutti i membri di una famiglia, il capo famiglia a volte mi chiede di diventare un membro della famiglia. Forse perché sono orfano."
    mc "Questo significa che potrò rimanere a cena o a dormire a casa loro quando voglio, proprio come se fossi un membro della famiglia."

    mc "A volte le persone con cui ho una buona relazione mi inviano messaggi o mi chiamano per chiedermi di uscire o per chiedermi un favore."
    mc "Sul cellulare posso vedere tutti i messaggi che ho ricevuto e le chiamate perse."
    mc "Ci sono anche altre funzioni interessanti che non ho avuto modo di provare."

    mc "Prima di finire..."
    mc "Non è da molto che mi sono trasferito qui a [city_name]. È una buona cittadina piena di cose da fare e persone da conoscere."
    mc "Ma a volte è fin troppo tranquilla. Per questo a volte prendo il bus per andare a [city_metro]."
    mc "È una metropoli futuristica piena di vita, luci e rumori. È un posto molto interessante."
    mc "A [city_metro] sembra non esserci molta criminalità, ma a [ghetto_name] è un altro discorso."
    mc "È un ghetto pieno di criminali, drogati, prostitute, ecc... È un posto molto pericoloso."
    mc "A [city_name] c'è anche una spiaggia, ma non è molto grande."
    mc "Se voglio voglio prendermi una pausa, posso andare a [city_beach]."
    mc "[city_beach] è un ottimo posto per andare in vacanza, ma è anche un posto molto costoso."
    mc "Ed infine questa è la mia casa."
    mc "È una casa molto grande, in cui ci sono molte stanza."
    show mc intro tutorial A01 02
    emily_shout "Ehi, [mc]! Il pranzo è pronto!!! Stiamo solo aspettando te."
    mc "Ok... [emily_for_mc]! Vengo subito!"
    mc "Ecco, ora devo andare a pranzo. Per ora è tutto, ci vediamo al prossimo video."
    return
