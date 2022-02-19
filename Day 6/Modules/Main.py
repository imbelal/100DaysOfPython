# Introduction to Python modules
# A module is a piece of software that has a specific functionality. A Python module is a file that contains Python code.
# For example, when building a shopping cart application, you can have one module for calculating prices
# and another module for managing items in the cart. Each module is a separate Python source code file.
# A module has a name specified by the filename without the .py extension. For example,
# if you have a file called pricing.py, the module name is pricing

import Pricing

# import Pricing as selling_pricing # we can also rename the module

# from Pricing import * # import everything from Pricing module

# from Pricing import get_net_price # import single method only

# from Pricing import get_net_price, get_tax # import multiple methods

# Python will search for the Pricing.py file from the following sources:
# The current folder from which the program executes.
# A list of folders specified in the PYTHONPATH environment variable, if you set it before.
# An installation-dependent list of folders that you configured when you installed Python.
# Python stores the resulting search path in the sys.path variable that comes from the sys module.
# Modifying the Python module search path at runtime
# Python allows you to modify the module search path at runtime by modifying the sys.path variable.
# This allows you to store module files in any folder of your choice.
# sys.path.append('d:\\modules\\')

net_price = Pricing.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)
