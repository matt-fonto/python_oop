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
