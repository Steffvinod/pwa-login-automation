from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#loginId")
        self.password = page.locator("input[type=\"password\"]")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self):
        self.page.goto("https://pwa.skordev.com/#/login")

    def login(self, user_name, password):
        self.username.click()
        self.username.press_sequentially(user_name)

        self.password.click()
        self.password.press_sequentially(password)

        self.page.wait_for_timeout(2000)

        expect(self.login_button).to_be_enabled(timeout=10000)

        self.login_button.click()
        self.page.wait_for_timeout(5000)