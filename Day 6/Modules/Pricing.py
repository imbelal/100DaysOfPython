# pricing.py

def get_net_price(price, tax_rate, discount=0):
    return price * (1 + tax_rate) * (1-discount)


def get_tax(price, tax_rate=0):
    return price * tax_rate


# Python __name__ variable example
# When you run the script directly, Python sets the __name__ variable to '__main__'
# However, if you import a file as a module, Python sets the module name to the __name__ variable.
print(__name__)
