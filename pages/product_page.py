# -*- coding: utf-8 -*-

from base_page import BasePage
from locators import ProductDetailsPageLocators

class ProductDetailsPage(BasePage):

    def add_to_cart(self):
        add_item = self.driver.find_element(*ProductDetailsPageLocators.ADDTOCART_BTN)
        add_item.click()

    def remove_from_cart(self):
        remove_item = self.driver.find_element(*ProductDetailsPageLocators.REMOVEFROMCART_BTN)
        remove_item.click()

    def press_back(self):
        back = self.driver.find_element(*ProductDetailsPageLocators.BACK_BTN)
        back.click()
