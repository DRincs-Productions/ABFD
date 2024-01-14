screen paper01(my_text):
    $ xsize_image = convert_to_int(800 * gui.dr_multiplicateur)
    $ ysize_image = convert_to_int(config.screen_height - (150 * gui.dr_multiplicateur))
    $ xmaximum_size = xsize_image - convert_to_int(200 * gui.dr_multiplicateur)
    add "/interface/paper01.webp":
        align (0.5, 0.1)
        xsize xsize_image
        ysize ysize_image

    vbox:
        xmaximum xmaximum_size
        xpos convert_to_int(620 * gui.dr_multiplicateur)
        ypos convert_to_int(280 * gui.dr_multiplicateur)
        text my_text:
            size gui.interface_text_size
            color "#000000"
            font "IndieFlower-Regular.ttf"
