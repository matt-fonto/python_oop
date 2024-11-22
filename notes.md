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

## Array methods Python

### 1. Adding elements

- append(item): add item to the end of the list
- extend(iterable): add multiple items from an iterable to the list
- insert(index, item): add item at specific index

```py
arr.append(4)
arr.extend([1,2,3])
arr.insert(2, 100)
```

### 2. Removing elements

- pop(index): remove and return the item at the specific index (last is the default)
- remove(item): remove the first occorrence of the item
- clear(): remove all elements from the list

```py
arr.pop() # removes last item
arr.pop(1) # removes item at index 1
arr.clear()
```

### 3. Searching

- index(item, start, end): return the index of the first occorrence of the item
- count(item): count occorrences of the item in the list

```py
arr.index(5)
arr.count(5)
```

### 4. Sorting and reversing

- sort(key=None, reverse=False): sort the list in place
- reverse(): reverses the list

```py
arr.sort() # asc
arr.sort(reverse=True) # des
arr.reverse()
```

### 5. Other useful methods

- copy(): create a shallow copy of the list
- len(arr): get the number of elements
- max(arr) || min (arr): get the largest or smallest element
- sum(arr): sum all numeric values
- list(iterable): converts iterable (range, tuple) to a list

```py
new_arr = arr.copu()
len(arr)
max(arr)
min(arr)
sum(arr)
arr = list(range(5))
```

## Typing in Python

- Python accepts specifying the types of aparams and the return type of a function.
- We use `type hints`. This feature is a part of type annotations

```py
def function_name(param1: Type1, param2: Type2) -> ReturnType:
    # function body

    # pass: placeholder that does nothing. Used as temporary placeholder
    # allows us to create a function, class or control structure without any actual code inside
    pass

def add(a:int, b:int) -> int:
    return a + b

def greet(name:str, age:int) -> str:
    return f"Hello, {name}. You are {age} years old."

from typing import List, Dict, Optional, Callable

# using lists and dictionaries: List, Dict
def process_data(numbers: List[int], info: Dict[str,str]) -> List[int]:
    return [num * 2 for num in numbers]

# adding optional: Optional
def get_user_info(user_id:int, nickname: Optional[str] = None) -> str:
    return f"User id: {user_id}, Nickname: {nickname or 'N/A'}

# adding function as params: Callable
def apply_function(x:int, func: Callable[[int], int]) -> int:
    return func(x)

print(apply_function(5, lambda n: n*2))
```

### Common type hints

- Built-in: int, float, str, bool, list, dict, set, tuple
- Complex types (from `typing` module): List, Dict, Set, Tuple, Optional, Callable, Union

### Custom Class

```py
class User:
    def __init__(self, name:str):
        self.name = name

def greet_user(user:User) -> string:
    return f"Hello, {user.name}!"
```

## Class attributes

- Variable that is shared among all instances of a class
- Defined directly within the class body, outside of any instance method

```py
class Car:
    wheels = 4 # Class attribute

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

print(Car.wheels) # printing straight from the class

car1 = Car("red", "toyota")

print(car1.wheels) # 4

Car.wheels = 6 # we're modifying the attribute at the class level
print(car1.wheels) # 6
```

### Class attributes vs. Instance attributes

- Class attributes:

  - Shared among all instances
  - Changes to the attribute affect all instances unless specially overriden
  - Defined within class body

- Instance attributes:
  - Unique to each instance
  - Defined in the **init** method or other instance-specific contexts
  - Defined within instance method

```py
class Example:
    class_attribute = "Shared"

    def __init__(self, instance_value):
        self.instance_value = instance_value

obj1 = Example('Instance 1')
obj2 = Example('Instance 2')

print(obj1.class_attribute) # Shared
print(obj1.class_attribute) # Shared

print(obj1.instance_value) # instance 1
print(obj2.instance_value) # instance 2

Example.class_attribute = 'Modified'
print(obj1.class_attribute) # Modified
print(obj1.class_attribute) # Modified
```

- Summary:
  - Class attribute: shared, defined at the class level, accessed by the class or instance. Changes to it reflect in every instance, since it's global
  - Instance attribute: Unique, defined at instantiation, usually in **init**

## Magic attributes and methods

- Also known as Dunder methods are special methods with names starting and ending with double underscores `__init__`, `__str__`
- They are used to define how objects of a class behave in specific situations, such as: initialization, string representation, comparison, arithmetic and more

### Common magic methods

1. Initialization and representation

- **init**(self, ...): called when the object is created. Used to initialize attributes

- **str**(self): defines user-friendly string representation used by print

```py
class Example:
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"Example with value {self.value}"

    def __repr__(self):
        return f"Example({self.value})"
```

### Magic attributes

- **dict**: shows all attributes from the class

```py
print(Class.__dict__) # All the attributes for Class level
print(Object.__dict__) # All the attributes for Instance level
```

## Class vs. Static methods

- Class and Static methods are used to define behaviors that aren't tied to a specific instance of the class
- Even though they could be called from an instance, normally you will call the class and the static methods from the class itself.

### Class method @classmethod

- Receives reference to the class `cls`
- Operates on the class itself
- Has access to class attributes via `cls`
- Modify or interact with class-level data

### Static method @staticmethod

- Does not receive instance,`self`, nor class, `cls`
- No access to class or instance attributes
- Static methods are good to do something that has a relationship with the class, but not something that must be unique per instance
- Behaves like a regular function, but belongs to the class's namespace

```py
class MyClass:
    # regular instance method
    # takes on parameter: self
    # points to an instance of our class
    def method(self):
        return 'instance method', self

    # takes a @classmethod decorator
    # takes `cls` as a param
    # points to the class, not the object instance, when the method is called
    # can't modify object instances
    @classmethod
    def classmethod(cls):
        return 'class method', cls

    # takes no `self`, nor `cls` param
    # don't modify object nor class state
    @staticmethod
    def staticmethod():
        return 'static method',
```
