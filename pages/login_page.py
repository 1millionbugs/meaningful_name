from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "Login is not presented in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_registration_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION_INPUT)
        email_registration_input.send_keys(email)
        password_registration_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_PASSWORD)
        password_registration_input.send_keys(password)
        password_confirmation_registration_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_PASSWORD_CONFIRMATION)
        password_confirmation_registration_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        #time.sleep(5)
        register_confirmation = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRMATION).text
        assert register_confirmation == "Thanks for registering!", "Register confirmation is not found"


