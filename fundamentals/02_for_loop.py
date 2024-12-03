# Loop list
numbers = [1, 2, 3, 4, 5]
# for item in iterable:
# directly iterates over the elements, not the index
# each number refers to an element in the list
# useful when we need only the value
for number in numbers:
    print(number)

# for i in range(len(iterable))
# go through the indeces [0, 1, 2, 3, ...]
# access each elements via its index numbers[i]
# useful when we need both the value and the index
for i in range(len(numbers)):
    print(numbers[i])

# other way to achieve this is to use enumberate
# for i, value in enumarate(iterable)
for i, element in enumerate(numbers):
    print(i, element)

