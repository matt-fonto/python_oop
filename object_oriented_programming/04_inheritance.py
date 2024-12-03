import csv 

class Item:
    # class attributes
    discount = 0.8 
    all = [] 

    def __init__(self, item_name:str, price:int, is_available:bool, quantity=0):
        # validate
        assert price >= 0, f"Price {price} can't be a negative number."
        assert quantity >= 0, f"Quantity {quantity} can't be a negative number."

        # instance attributes
        self.item_name = item_name
        self.price = price
        self.is_available = is_available
        self.quantity = quantity

        # actions to execute
        Item.all.append(self) # add current object to list
    
    def give_info(self):
        return (
            f"{self.item_name} costs {self.price}. "
            f"It is currently {'available' if self.is_available else 'not available'}. "
            f"Quantity is: {self.quantity}"
        )
    
    def total_price(self):
        total_price = self.price * self.quantity
        return f"Total price is: {total_price}"
    
    def apply_discount(self):
        self.price *= self.discount
    
    @classmethod 
    def instantiate_from_csv(cls):
        with open('03_example.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            items = list(csv_reader)

        for item in items:
            Item(
                item_name=item.get('item_name'),
                price=float(item.get('price')),
                is_available=item.get('is_available'),
                quantity=float(item.get('quantity'))
            )    

    @staticmethod 
    def is_int(num):  
        if isinstance(num, float):
            return num.is_integer() # built-in method
        elif isinstance(num, int):
            return True
        return False

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.item_name}, price: {self.price}, is available?: {self.is_available}, quantity: {self.quantity} \n"

# inheriting. Item parent, Phone child
class Phone(Item):
    def __init__(self, item_name: str, price: int, is_available:bool, quantity=0, broken_phones=0):
        # call the parent class constructor with super
        super().__init__(item_name, price, is_available, quantity)
        assert broken_phones >= 0, f"Broken phones {broken_phones} can't be a negative number"
        self.broken_phones = broken_phones

item1 = Phone('item 1', 400, True, 3, 0)
print(item1.all)

phone1 = Phone('iphone 16', 1000, True, 10, 0)
print(phone1.item_name)
print(phone1.total_price())

print(phone1.all)