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

## Lambda & Higher order functions

- Lambda functions are anonymous, but we can assign them to a variable
- Lambda func is normally used inside another function
- Lambda takes N params and returns operation

```py
# variable = lambda param: operation
# It's optional to save the lambda into a variable
def squared(num): return num * num # => normal function, one-line function

squared_lambda = lambda num: num * num
add_two = lambda num: num + 2
sum = lambda a,b: a + b
```

### Higher order functions (HOF)

- Functions that either/both:

1. Take other functions as arguments
2. Return a function as their result

- Benefits of HOF

1. Reusability: functions can be reused in different contexts by passing different callbacks
2. Abstraction: abstracts away details of operation
3. Functional programming: allows functional programming patterns, such as composition and chaining

- Important built-in higher-order functions:

1. `map`: applies a function to each array item
2. `filter`: filters elements based on a condition
3. `reduce`: aggregates elements based on a reducer function

- Higher order functions take a callback function, which can be a lambda function
- In Python, we can't directly declare the function inside the map, as we'd in JS
- So, in Python, we either declare it outside and reference it inside the HOF or we use the lambda

```js
// This is okay in JS
const doubled = numbers.map(function (num) {
  return num * 2;
});
```

```py
def double(num):
    return num * 2

# they are equal
doubled = map(double, numbers)
doubled = map(lambda num: num * 2, numbers)
```

```py
# Function as argument
def apply_operation(a, b, operation):
    return operation(a, b)

sum = lambda x, y: x + y
multiply = lambda x, y: x * y

# Function as return value
def create_multiplier(multiplier):
    return lambda num: num * multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

double(5) # 10
triple(5) # 15

# Built-in HOF
numbers = [1,2,3,4,5]

# map(func, array) => returns a map object. To see the results as list, we normally convert it to a list with `list(map())`
# Instead of having a loop, we simply use map
doubled = list(map(lambda num: num * 2, numbers))

def get_double(arr):
    # loop
    result = []
    for item in arr:
        result.append(item * 2)
    return result

    # list comprehension
    return [item * 2 for item in arr]


doubled_with_loop = get_double(numbers)

evens = filter(lambda num: num % 2 == 0, numbers)
sum = numbers.reduce(lambda acc, num: acc + num, 0, numbers)

from functools import reduce

# Even though we can use reduce to get the total, Python has a `sum(arr)` function, which does the same
# reduce(func, arr, starting_num<optional>)
total = reduce(lambda acc, curr: acc + cur, numbers)
total_two = sum(numbers)
```
