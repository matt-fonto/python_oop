# list comprehension: we define a for loop inside the iterable
# List = [expression(i) for i in another_list if filter(i)]

# num % 2 == 0: even numbers
# num % 2 != 0: odd numbers

lst = [x for x in range(1,11) if x % 2 != 0]
print(lst)