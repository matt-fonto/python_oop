# Getters and Setters

- getters and setters allow controlled access to instance attributes
- They help enforce encapsulation, this way attributes are not directly modified or accessed in unintended ways

```py
# get: @property => makes the attribute read only
# set: @<property_name>.setter

class Item:
    def __init__(self, price):
        self._price = price # use a private-like attribute (prepend the name with `_`)

    #get
    @property
    def price(self):
        return self._price

    #set
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

item = Item(100)
print(item.price) # getter is called

item.price = 200 # setter is called
```

- To completely prevent the access to the `_` naming instance attributes from the outside, we should use double underscore `__`. This way, we prevent the access from outside the class
- But double underscore cause `name mangling`, so you should avoid it. Preferably use only a single underscore
