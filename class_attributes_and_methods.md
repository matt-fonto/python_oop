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
