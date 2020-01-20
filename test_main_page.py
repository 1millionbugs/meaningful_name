from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_should_be_login_url(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_url()

def test_should_be_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_form()

def test_should_be_register_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.guest_cant_see_product_in_basket_opened_from_main_page()






