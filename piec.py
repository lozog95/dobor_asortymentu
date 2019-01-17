class Piec():
    def __init__(self, name, time_per_material, time_limit):
        self.name = name
        self.time_per_material = time_per_material
        self.time_limit=time_limit

    def __init__(self, name):
        self.name = name

    def set_time_per_material(self, time_per_material):
        self.time_per_material=time_per_material

    def set_time_limit(self, time_limit):
        self.time_limit=time_limit

    def __str__(self):
        return "Piec: "+self.name + " - time/material: "+str(self.time_per_material) + \
               " - time limit: " + str(self.time_limit)
