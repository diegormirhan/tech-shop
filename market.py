import time
from typing import List, Dict
from time import sleep
from models.product import Produto
from utils.helper import formata_float_str_moeda

products: List[Produto] = []
cart: List[Dict[Produto, int]] = []


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
    pass


def list_products() -> None:
    pass


def buy_product() -> None:
    pass


def view_cart() -> None:
    pass


def close_order() -> None:
    pass


def get_product_by_code(code: int) -> None:
    pass


def main() -> None:
    menu()


if __name__ == '__main__':
    main()
