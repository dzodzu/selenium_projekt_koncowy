# -*- coding: utf-8 -*-

from base_page import BasePage
from locators import CartPageLocators

class CartPage(BasePage):

    def continue_shopping(self):
        cont_shop = self.driver.find_element(*CartPageLocators.CONTINUE_BTN)
        cont_shop.click()

    def go_to_checkout(self):
        checkout = self.driver.find_element(*CartPageLocators.CHECKOUT_BTN)
        checkout.click()
