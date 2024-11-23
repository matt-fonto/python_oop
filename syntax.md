## Fundaments Python Syntax

### Variable and data types

```py
x = 10 # int
y = 3.14 # float
name = 'Matt' # str
is_active = True  # bool

a, b, c = 1, 2, 3 # multiple assignment
```

### Control flow

- Refers to the order in which individual instructions, statements, or blocks of code are executed or evaluated.
- It determines how a program's logic flows based on conditions, loops, and branching

#### If-else statements

```py
x = 10

if x > 5:
    print ("x is greater than five")
elif x == 5:
    print ("x is equal to five")
else:
    print ("x is less than five")
```

#### For loops

- Iterate over a range or any iterable (list, tuples, dictionaries)

```py
# Basic range loop
for i in range(5):
    print(i)

# Loop list
numbers = [1, 2, 3, 4, 5]
# for item in iterable:
for number in numbers:
    print(number)

# Inverted loop list: HOW TO BUILD IT?

# Loop dictionary
person = {name:"Mateus", age: 28, profession: "Software Engineer"}

for key, value in person.items():
    print(f"{key}: {value}")

# Loop array of dictionaries

# While loop
count = 0

while count < 5:
    print(count)
    count += 1
```

### Functions

```py
# function with default parameter
def greet(name="World"):
    return f"Hello, {name}!"

print(greet("Mateus")) # Hello, Mateus!
print(greet()) # Hello, World!
```

### Lists

- Python's arrays are dynamic and called **lists**

```py
numbers = [1,2,3]
numbers.append(4) # add element
numbers.remove(2) # remove element by value
print(numbers)

# List comprehesion
squared = [x**2 for x in range(5)]
print(squared) # [0, 1, 4, 9, 16]
```

### Dictionaries

- Key-value pairs, similar to objects in JS
- Differently from JS, where we can access object properties with dot notation, in Python we need to use bracket notation
- In Py, dot notation ised used to access attributes for objects, not dictionary keys. Meaning, if `person` were a class instance (object) with an attribute `name`, we'd be able to use dot notation.
- Dot notation: only for class instances, not normal objects

```py
person = {"name":"Matt", "age":28}
print(person["name"]) # in python, we can't access dictionary properties with dot notation `person.name`, as we would in JS

# In Python, dictionaries require the use of bracket notation `person["age"]`
```

### Tuples

- Immutable sequences

```py
point = (1,2)
print(point[0]) # 1

x, y = point
```

### Sets

- Unordered collections of unique elements

```py
# list -> []
# tuple -> ()
# set -> {}

unique_numbers = {1,2,3,3}
print(unique_numbers)
```
