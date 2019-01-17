class Material():
    def __init__(self, name, cost, count):
        self.name = name
        self.cost = cost
        self.count = count

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.count=0

    def set_count(self, count):
        self.count = count

    def __str__(self):
        return "Material: "+self.name + " - cost: "+str(self.cost)