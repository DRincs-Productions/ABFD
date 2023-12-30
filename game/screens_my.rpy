screen which_contents_to_enable():
    $ padding_size = convert_to_int(50 * gui.dr_multiplicateur)
    $ xmaximum_size = convert_to_int((config.screen_width - (padding_size * 4))/4)
    $ check_box_size = convert_to_int(80 * gui.dr_multiplicateur)
    modal True
    add "gui/overlay/game_menu.png"

    text _("Quali contenuti vuoi abilitare?"):
        size gui.name_text_size
        align (0.5, 0.1)

    hbox:
        align (0.5, 0.5)
        spacing padding_size
        vbox:
            xmaximum xmaximum_size
            text _("I personaggi con cui hai una relazione possono avere rapporti con altri personaggi di tipo {b}femminile{/b} con il tuo permesso. \n({b}Lesbo MFF{/b})"):
                size gui.interface_text_size
                align (0.5, 0.5)

            use check_box(
                [
                    Function(set_flags, 'lesbian_sharing_content', not get_flags("lesbian_sharing_content")),
                ],
                get_flags("lesbian_sharing_content"),
                check_box_size,
                (0.5, 0.5)
            )
        vbox:
            xmaximum xmaximum_size
            text _("I personaggi con cui hai una relazione possono avere rapporti con altri personaggi di tipo {b}femminile{/b} senza chiederti il permesso. \n({b}Lesbo{/b})"):
                size gui.interface_text_size
                align (0.5, 0.5)

            use check_box(
                [
                    Function(set_flags, 'lesbian_ntr_content', not get_flags("lesbian_ntr_content")),
                ],
                get_flags("lesbian_ntr_content"),
                check_box_size,
                (0.5, 0.5)
            )
        vbox:
            xmaximum xmaximum_size
            text _("I personaggi con cui hai una relazione possono avere rapporti con altri personaggi di tipo {b}maschile{/b} con il tuo permesso. \n({b}Sharing MMF{/b})"):
                size gui.interface_text_size
                align (0.5, 0.5)

            use check_box(
                [
                    Function(set_flags, 'sharing_content', not get_flags("sharing_content")),
                ],
                get_flags("sharing_content"),
                check_box_size,
                (0.5, 0.5)
            )
        vbox:
            xmaximum xmaximum_size
            text _("I personaggi con cui hai una relazione possono avere rapporti con altri personaggi di tipo {b}maschile{/b} senza chiederti il permesso. \n({b}NTR{/b})"):
                size gui.interface_text_size
                align (0.5, 0.5)

            use check_box(
                [
                    Function(set_flags, 'ntr_content', not get_flags("ntr_content")),
                ],
                get_flags("ntr_content"),
                check_box_size,
                (0.5, 0.5)
            )

    textbutton _("Continua"):
        align (0.5, 0.9)

        action Return()