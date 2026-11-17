class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def enter_text(self, locator, value):
        self.page.locator(locator).fill("")
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()