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
    
    # this method shouldn't be called from an instance because it instantiates the instance. 
    # Instead, it should be a `Class method`
    # this method, since it's a class method, it won't take the self -- meaning the instance itself. 
    @classmethod # this decorator tells python this is a class method
    def instantiate_from_csv(cls): # cls: class reference is passed as argument
        with open('03_example.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            items = list(csv_reader)

        for item in items:
            Item(
                item_name=item.get('item_name'),
                price=float(item.get('price')), # convert to float
                is_available=item.get('is_available'),
                quantity=float(item.get('quantity'))
            )    

    # static method: doesn't take any parameter
    @staticmethod 
    def is_int(num):  
        if isinstance(num, float):
            return num.is_integer() # built-in method
        elif isinstance(num, int):
            return True
        return False

    def __repr__(self):
        return f"Item: {self.item_name}, price: {self.price}, is available?: {self.is_available}, quantity: {self.quantity} \n"

# Item.instantiate_from_csv() # should be able to instantiate our item
# print(Item.all)

print(Item.is_int(3.0))
