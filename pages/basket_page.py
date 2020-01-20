from .locators import BasePageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def guest_cant_see_product_in_basket_opened_from_main_page(self): # Проверяем, что гость не видит продукта в корзине \
                                                                      # при переходе с главной страницы
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_ADDED_TO_BASKET), \
            "Product is presented, but should not be"
        empty_basket = self.browser.find_element(*BasePageLocators.EMPTY_BASKET).text
        assert "Your basket is empty" in empty_basket, "Your basket is not empty"

