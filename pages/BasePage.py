from utils.logger import get_logger
from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, url):
        self.logger.info(f"Navigating to URL: {url}")

        try:
            self.page.goto(url)
            self.logger.info("Navigation completed successfully")

        except Exception:
            self.logger.exception(f"Navigation failed for URL: {url}")
            raise

    def click(self, locator):
        self.logger.info(f"Clicking on element: {locator}")

        try:
            self.page.locator(locator).click()
            self.logger.info(f"Successfully clicked on element: {locator}")

        except Exception:
            self.logger.exception(f"Failed to click on element: {locator}")
            raise

    def enter_text(self, locator, value, sensitive=False):
        logged_value = "[REDACTED]" if sensitive else value
        self.logger.info(
            f"Entering text '{logged_value}' into element: {locator}"
        )

        try:
            self.page.locator(locator).fill(value)
            self.logger.info(
                f"Successfully entered text '{logged_value}' into: {locator}"
            )

        except Exception:
            self.logger.exception(f"Failed to enter text into: {locator}")
            raise

    def get_text(self, locator):
        self.logger.info(f"Retrieving text from element: {locator}")

        try:
            text = self.page.locator(locator).inner_text()
            self.logger.info(f"Successfully retrieved text from: {locator}")
            return text

        except Exception:
            self.logger.exception(f"Failed to retrieve text from: {locator}")
            raise

    def press_key(self, locator, key):
        self.logger.info(f"Pressing key '{key}' on element: {locator}")

        try:
            self.page.locator(locator).press(key)
            self.logger.info(f"Successfully pressed key '{key}'")

        except Exception:
            self.logger.exception(
                f"Failed to press key '{key}' on element: {locator}"
            )
            raise

    def get_attribute(self, locator, attribute):
        self.logger.info(
            f"Retrieving attribute '{attribute}' from element: {locator}"
        )

        try:
            value = self.page.locator(locator).get_attribute(attribute)
            self.logger.info(
                f"Successfully retrieved attribute '{attribute}'"
            )
            return value

        except Exception:
            self.logger.exception(
                f"Failed to retrieve attribute '{attribute}' from: {locator}"
            )
            raise

    def is_visible(self, locator):
        self.logger.info(f"Verifying visibility of element: {locator}")

        try:
            expect(self.page.locator(locator)).to_be_visible()
            self.logger.info(f"Element is visible: {locator}")
            return True

        except Exception:
            self.logger.exception(f"Element is not visible: {locator}")
            raise