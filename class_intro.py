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
    discount = 0.8 # class attribute

    # __init__: initializes the class with the parameters we passed. init is also called constructor
    # the constructor is executed during the class instantiation
    # it's possible to describe the type of argument that we accept in our methods/functions
    def __init__(self, item_name:str, price:int, is_available:bool, quantity=0):
        # Run validations to received arguments: we catch possible bugs before going further in the program
        assert price >= 0, f"Price {price} needs to be greater than 0."
        assert quantity >= 0, f"Quantity {quantity} needs to be greater than 0."

        # print(f'An instance of "{item_name}" was created')
        # we dynamically assign the passed arguments to the instantiated class attribute
        # Attribute assignment in the constructor
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
    
    def apply_discount(self):
                    # discount: class attribute.
                    # when we call `self`, it will look at the instance level first
                    # if it can't find it, it goes to the class level
                    # so a best practice is to write `self.class_attribute` instead of `Class.class_attribute`
        self.price *= self.discount



# 2. Instantiate an object
phone = Item('phone',1000, True, 10) # these arguments are passed to the init method
tv = Item('tv',5000, True, 2)

# print(phone.total_price())
# print(tv.total_price())

""" 
 Just because we use `Attribute assignment` in the constructor,
 it doesn't mean that we can't add further attributes to each specific object.

 We can add more attributes after the object is instantiated
""" 

phone.is_ios = True
phone.has_front_camera = True

tv.is_lcd = True
tv.is_smart = True

# print(phone.is_ios)
# print(phone.has_front_camera)

# print(tv.is_lcd) 
# print(tv.is_smart) 

# print(phone.price)
# phone.apply_discount() # 0.8
# print(phone.price)

## we can override class attributes with instance attributes

print(tv.price)
tv.discount = 0.5 # overrode the class discount
tv.apply_discount()
print(tv.price)