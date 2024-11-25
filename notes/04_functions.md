# Functions

- Blocks of reusable code that perform specific tasks
- Functions accept parameters to customize their behavior

```py
def func_name(parameters):
    return value
```

## Function parameters

- In Python, there are different ways to handle parameters

1. Positional arguments: Simplest form, values are assigned based on their position
2. Default arguments: Provide default values for parameters. If no value is passed, default is used
3. Keyword arguments: Explicitly specify param name when calling the function. Order doesn't matter
4. Arbitrary arguments (`*args`): Accept a non-specific number of positional arguments. They are packed into a tuple
5. Arbitrary keyword arguments (`**kwargs`): Accept a non-specific number of keyword arguments. The arguments are packed into a dictionary.

```py
# positional argument: values assigned from position
def sum(a,b):
    return a + b

sum(2,4) # 6

# default argument: if no value is passed, default is used
def greet(name="World")
    return f"Hello, {name}!"

greet()
greet("Mateus")

# keyword argument: specify parameters when calling function
def introduce(name, age):
    return f"Hi! My name is {name} and I'm {age} years old."

# order doesn't matter
introduce(name='Mateus', age='28')
introduce(age='28', name='Mateus')


# arbitrary arguments *arg: accept variable number of positional arguments
def sum_all(*args):
    return sum(args)

sum_all(1,2,3,4,5)

# arbitrary keyword arguments **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_info(name='Mateus', age='28', country="Austria")
```

## Unpack arguments

- Allows us to pass multiple elements as arguments to a function using `*` or `**` operators

```py
x = [1,2,4,5]
print(*x) # unpacking x
```

## Anonymous functions (lambda)

- Short, one-line functions with no name
- Need `lambda` keyword
- Commonly used as anonymous functions inside another function

```py
func_name = lambda expression

square = lambda x: x * x
is_even = lambda x: x % 2 == 0

x = lambda a, b: a + b
z = lambda a, b, c: a + b * c
```

### Map and filter

- Lambdas are commonly used with these functions

```py
num_array = [1,2,3,4,5,6,7]

# map(lambda: expression, array)
# map(func, array)
my_map = map(lambda item: item + 2, num_array)

# filter(lambda: expression, array)
# filter(func, array)
filtered_map = map(lambda item: item % 2 == 0, num_array)

```

## Scope & Globals

- Scope: region of a program where a variable is accessible
- Globals: variables that are defined at the module level and can be accessed throughout the file

### Scope

- Python scoping model: LEGB
- L: Local - variables inside a function
  - Variables defined within a function are local to that function and can't be accessed ouside of it
- E: Enclosing - variables in the enclosing (non-global) scope of a nested function
  - A variable in an outer function can be accessed by an inner function, but it can't be modified directly unless we use `nonlocal`
- G: Global - variables defined at the top level of the module
  - Variables defined at the top level or a script are in the global scope and can be accessed anywhere in the module
  - To modify a global variable inside a function, we must declare it explicitly using the `global` keyword
- B: Built-in - predefined names in Python (`len`, `print`)

```py
x = 'global'

def outer():
    y = 'enclosing'

    def inner():
        z = 'local'
        print(x) # access global
        print(y) # access enclosing
        print(z) # access local

    inner()

outer()
```

#### Local scope

```py
def example():
    x = 10 # local to the function
    print(x)

example()
# print(x) # Error: x isn't defined
```

### Enclosing scope

- To modify a variable in enclosing scope, we use `nonlocal` keyword

```py
def outer():
    y = 10 # enclosing scope

    def inner():
        print(y) # access enclosing scope

    inner()

outer()

# Modifying enclosing variable
def outer():
    y = 10

    def inner():
        nonlocal y
        y += 5  # modify the enclosing variable
        print(y)

    inner()
    print(y)

outer()
```

### Global scope

- To modify a variable in global scope, we use `global` keyword
- It's not a good practice to use this

```py
x = 'global'

def example():
    print(x) # access global variable

example() # works
print(x)  # works

# Modifying global variables
def modify_global():
    global x # to modify the global variable we need to use the `global` keyword
    x = 20

modify_global()
print(x) # 20
```
