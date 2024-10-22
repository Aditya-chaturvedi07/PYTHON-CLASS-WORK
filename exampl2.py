class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__age=age
    def get_age(self):
        return f"{self.name} is {self.age} years old"
    def __str__(self):
        return f"{self.name} is {self.__age} years old"

class Dog(Animal):#inherting animal
    species="GOLDEN RETRIVER"
    def bark(self):
        return f"{self.name} says Woof!"

class Cat(Animal):#inheriring animal
    Species="CAT SPECIES"
    def meow(self):
        return f"{self.name} says Meow!"



dog1=Dog("d1",3)
cat1=Cat("c1",3)

print(dog1)
print(cat1)
print(dog1.bark)
print(cat1.meow)