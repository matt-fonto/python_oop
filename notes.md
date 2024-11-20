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
- Methods: functions that define behavior of the objects

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
