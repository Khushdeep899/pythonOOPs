import csv
import logging
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(filename='inventory.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Validation for the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Add to the list of all items
        Item.all.append(self)
        logging.info(f"New item created: {self}")

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        try:
            self.__price = self.__price * self.pay_rate
            logging.info(f"Discount applied to {self.name}, new price: {self.__price}")
        except Exception as e:
            logging.error(f"Error applying discount: {e}")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @staticmethod
    def plot_stock():
        labels = [item.name for item in Item.all]
        quantities = [item.quantity for item in Item.all]

        plt.bar(labels, quantities)
        plt.xlabel('Items')
        plt.ylabel('Quantity')
        plt.title('Stock of Inventory Items')
        plt.show()

    def __repr__(self):
        return f"Item('{self.name}', {self.__price}, {self.quantity})"


# Usage example:
# item = Item("TestItem", 9.99, 5)
# item.send_email("smtp.example.com", 587, "username", "password", "recipient@example.com")




# print(Item.is_integer(7.0))


# item1 = Item("Phone", 100, 1)  # creating instace of class

# print(Item.all) # return represtation given by __repr__() method

# to print all instances using Item.all separately by looping though
# for instance in Item.all:
#     print(instance.name)
# print(Item.__dict__) # bult in magic attribute, this will bring all the attributes that are belonging that are belonging to the object(represented as a dictionary)
# print(item1.__dict__)

# (type(item1)) # item or <class '__main__.Item'>
# (type(item1.name)) #str
# (type(item1.price)) # int
# (type(item1.quantity)) # int


# Static vs Class methods:

"""
Class Methods

Class Method: Defined with the @classmethod decorator.
First Argument: The first argument to a class method is the class itself, typically named cls.
Use Case: Used when you need to do something with the class itself, like creating factory methods that instantiate instances of the class using different sets of parameters.
Can Modify Class State: Since they receive the class as the first argument, class methods can modify the class state that applies across all instances of the class.

Example of a class method:

class MyClass:
    @classmethod
    def class_method(cls):
        print(f"This is a class method. {cls}")

Static Methods
Static Method: Defined with the @staticmethod decorator.
No Implicit First Argument: Static methods do not take an implicit first argument; they behave like plain functions but belong to the class's namespace.
Use Case: Used when you need to perform some operation that's related to the class, but doesn't need to modify class or instance state. They are utility methods that could logically be part of the class but could also stand alone.
Cannot Modify Class or Instance State: Static methods do not have access to the cls or self keywords, so they cannot modify state. They work like regular functions but are included in the class's body to have a logical grouping.

Example of a static method:

class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

When to Use Each
Use a class method when you need access to the class object to call other class methods or constructors, or to modify class attributes.
Use a static method when the method does not access or modify the class or instance state and could logically be a standalone function, but you want to include it in the class for organizational purposes.
"""
