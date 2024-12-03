people: list[str] = ['Susan', 'John', 'Mary']

people.append('Mario')
people.append('Mario')

copy_people = people.copy() # copy_people and people are different objects. So change in one, won't affect the other.

num_of_mario = people.count('Mario')

fruits: list[str] = ['Apple', 'Banana','Orange']
print(people) # without adding people

people.extend(fruits) # extend doesn't return a value. It modifies the original list

# print(num_of_mario)
# print(people)

location_john = people.index('John')
# print(location_john)

people.insert(1, 'Obama') # insert(index, value)
# print(people)

removed_element_at_beginning = people.pop(0)
# print(removed_element_at_beginning)
# print(people)

people.remove('John') # differently from pop, remove doesn't return a value
print(people)

people.sort()
print(people)
