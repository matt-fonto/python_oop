# Collections

## Array methods Python

### 1. Adding elements

- append(item): add item to the end of the list
- extend(iterable): add multiple items from an iterable to the list
- insert(index, item): add item at specific index

```py
arr.append(4)
arr.extend([1,2,3])
arr.insert(2, 100)
```

### 2. Removing elements

- pop(index): remove and return the item at the specific index (last is the default)
- remove(item): remove the first occorrence of the item
- clear(): remove all elements from the list

```py
arr.pop() # removes last item
arr.pop(1) # removes item at index 1
arr.clear()
```

### 3. Searching

- index(item, start, end): return the index of the first occorrence of the item
- count(item): count occorrences of the item in the list

```py
arr.index(5)
arr.count(5)
```

### 4. Sorting and reversing

- sort(key=None, reverse=False): sort the list in place
- reverse(): reverses the list

```py
arr.sort() # asc
arr.sort(reverse=True) # des
arr.reverse()
```

### 5. Other useful methods

- copy(): create a shallow copy of the list
- len(arr): get the number of elements
- max(arr) || min (arr): get the largest or smallest element
- sum(arr): sum all numeric values
- list(iterable): converts iterable (range, tuple) to a list

```py
new_arr = arr.copu()
len(arr)
max(arr)
min(arr)
sum(arr)
arr = list(range(5))
```

### Slice operator

- We take a slice of a iterable and do something with it

```py
sliced = [start:stop:step] # similar to the range

[0:4:2] # start at index 0, go until index 4, step by 2
[:4] # start at 0, stop at 4
[2:] # start at 2, stop at end
[::-1] # reverse  a list
[::2] # step by two
```

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
