# here inventory is a package that contains another subpackage product, which contains products module
from inventory.product import products

# here sales is a package that contains another subpackage order, which contains orders module
from sales.order import orders

# accessing default tax rate from init file of sales package
from sales import tax_rate


def get_bill_for_current_orders():
    # now printing all orders with total price
    all_orders = orders.get_all_orders()
    all_products = products.get_all_products()
    total = 0.0

    for ord in all_orders:
        subTotal = 0.0
        print()
        print(f'order no :{ord["id"]}     ')

        for orderedProduct in ord['products']:
            for prod in all_products:
                if(orderedProduct['productId'] == prod['id']):

                    priceBeforeTax = orderedProduct["quantity"] * prod["price"]
                    priceAfterTax = priceBeforeTax + \
                        priceBeforeTax * (tax_rate / 100)
                    subTotal += priceAfterTax

                    print(
                        f'product:  {prod["name"]}  Quantity: {orderedProduct["quantity"]}  Price: {priceAfterTax}')

        total += subTotal
        print(f'Sub-total:  {subTotal}')

    print()
    print(f'Total:  {total}')
