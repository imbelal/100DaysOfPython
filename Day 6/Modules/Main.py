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

net_price = Pricing.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)
