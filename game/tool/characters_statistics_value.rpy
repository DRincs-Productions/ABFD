default stats = {
    'mc'        :   Statistics(gender = "M"),
}

label stats_default_family:
    $ stats['jn'] = Statistics(gender = "M", virgin = False, friendship = 30, addiction = 15,
    other_values= {
        'strength'      :   130,
        'perception'    :   70,
        'charisma'      :   40,
        'intelligence'  :   20,
        'agility'       :   40,
    })
    $ stats['emy'] = Statistics(gender = "F", virgin = False, favour = 40, love = 10, against = 40,
    other_values= {
        'strength'      :   40,
        'charisma'      :   40,
        'intelligence'  :   50,
        'agility'       :   40,
        'favour'        :   20,
    })
    $ stats['vct'] = Statistics(gender = "F", virgin = False, love = 10, against = 20,
    other_values= {
        'strength'      :   50,
        'charisma'      :   70,
        'intelligence'  :   20,
        'agility'       :   40,
    })
    $ stats['arn'] = Statistics(gender = "F", virgin = True, friendship = 20, against = 15, addiction = 10,
    other_values= {
        'strength'      :   10,
        'charisma'      :   20,
        'intelligence'  :   50,
        'agility'       :   60,
    })
    $ stats['mia'] = Statistics(gender = "F", virgin = True, friendship = 10, against = 10,
    other_values= {
        'intelligence'  :   30,
    })
    return

label stats_default_bfffamily:
    $ stats['bff'] = Statistics(gender = "M", virgin = True, friendship = 90,
    other_values= {
        'strength'      :   20,
        'perception'    :   40,
        'intelligence'  :   70,
        'videogame'     :   80,
    })
    $ stats['tam'] = Statistics(gender = "F", virgin = True, friendship = 90,
    other_values= {
        'strength'      :   30,
        'charisma'      :   20,
        'intelligence'  :   10,
        'agility'       :   50,
        'yoga'          :   80,
    })
    return
