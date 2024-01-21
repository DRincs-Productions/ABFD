image welcomed_into_family_notify = Transform("interface/welcomed_into_family.webp", xysize=(gui.notify_image_size, gui.notify_image_size))
define welcomed_into_tammy_house_notify = NotifyEx(
    message=__("[tammy] ti ha accolto nella sua famiglia"),
    image="welcomed_into_family_notify",
)
