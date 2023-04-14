class BeeElephant:
    def __init__(self, pB, pE):
        self.partB = pB
        self.partE = pE
    def fly(self):
        if (self.partB >= self.partE):
            return True
        else :
            return False
    def trumpet(self):
        if (self.partB <= self.partE):
            return "tu-tu-doo-doo!"
        else :
            return "wzzzzz"
    def get_parts(self):
        parts=[self.partE, self.partB]
        return parts
    def eat(self, meal, value):
        if (meal == "nectar") :
            if (self.partE - value >= 0) :
                self.partE -= value
                self.partB += value
            else :
                return "Error"
        if (meal == "grass") :
            if (self.partB - value >= 0) :
                self.partB -= value
                self.partE += value
            else :
                return "Error"
        return "Data changed successfully!"
be1 = BeeElephant(17, 83)
print(be1.get_parts())
print(be1.trumpet())
print(be1.fly())
print(be1.eat("grass", 50))
print(be1.get_parts())
print(be1.trumpet())
print(be1.fly())