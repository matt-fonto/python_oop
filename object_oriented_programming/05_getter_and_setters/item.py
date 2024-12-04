import csv
import os

class Item:
    # class attributes
    discount = 0.8 
    all = [] 

    def __init__(self, item_name:str, price:int, is_available:bool, quantity=0):
        # Run validations
        assert price >= 0, f"Price {price} can't be a negative number."
        assert quantity >= 0, f"Quantity {quantity} can't be a negative number."

        # Assign params to instance 
        # instance attributes
        self._item_name = item_name # read-only attribute
        self._price = price
        self.is_available = is_available
        self.quantity = quantity

        # actions to execute
        Item.all.append(self) # every time we init, we append the items to the list of items
    
    # item.read_only_name
    # if we try to change this to something else, Python will complain
    # @property # this becomes a property we can access
    # def read_only_name(self):
    #     return self._item_name
    
    @property
    def item_name(self):
        return self._item_name
    
    @item_name.setter
    def item_name(self, value):
        if len(value) < 3:
            raise Exception("Too short")
        elif len(value) > 10:
            raise Exception("Too long")
        else:
            self._item_name = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        self._price = value
    
    def apply_discount(self):
        # use setter
        self.price *= self.discount

    def apply_increment(self, value):
       self.price += value # python doesn't accept assignment on the return
       return self.price

    # instance method
    # method is dependent on both instance and class
    def give_info(self):
        availability = "available" if self.is_available else "not available"

        return (
            # we use self.item_name because we use the getter, removing the need of _item_name. Same thing with the price
            f"{self.item_name} costs {self.price}. "
            f"It is currently {availability}. "
            f"Quantity is: {self.quantity}"
        )
    
    def total_price(self):
      return self.price * self.quantity

    # class-level data
    # bound to the class, not the object
    # param `cls` points to the class, not the instance
    # can modify or use class-level data (like class variables)
    # can be called on the class itself, not just an instance
    # method is indepedent from the instance
    @classmethod 
    def instantiate_from_csv(cls) -> None:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'items.csv')

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(
                item_name=item.get('item_name'), # use setter 
                price=float(item.get('price')), # use setter
                is_available=item.get('is_available') == 'True',
                quantity=int(item.get('quantity')))
    
    # doesn't take either a self, nor cls
    # doesn't rely on the class or instance
    # acts like a regular function inside the class - grouped logically
    # method is independent from the class/instance
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__}: {self.item_name}, price: {self.price}, is available: {self.is_available}, quantity: {self.quantity} \n"
        
    
    



        