# -*- coding: utf-8 -*-

from base_page import BasePage
from locators import CheckoutCompletePageLocators

class CheckoutCompletePage(BasePage):

    def thank_you(self):
        thank_you_text = self.driver.find_element(*CheckoutCompletePageLocators.THANK_YOU_TXT)
        return thank_you_text.text
