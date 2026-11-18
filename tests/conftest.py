import pytest
from playwright.sync_api import sync_playwright
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage


@pytest.fixture(scope = "function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def base_page(page):
    return BasePage(page)


@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)
