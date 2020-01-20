from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3 a")
    EMPTY_BASKET = (By.CSS_SELECTOR, "div#content_inner p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTRATION_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REGISTRATION_CONFIRMATION_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    REGISTER_CONFIRMATION = (By.CSS_SELECTOR, "div.alertinner.wicon")

class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alertinner  strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")




