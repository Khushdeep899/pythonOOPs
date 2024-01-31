from item import Item
from keyboard import Keyboard

# Load items from CSV
Item.instantiate_from_csv()

# Apply discount to items
for item in Item.all:
    item.apply_discount()

# Plot inventory stock
Item.plot_stock()

# Access and modify item properties
item = Item.all[0]
print(item.price)
item.name = "NewName"


# Create a Keyboard instance
keyboard1 = Keyboard("Gaming Keyboard", 150, 3, "Red")

# Apply a discount
keyboard1.apply_discount()

# Change the color of the keyboard
keyboard1.change_color("Blue")

# Display the details of the keyboard
print(keyboard1)
