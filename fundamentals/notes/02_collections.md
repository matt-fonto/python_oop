# Collections

## Arrays

- Collection of indexed items
- Accepts repeatable values, differently from set
- Operations on it usually are O(n)

## Sets

- Unordered collection of unique elements
- We only care if something is there or not
- Set is extremely fast for lookups, additions and removals

```py
x = set() # creating an empty set
s = {} # this actually creates a dictionary. If you populate, then it's ok
s = {4, 32, 4, 2} # creating a populated set

s.add()
s.remove()
print(33 in s) # O(1) -> constant time, instead of O(n), which would be a in list
```

## Dictionaries: hash table, map, object

- Uses a hash, so it's very fast.

```py
x = {'key': value}
x['key2'] = another_value
```

### Dictionary methods

```py
print(person["name"]) # use it when we're sure the certain key exists
print(person.get('name')) # use it when unsure if certain key exists. safe retrieve. If key doesn't exist, doesn't throw error as the bracket notation would, and returns None

person.keys() # get all dict keys
person.values() # get all dict values
person.items() # get all key:value pair as a tuple
person.update() # updates values and overrides the previous ones
person.pop(key) # removes and returns the value of the specified key

del person['key'] # removes the key from the dict
```

### Loop over dictionary

```py
for key, value in our_dict.items():
    print(key, value)
```

## Comprehensions

```py
# list comprehension: we define a for loop inside the iterable
# List = [expression(i) for i in another_list if filter(i)]
x = [x for x in range(5)]

# num % 2 == 0: even numbers
# num % 2 != 0: odd numbers

lst = [x for x in range(1,11) if x % 2 != 0]
print(lst)
```
