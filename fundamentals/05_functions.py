def check_items_list_even(list):
    new_list = []
    for item in list:
        if item % 2 == 0:
            new_list.append('Even')
        else:
            new_list.append('Odd')
    return new_list

lst = [1,2,3,4,5,6,7,8,9]

print(check_items_list_even(lst))

lst_comprehension = ['Even' if item % 2 == 0 else 'Odd' for item in lst]
print(lst_comprehension)

# lambda

square = lambda num: num * num
print(square(4)) # 16

numbers = [1,2,3]
# used in higher-order functions
squared = list(map(lambda item: item * item, numbers))
print(squared)