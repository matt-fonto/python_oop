# In Python, each data type is an object instantiated from a class

item1 = 'Phone'
item1_is_available = False
item1_price = 1000

# print(type(item1))
# print(type(item1_is_available))
# print(type(item1_price))

""" Output
<class 'str'>
<class 'bool'>
<class 'int'>
 """

# 1. Create class
class Item:
    # __init__: initializes the class with the parameters we passed. init is also called constructor
    def __init__(self, item_name, price, is_available, quantity):
        self.item_name = item_name
        self.price = price
        self.is_available = is_available
        self.quantity = quantity
    

    def give_info(self):
        # self: passes the object itself to the method
        # all methods will take a `self`
        return (
            f"{self.item_name} costs {self.price}. "
            f"It is currently {'available' if self.is_available else 'not available'}. "
            f"Quantity is: {self.quantity}"
        )
    
    def total_price(self):
        total_price = self.price * self.quantity
        return f"Total price is: {total_price}"

# 2. Instantiate an object
phone = Item('phone',1000, True, 8) # these arguments are passed to the init method
tv = Item('tv',5000, True, 2)

print(phone.total_price())
print(tv.total_price())
