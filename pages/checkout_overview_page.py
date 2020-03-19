# -*- coding: utf-8 -*-

from base_page import BasePage
from locators import CheckoutOverviewPageLocators

class CheckoutOverviewPage(BasePage):

    def finish_order(self):
        click_finish = self.driver.find_element(*CheckoutOverviewPageLocators.FINISH_BTN)
        click_finish.click()
