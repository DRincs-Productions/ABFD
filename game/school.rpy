init python:
    class SchoolGrade():
        """In this class there are the average list of each subject, and the functions to manage them"""
        def __init__(self, materials):
            self.materials = {}
            self.materials.update(materials)
            self.average = None
            self.update_average()
        def get_convert(self, grade):
            """Convert numeric grade to alphabetical grade"""
            if (grade == None or grade == ""):
                return None
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
            """Update average, i.e. the average of all subjects"""
            item = 0
            amt = 0
            for matter in self.materials.values():
                if matter != None:
                    item += 1
                    amt += matter
            # if there are no elements
            if (item == 0):
                if (self.average == None):
                    self.average = "Unknown"
                return

            else:
                self.average = self.get_convert(amt/item)
            del item
            del amt
        def get_average_matter(self, matter):
            """Returns the average of a matter"""
            return self.get_convert(self.get(matter))
        def get(self, text):
            """Returns the value "text", in case it does not exist returns \"Unknown\""""
            if text in self.materials:
                return self.materials[text]
            else:
                return None
        def set(self, text, value):
            """Function to set or add a new value"""
            if (text != None and text != ""):
                self.materials[text] = value
            else:
                remove(text)
        def remove(self, text):
            """Delete the text value"""
            del materials[text]

default school_grades_mc = SchoolGrade(materials = {
    'science'   :   35,
    'math'      :   35,
    'gym'       :   35,
    'french'    :   35,
    'art'       :   35,
    'music'     :   35,
})

# TODO: default school_grades_other = {}
