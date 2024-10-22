class Dog:
    species="coins familiars"
    def __init__(self, name, age):
        self.name=name
        self.age=age
        #self.__age=age-->private property.
    def bark(self):
        return f"{self.name} says woof!"
    def get_age(self):
        return f"{self.name} is {self.age} years old"
    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}"   #custom representation for object when it is printed.

class cat:
    species="Cat species"
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def mew(self):
        return f"{self.name} says meow!"
    def get_age(self):
        return f"{self.name} is {self.age} years old"
    
dog1=Dog("Buddy",3)
dog2=Dog("Charlie",5)

cat1=cat("tom",3)

print(cat1.get_age())
print(dog2.bark())
print(dog1.get_age())
print(dog1.species)
#print(dog1.__age)  --> Can't be accessed outside the class..
print(dog1)#output->Buddy is a 3 year old coins familiars