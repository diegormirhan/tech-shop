## Description
**Tech Shop Management System**

This GitHub repository contains a Python script for a simple Tech Shop management system. The script utilizes command-line interaction to perform various tasks related to product registration, listing, purchasing, and order management. The system is organized into different functions to handle different aspects of the shop's operations.

**Features:**
- Register new products with names and prices.
- List all registered products.
- Purchase products and add them to the cart.
- View the products currently in the cart.
- Close the current order, calculating and displaying the total bill.
- Gracefully exit the system.

**How to Use:**
1. Run the script in a Python environment.
2. The main menu will be displayed with numbered options.
3. Choose from the options to perform different tasks such as registering products, listing products, buying products, viewing the cart, closing the order, and exiting the system.
4. Follow the prompts and input the necessary information based on the chosen action.

**Key Components:**
- `models.product.Produto`: This module defines the `Produto` class, representing a product with attributes like name, price, and code.
- `utils.helper.formata_float_str_moeda`: A utility function to format a floating-point value as a currency string.
- `products_list`: A list to store registered products.
- `products_cart`: A list of dictionaries to store products and their quantities in the cart.

The script is intended for educational purposes and provides a basic example of managing a shop's inventory and orders through the command line. It showcases concepts such as user input, data structures, loops, and modular programming. Users can explore, run, and modify the code according to their needs.

<br />


---

## License

MIT License

Copyright (c) 2022 Diego R. Mirhan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<br />


---

## Author Info

- LinkedIn - [@diegomirhan](https://www.linkedin.com/in/diegomirhan/)

<br />

[Back To The Top](#bank-app-with-python)
