from animal import Animal
class Dog(Animal):#inherting animal
    species="GOLDEN RETRIVER"
    def bark(self):
        return f"{self.name} says Woof!"