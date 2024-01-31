from item import Item
import logging

class Phone(Item):
    pay_rate = 0.9  # Different pay rate for phones

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to the super function to access all attributes/methods from the parent Item class
        super().__init__(name, price, quantity)

        # Validate broken_phones
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # New attribute specific to Phone
        self.broken_phones = broken_phones

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.broken_phones})"

    # Example of an additional method specific to Phone
    def report_broken_phones(self, number):
        self.broken_phones += number
        logging.info(f"{number} broken phones reported for {self.name}. Total broken phones: {self.broken_phones}")
