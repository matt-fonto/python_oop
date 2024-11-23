# Array methods Python

## 1. Adding elements

- append(item): add item to the end of the list
- extend(iterable): add multiple items from an iterable to the list
- insert(index, item): add item at specific index

```py
arr.append(4)
arr.extend([1,2,3])
arr.insert(2, 100)
```

## 2. Removing elements

- pop(index): remove and return the item at the specific index (last is the default)
- remove(item): remove the first occorrence of the item
- clear(): remove all elements from the list

```py
arr.pop() # removes last item
arr.pop(1) # removes item at index 1
arr.clear()
```

## 3. Searching

- index(item, start, end): return the index of the first occorrence of the item
- count(item): count occorrences of the item in the list

```py
arr.index(5)
arr.count(5)
```

## 4. Sorting and reversing

- sort(key=None, reverse=False): sort the list in place
- reverse(): reverses the list

```py
arr.sort() # asc
arr.sort(reverse=True) # des
arr.reverse()
```

## 5. Other useful methods

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
