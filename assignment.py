# define class method and static method in python with example ..

class MyClass:
    class_variable = 0

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

# Usage
MyClass.increment_class_variable()
print(MyClass.class_variable)  # Output: 1


class MyClass1:
    @staticmethod
    def multiply(x, y):
        return x * y

# Usage
result = MyClass1.multiply(5, 3)
print(result)  # Output: 15

"""
Class Method
Definition: A class method is a method that is bound to the class rather than its object. It can modify the class state that applies across all instances of the class.
Decorator: It is defined using the @classmethod decorator.
First Parameter: The first parameter is typically named cls, which refers to the class itself.


Static Method
Definition: A static method is a method that does not access or modify the class or instance state. It behaves like a regular function but lives in the class's namespace.
Decorator: It is defined using the @staticmethod decorator.
Parameters: It does not take self or cls as its first parameter.
"""