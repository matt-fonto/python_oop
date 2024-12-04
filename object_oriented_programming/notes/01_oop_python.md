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

- Restrict direct access/update to some attributes. For that we use the getters and setters
- Hide implementation details and provide public interface
- In Python, private attributes are denoted with a single or double underscore `_attribute`, `__attribute`

#### Single vs. Double Underscore

- Single underscore:

  - Purpose: Indicates the attribute is intended to be protected (used internally or by subclasses), but it's not strictly private
  - Behavior: Not enforced by Python, it's a convention
  - Use case: For attributes that shoudn't be accessed or set directly, but can be accessed in subclasses

  ```py
    class Example:
        def __init__(self):
            self._protected_attribute = 42 # Internal use only

    obj = Example()
    print(obj._protected_attribute) # Accessible, but breaking convention
  ```

- Double underscore:

  - Purpose: Triggers `name mangling`, what makes the attribute difficult to access directly (intended for strong encapsulation and avoiding name collisions in subclasses)
  - Behavior: Python renames the attribute internally to `__ClassName__attribute`
  - Use case: Attributes that are strictly private and not accessible even in subclasses

  ```py
    obj = Example()
    print(obj.__strictly_priv_att) # AttributeError
    print(obj.__Example__strictly_priv_att) # Accessible with name mangling
  ```

  - Which one to use?
    1. Single underscore (`_attribute`):
       - Indicate attribute is internal or protect, but does't need strict privacy
       - Easier to debug and less restrictive
    2. Double underscore (`__attribute`):
       - Strong encapsulation and want to avoid accidental name collision in subclasses
       - Use sparingly because name mangling can complicate debugging

```py
class Account:
    def __init__(self, balance):
        self._balance = balance

    @property # get
    def balance(self)"
        return self._balance

    @balance.setter # set
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def deposit(self, amount):
        self.balance += amount # use setter
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount # setter
        return self.balance

account = Account(100)

account._balance = 150 # it won't work
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
- Shows necessary attributes and hides unnecessary information
- Hide unnecessary details from the user, meaning devs who will use our class to instantiate their objects

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
