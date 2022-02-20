'''
    A Python package contains one or more modules. Python uses the folders and files structure to manage packages and modules.
    Use the __init__.py file if you want to initialize the package-level data.
    Use __all__ variable to specify the modules that will load automatically when importing the package.
    A package may contain subpackages.

    Today we will understand package, subpackage, module using a real world application example.
    It will be a small console application where we will able to show billing details based on order details.
    
    Folder structure will be as follows:

   Root
    |-------inventory
    |           |-----product
    |           |        |-----products.py
    |           |-----__init__.py
    |--------sales
    |          |------billing
    |          |         |------bills.py
    |          |------order
    |          |        |-------orders.py
    |          |------__init.py
    |
    |--------main.py

'''

# here inventory is a package that contains another subpackage product, which contains products module
from inventory.product import products

# here sales is a package that contains another subpackage order, which contains orders module
from sales.order import orders

# here sales is a package that contains another subpackage billing, which contains bills module
from sales.billing import bills

# printing all products
print(products.get_all_products())

# printing all orders
print(orders.get_all_orders())

# printing bill details
print(bills.get_bill_for_current_orders())
