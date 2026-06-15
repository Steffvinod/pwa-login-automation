class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#loginId")
        self.password = page.locator("input[type=\"password\"]")
        self.login_button = page.locator(".d-flex")

    def open(self):
        self.page.goto("https://pwa.skordev.com/#/login")

    def login(self, user_name, password):
        self.username.fill(user_name)
        self.password.fill(password)
        self.login_button.click()