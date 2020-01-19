from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "Login is not presented in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTRATION_INPUT), (
            "Email registration input  is not presented")
        email_registration_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION_INPUT)
        email_registration_input.send_keys(email)
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION_INPUT), (
            "Password registration input  is not presented")
        password_registration_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_INPUT)
        password_registration_input.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION_INPUT), (
            "Password registration confirmation input  is not presented")
        password_confirmation_registration_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_CONFIRMATION_INPUT)
        password_confirmation_registration_input.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), (
            "Register button  is not presented")
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        assert self.is_element_present_waiting(*LoginPageLocators.REGISTER_CONFIRMATION), (
            "Confirmation  is not presented")
        register_confirmation = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRMATION).text
        assert register_confirmation == "Thanks for registering!", "Register confirmation is not found"


