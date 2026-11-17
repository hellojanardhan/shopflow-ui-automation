from playwright.sync_api import expect
from config.config import ConfigManager


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"
        self.app_logo = "div[class='app-logo']"
        self.config_manager = ConfigManager()

    def login(self, username, password):
        self.page.goto(self.config_manager.BASE_URL)
        self.page.locator(self.username).fill(username)
        self.page.locator(self.password).fill(password)
        self.page.locator(self.login_button).click()
