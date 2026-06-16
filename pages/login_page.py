class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#loginId")
        self.password = page.locator("input[type=\"password\"]")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self):
        self.page.goto("https://pwa.skordev.com/#/login")

    def login(self, user_name, password):
        self.username.fill(user_name)
        self.password.fill(password)

        self.password.press("Tab")
        self.page.wait_for_timeout(2000)

        print("Login button enabled:", self.login_button.is_enabled())

        self.login_button.click()
        self.page.wait_for_timeout(3000)