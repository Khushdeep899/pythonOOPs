import logging

from item import Item

class Keyboard(Item):
    pay_rate = 0.7  # Different pay rate for keyboards

    def __init__(self, name: str, price: float, quantity=0, color='Black'):
        self.color = color  # Set color before calling super().__init__
        # Call to the super function to access all attributes/methods from the parent Item class
        super().__init__(name, price, quantity)



    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity}, '{self.color}')"

    # Example of an additional method specific to Keyboard
    def change_color(self, new_color):
        self.color = new_color
        logging.info(f"Color changed for {self.name} to {self.color}")
