# Basic lambda
# variable = lambda param: operation
# It's optional to save the lambda into a variable

def squared(num): return num * num # => normal function, one-line function

squared_lambda = lambda num: num * num
add_two = lambda num: num + 2
sum = lambda a,b: a + b

# Lambda func is normally used inside another function

def func_builder(x):
    return lambda num: num + x

add_ten = func_builder(10) # we are build the structure of add_ten, which we can then call after
add_twenty = func_builder(20)

add_ten(4) # 10 + 4 = 14
add_twenty(8) # 20 + 8 = 28

# Higher order function 
# - A function that takes one or more functions as arguments

from functools import reduce

numbers = [1,2,3,4,5]

total_sum = reduce(lambda acc, curr: acc + curr, numbers)
total_multiplication = reduce(lambda acc, curr: acc * curr, numbers)

print(f"total sum: {total_sum}")
print(f"total multiplication: {total_multiplication}")