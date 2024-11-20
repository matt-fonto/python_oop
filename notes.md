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
