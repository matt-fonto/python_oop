## Array/List methods Python

The methods are:

- Adding:

  - append: adds end of the list
  - extend: adds all elements from iterable to list
  - insert: inserts at specified index:

- Removing

  - pop: removes and returns element at index. Default last.
  - clear: removes all elements
  - remove: removes first occurence item

- Finding

  - index: returns index of the first occorrence of `item`. Raises `ValueError` if no `item` is found
  - count: returns number of occurrences of `item`

- Sorting & Reversing

  - sort: sorts the list in place
  - reverse: reverses the list

- Miscellaneous
  - copy: returns shallow copy of the list
  - len: not a method, but very common. Returns the number of elements in the list

#### Quick tip on shift and unshift

- In JS, we have the methods, shift and unshift.
  - Shift: Removes item at the beginning (position 0) and returns it
  - Unshift: Adds N items at the beginning (position 0) of the array
- In Python, we could use :
  - pop(0) as the equivalent of shift
  - insert(0, value) as the equivalent of unshift

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
