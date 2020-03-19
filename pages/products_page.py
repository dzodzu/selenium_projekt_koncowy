# -*- coding: utf-8 -*-

from base_page import BasePage
from locators import ProductsPageLocators
from locators import BasePageLocators

class ProductsPage(BasePage):

    def click_backpack(self):
        backpack_item = self.driver.find_element(*ProductsPageLocators.BACKPACK_LINK)
        backpack_item.click()

    def click_redtshirt(self):
        redshirt_item = self.driver.find_element(*ProductsPageLocators.REDTSHIRT_LINK)
        redshirt_item.click()

    def click_bolttshirt(self):
        boltshirt_item = self.driver.find_element(*ProductsPageLocators.BOLTTSHIRT_LINK)
        boltshirt_item.click()

    def go_to_shoppingcart(self):
        shoppingcart = self.driver.find_element(*BasePageLocators.SHOPPINGCART_BTN)
        shoppingcart.click()
