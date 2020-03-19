# -*- coding: utf-8 -*-

from base_page import BasePage
from locators import LoginPageLocators

class LoginPage(BasePage):

    def input_username(self, name):
        username_field = self.driver.find_element(*LoginPageLocators.USRNAME_FIELD)
        username_field.click()
        username_field.send_keys(name)

    def input_password(self, password):
        password_field = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password)

    def click_login(self):
        login_btn = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.click()

    def login_error(self):
        error_msg = self.driver.find_element(*LoginPageLocators.ERR_MSG)
        return error_msg.text
