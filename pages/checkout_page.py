# -*- coding: utf-8 -*-

from base_page import BasePage
from locators import CheckoutPageLocators

class CheckoutPage(BasePage):

    def input_firstname(self, name):
        firstname_field = self.driver.find_element(*CheckoutPageLocators.FIRSTNAME_INPUT)
        firstname_field.click()
        firstname_field.send_keys(name)

    def input_lastname(self, name):
        lastname_field = self.driver.find_element(*CheckoutPageLocators.LASTNAME_INPUT)
        lastname_field.click()
        lastname_field.send_keys(name)

    def input_zipcode(self, code):
        zipcode_field = self.driver.find_element(*CheckoutPageLocators.ZIPCODE_INPUT)
        zipcode_field.click()
        zipcode_field.send_keys(code)

    def checkout_continue(self):
        click_continue = self.driver.find_element(*CheckoutPageLocators.CHECKCONTINUE_BTN)
        click_continue.click()
