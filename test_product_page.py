from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
import faker

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.need_review
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_added_message_presented()
    page.basket_total_message_presented()

def test_guest_should_see_login_link_on_product_page(browser):
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.guest_cant_see_product_in_basket_opened_from_main_page()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.guest_cant_see_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.message_disappeared_after_adding_product_to_basket()

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        f = faker.Faker()
        email = f.email()
        password = "test12345"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.guest_cant_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.product_added_message_presented()
        page.basket_total_message_presented()





