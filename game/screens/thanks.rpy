screen thanks(text1, my_align):
    $ text_size = convert_to_int(60 * gui.dr_multiplicateur)

    vbox:
        align my_align
        text text1:
            size text_size
            align (0.5, 0.5)
            color "#ffffff"
            outlines [(2, "#00000080", 1, 1)]
            font "Salsa-Regular.ttf"

screen thanks_double_line(text1, text2, my_align):
    $ little_size = convert_to_int(40 * gui.dr_multiplicateur)
    $ big_size = convert_to_int(60 * gui.dr_multiplicateur)
    
    vbox:
        align my_align
        text text1:
            size little_size
            align (0.1, 0.1)
            color "#25d0ee"
            outlines [(2, "#00000080", 1, 1)]
            font "Salsa-Regular.ttf"
        text text2:
            size big_size
            align (0.9, 0.9)
            color "#ffffff"
            outlines [(5, "#00000080", 1, 1)]
            font "Anton-Regular.ttf"

screen line_info(text1, text2, text3, my_align):
    $ little_size = convert_to_int(60 * gui.dr_multiplicateur)
    $ big_size = convert_to_int(80 * gui.dr_multiplicateur)
    $ spacing_size = convert_to_int(5 * gui.dr_multiplicateur)

    hbox:
        align my_align
        spacing spacing_size
        text text1:
            align (0.5, 0.8)
            outlines [(5, "#00000080", 1, 1)]
            font "Salsa-Regular.ttf"
            size little_size
        text text2:
            align (0.5, 0.9)
            color "#da6404"
            outlines [(2, "#00000080", 1, 1)]
            font "Anton-Regular.ttf"
            size big_size
        text text3:
            align (0.5, 0.8)
            color "#ffffff"
            outlines [(5, "#00000080", 1, 1)]
            font "Salsa-Regular.ttf"
            size little_size
