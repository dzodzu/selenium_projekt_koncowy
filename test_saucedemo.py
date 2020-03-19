#-*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.product_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from ddt import ddt, data, unpack
import csv
import time

def get_data(file_name):
    rows = []
    data_file = open(file_name, "rb")
    reader = csv.reader(data_file)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows

@ddt
class SauceDemoOrder(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/index.html")

    def tearDown(self):
        self.driver.quit()

    def test_correct_order(self):

        login_page = LoginPage(self.driver)
        login_page.input_username("standard_user")
        login_page.input_password("secret_sauce")
        login_page.click_login()

        products_page = ProductsPage(self.driver)
        products_page.click_backpack()

        product_details_page = ProductDetailsPage(self.driver)
        product_details_page.add_to_cart()
        product_details_page.press_back()

        products_page.click_redtshirt()

        product_details_page.add_to_cart()
        product_details_page.press_back()

        products_page.go_to_shoppingcart()

        cart_page = CartPage(self.driver)
        cart_page.continue_shopping()

        products_page.click_redtshirt()

        product_details_page.remove_from_cart()
        product_details_page.press_back()

        products_page.click_bolttshirt()

        product_details_page.add_to_cart()
        product_details_page.press_back()

        products_page.go_to_shoppingcart()

        cart_page.go_to_checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.input_firstname("John")
        checkout_page.input_lastname("Doe")
        checkout_page.input_zipcode("12345")
        checkout_page.checkout_continue()

        checkout_overview_page = CheckoutOverviewPage(self.driver)
        checkout_overview_page.finish_order()

        checkout_complete_page = CheckoutCompletePage(self.driver)
        self.assertEqual(checkout_complete_page.thank_you(), "Your order has been dispatched, and will arrive just as fast as the pony can get there!")


    @data(*get_data("invalid_credentials.csv"))
    @unpack
    def test_incorrect_login(self, invalid_login, invalid_password):

        login_page = LoginPage(self.driver)
        login_page.input_username(invalid_login)
        login_page.input_password(invalid_password)
        login_page.click_login()
        self.assertEqual(login_page.login_error(), "Epic sadface: Username and password do not match any user in this service")


if __name__ == '__main__':
    unittest.main(verbosity=2)
