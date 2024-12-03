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
        self.price = price
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
        self._item_name = value
    
    # instance method
    # method is dependent on both instance and class
    def give_info(self):
        availability = "available" if self.is_available else "not available"

        return (
            f"{self._item_name} costs {self.price}. "
            f"It is currently {availability}. "
            f"Quantity is: {self.quantity}"
        )
    
    def total_price(self):
      return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.discount

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
                _item_name=item.get('item_name'),
                price=float(item.get('price')),
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
        return f"{self.__class__.__name__}: {self._item_name}, price: {self.price}, is available: {self.is_available}, quantity: {self.quantity} \n"
        
    
    



        