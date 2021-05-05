image bg at_table preparation = Composite( (gui.width, gui.height),
    (0, 0), "/family/at_table/preparation01.webp",
    (0, 0), "/family/at_table/preparation01A.webp")
image bg at_table preparation A = Composite( (gui.width, gui.height),
    (0, 0), "/family/at_table/preparation01.webp",
    (0, 0), "/family/at_table/preparation01B.webp")

label at_table_preparation:
    show bg at_table preparation A
    ""
    show bg at_table preparation
    call screen room_navigation