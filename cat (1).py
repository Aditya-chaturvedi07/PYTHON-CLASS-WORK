from animal import Animal

class Cat(Animal):#inheriring animal
    Species="CAT SPECIES"
    def meow(self):
        return f"{self.name} says Meow!"
