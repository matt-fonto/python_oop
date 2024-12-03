# Object-Oriented Programming in Python

Paradigm where software is designed by creating reusable objects that combine data (attributes) and behavior (methods)

## Key Concepts of OOP in Python

### 1. Classes and Objects

- Class: blueprint for creating objects. Defines the structure and behavior of the objects.
- Object: instance of a class

```python
class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog('Buddy', "Golden Retriever")
print(my_dog.bark())
```

### 2. Attributes and methods

- Attributes: variables that store data about an object. They are defined in the `__init__` method or class scope
- Methods: functions that define behavior of the objects. Functions inside classes.

### 3. Encapsulation

- Hide implementation details and provide public interface
- In Python, private attributes are denoted with a single or double underscore `_attribute`, `__attribute`

```py
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance

account = Account(100)
print(account.deposit(50)) # 100 + 50 = 150
print(account.withdraw(120)) # 150 - 120 = 30
```

### 4. Inheritance

- A way to create a new class that is a modified version of an existing one
- The child class inherits attributes and methods from parent
- We use `super` method in the children to inherit all the parent's attributes, this way, we don't need to use `__init__()` repeating the attributes

```py
class Animal:
    def speak(self):
        return "I make sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak()) # Woof!
```

### Polymorphism

- Objects can be treated as instances of their parent class, allowing for flexibility and code reuse

```py
class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
```

### Abstraction

- Focus on essential details while hiding unnecessary implementation. Achieved using abstract base classes (ABCs)

```py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5,10)
print(rect.area())
```
