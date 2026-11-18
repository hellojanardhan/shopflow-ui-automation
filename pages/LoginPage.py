from pages.BasePage import BasePage
from playwright.sync_api import expect
from config.config import ConfigManager


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"
        self.app_logo = ".app_logo"
        self.error_button = "button[class='error-button']"
        self.inventory_url = "/inventory.html"
        self.error_message = "[data-test='error']"
        self.config_manager = ConfigManager()

    def login(self, username, password, expected_message=None):

        self.logger.info("Starting login process")

        self.navigate(self.config_manager.BASE_URL)

        self.enter_text(self.username, username)
        self.enter_text(self.password, password)

        self.click(self.login_button)

        self.logger.info("Login form submitted")

        if expected_message is None:

            # Positive scenario
            self.logger.info("Verifying successful login")

            expect(self.page).to_have_url(
                f"{self.config_manager.BASE_URL.rstrip('/')}{self.inventory_url}"
            )
            expect(self.page.locator(self.app_logo)).to_have_text("Swag Labs")

            self.logger.info("Login successful - Inventory page is displayed")

        else:

            # Negative scenario
            self.logger.info("Verifying unsuccessful login")

            error = self.page.locator(self.error_message)

            expect(error).to_be_visible()
            expect(error).to_have_text(expected_message)

            self.logger.info(
                f"Login failed as expected. Error verified: {expected_message}"
            )

    def login_using_enter_key(self, username, password):

        self.logger.info("Starting login using Enter key")

        self.navigate(self.config_manager.BASE_URL)

        self.enter_text(self.username, username)
        self.enter_text(self.password, password)

        self.press_key(self.password, "Enter")

        self.logger.info("Login submitted using Enter key")

    def is_password_masked(self):
        self.logger.info("Starting login using Enter key")
        self.navigate(self.config_manager.BASE_URL)

        self.logger.info("Verifying password field is masked")
        password_type = self.get_attribute(self.password, "type")

        result = password_type == "password"

        if result:
            self.logger.info("Password field is masked successfully")
        else:
            self.logger.error("Password field is not masked")

        return result

    def dismiss_login_error_message(self, username, password):

        self.logger.info("Starting invalid login scenario")

        self.navigate(self.config_manager.BASE_URL)

        self.enter_text(self.username, username)
        self.enter_text(self.password, password)

        self.click(self.login_button)

        self.logger.info("Verifying login error message")

        expect(self.page.locator(self.error_message)).to_be_visible()

        self.logger.info("Login error message displayed successfully")

        self.click(self.error_button)

        self.logger.info("Dismissing login error message")

        expect(self.page.locator(self.error_message)).to_be_hidden()

        self.logger.info("Login error message dismissed successfully")
