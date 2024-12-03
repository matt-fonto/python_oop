user_name = input('Name: ') # input: it will always return a string
# in case we want to grab numbers from the input function, we need to convert them

def say_hello(name:str):
    return f"Hello, {name}"

hello = 'hello'.count

print(say_hello(user_name))