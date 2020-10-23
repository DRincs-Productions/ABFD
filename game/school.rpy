init python:
    ## PartnerStats
    class Grade():
        def __init__(self, science, math, gym, french, art, music):
            self.average = 50
            self.science = science
            self.math = math
            self.gym = gym
            self.french  = french
            self.art = art
            self.music = 100
        def get_convert(self, grade):
            if (grade == 100):
                return "A+"
            elif (grade > 90):
                val = "A"
            elif (grade > 80):
                val = "B"
            elif (grade > 70):
                val = "C"
            elif (grade > 60):
                val = "D"
            elif (grade > 50):
                val = "E"
            else:
                return "F"
            if (grade%10 > 7):
                return "[let]+"
            elif (grade > 3):
                return let
            elif (grade > 0):
                return "[let]-"
        def update_average(self):
            self.average = self.get_convert((self.science + self.math + self.gym + self.french + self.art + self.music)/6)
        def get_science(self):
            return self.get_convert(self.science)
        def get_math(self):
            return self.get_convert(self.math)
        def get_gym(self):
            return self.get_convert(self.gym)
        def get_french(self):
            return self.get_convert(self.french)
        def get_art(self):
            return self.get_convert(self.art)
        def get_music(self):
            return self.get_convert(self.music)

## Grade MC
default grade = Grade(35, 35, 35, 35, 35, 35)
