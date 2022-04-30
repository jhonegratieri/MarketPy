from typing import List, Dict, Optional
from time import sleep

from models.products import Product
from utils.helpper import float_to_str_coin

products: List[Product] = []
shopping_cart: List[Dict[Product, int]] = []


def menu() -> None:
    print('', 50 * '=', '  WELCOME TO PYSHOP  '.center(50, '='), 50 * '=', sep='\n')
    print('Select an option below:',
          '1 - Register product',
          '2 - List product',
          '3 - Buy product',
          '4 - View shopping cart',
          '5 - Finalize order',
          '6 - Exit to system', sep='\n'
          )

    try:
        option: int = int(input())
    except ValueError:
        print('Invalid option. Try again.')
        menu()

    match option:
        case 1:
            register_product()
        case 2:
            list_product()
        case 3:
            buy_product()
        case 4:
            view_shopping_cart()
        case 5:
            finalize_order()
        case 6:
            print('Thank you and come back often.')
            sleep(1)
            exit(0)
        case _:
            print('Invalid option!')
            sleep(1)
            menu()


def main() -> None:
    menu()


def register_product() -> None:
    print('  Product registration  '.center(50, '='))

    name: str = input('Enter the product name: ')

    try:
        price: float = float(input('Enter a product price: '))
    except ValueError:
        print(f'ERROR: Use only numbers for price.')
        menu()

    product: Product = Product(name=name, price=price)
    products.append(product)

    print(f'The product {product.name} has been registered successfully.')

    sleep(1)
    menu()


def list_product() -> None:
    if len(products) > 0:
        print('  Product listing  '.center(50, '='))
        for product in products:
            print(product)
            print(50 * '-')
    else:
        print('There are no registered products yet.')

    sleep(1)
    menu()


def buy_product() -> None:
    if len(products) > 0:
        print('  Available products  '.center(50, '='))

        for product in products:
            print(product)
            print(50 * '-')

        code: int = int(input('Enter the code of the product you want to add to the cart: '))
        product: Product = get_product(code)

        if product:
            if len(shopping_cart) > 0:
                have_in_cart: bool = False
                for item in shopping_cart:
                    quant: int = item.get(product)
                    if quant:
                        item[product] = quant + 1
                        print(f'The product {product.name} has {quant + 1} units in the cart.')
                        have_in_cart = True
                        sleep(1)
                        menu()

                if not have_in_cart:
                    prod = {product: 1}
                    shopping_cart.append(prod)
                    print(f'The {product.name} has been added to the cart.')
            else:
                shopping_cart.append({product: 1})
                print(f'The product {product.name} has been added to the cart.')
        else:
            print('This code does not exist. Please, Try again.')
    else:
        print('There are no products available for sale yet.')

    sleep(1)
    menu()


def view_shopping_cart() -> None:
    if len(shopping_cart) > 0:
        print('  Products in cart  '.center(50, "="))

        for item in shopping_cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print(50 * '-')
    else:
        print('There are no products available for sale yet.')

    sleep(1)
    menu()


def finalize_order() -> None:
    if len(shopping_cart) > 0:
        total_value: float = 0

        print('Products in the shopping cart'.center(50, '='))
        for item in shopping_cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print(50 * '-')
                total_value += data[0].price * data[1]

        sleep(1)
        print()
        print(f'Your total bill is {float_to_str_coin(total_value)}.')
        print('Check back often!')

        shopping_cart.clear()
        sleep(2)
    else:
        print('There are no products in the cart yet.')
        sleep(2)
        menu()


def get_product(code: int) -> Optional[Product]:
    product1: Product = None
    for product in products:
        if code == product.code:
            product1 = product
    return product1


if __name__ == '__main__':
    main()
