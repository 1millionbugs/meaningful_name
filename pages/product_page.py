from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self): # Добавляем продукт в корзину
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def product_added_message_presented(self): # Проверяем наличие сообщения о том, что продукт добавлен
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), (
            "Message about adding is not presented")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE).text
        assert product_name == message, "No product name in the message"

    def basket_total_message_presented(self): # Проверяем совпадение цены добавленного товара со стоимостью корзины
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in message_basket_total, "No product price in the message"

    def guest_cant_see_success_message(self): # Проверяем, что гость не видит сообщение о добавлении товара
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def message_disappeared_after_adding_product_to_basket(self): # Проверяем, что сообщение о добавлении товара исчезает
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), \
            "Success message is presented, but should not be"













