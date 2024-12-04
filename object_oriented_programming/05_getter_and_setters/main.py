from item import Item
from phone import Phone
# from file import module

item1 = Item('my item', 500, True, 10)
print(item1.item_name) # Now, the __item_name is not accessible in the instance class

item1.item_name = 'Changed'
print(item1.item_name) # changed through the setter
