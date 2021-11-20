import time
from typing import List, Dict
from time import sleep
from models.product import Produto
from utils.helper import formata_float_str_moeda as formata

products_list: List[Produto] = []
products_cart: List[Dict[Produto, int]] = []


def menu() -> None:
    print('====================================\n'
          '============ Welcome ===============\n'
          '=========== Tech Shop ==============\n'
          '====================================\n')

    print('Select one of the options below:\n'
          '1 -> Register Product\n'
          '2 -> List Product\n'
          '3 -> Buy Product\n'
          '4 -> View Cart\n'
          '5 -> Close Order\n'
          '6 -> Close System\n'
          '-----------------')

    option: int = int(input('--> '))

    if option == 1:
        register_product()
    elif option == 2:
        list_products()
    elif option == 3:
        buy_product()
    elif option == 4:
        view_cart()
    elif option == 5:
        close_order()
    elif option == 6:
        exit()
    else:
        print('Unrecognized command... Returning to menu')
        time.sleep(2)
        menu()


def register_product() -> None:
    print('========= Register Product =========\n'
          '====================================')

    product_name: str = input('Enter the product name: ')
    product_price: float = float(input('Enter the product price: '))

    product: Produto = Produto(product_name, product_price)
    products_list.append(product)

    time.sleep(1)
    print(f'The product {product.name} has been succesfully registered!\n')

    time.sleep(2)
    menu()


def list_products() -> None:
    if len(products_list) > 0:
        print('========== List Products ===========\n'
              '====================================')

        for products in products_list:
            print(products)
            time.sleep(1)
    else:
        print("There're no registered products!")

    time.sleep(2)
    menu()


def buy_product() -> None:
    pass


def view_cart() -> None:
    pass


def close_order() -> None:
    if len(products_cart) > 0:
        amount: float = 0

        print('========== Cart Products ===========\n'
              '====================================')

        for item in products_cart:
            for data in item.items():
                print(f'{data[0]} -> Quantity: {data[1]}\n')
                amount += data[0].price * data[1]
                time.sleep(1)
        print(f"Your bill's {formata(amount)}")
        products_cart.clear()
        sleep(3)
    else:
        print("There're no products in the cart!")

    time.sleep(2)
    menu()


def get_product_by_code(code: int) -> None:
    p: Produto = None

    for product in products_list:
        if product.code == code:
            p = product
    return p


def main() -> None:
    menu()


if __name__ == '__main__':
    main()
