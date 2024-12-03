from typing import Literal
from item import Item

class Phone(Item):
    def __init__(self, item_name:str, price:float, is_available:bool, quantity=0, os:Literal['android', 'ios'] = 'ios'):
        super().__init__(item_name, price, is_available, quantity)

        self.os = os

    def give_info(self):
        parent_info = super().give_info() # call the base functionality from the parent

        # extend the functionality 
        return f"{parent_info}. It's a phone. OS: {self.os}"

