def login(self, user_name, password):
    self.username.click()
    self.username.fill("")
    self.username.type(user_name, delay=100)

    self.password.click()
    self.password.fill("")
    self.password.type(password, delay=100)

    self.password.press("Tab")
    self.page.wait_for_timeout(3000)

    print("Username value:", self.username.input_value())
    print("Password value:", self.password.input_value())
    print("Login button enabled:", self.login_button.is_enabled())
    print("Login button text:", self.login_button.inner_text())

    self.page.locator("body").click()
    self.page.wait_for_timeout(1000)

    print("Login button enabled after body click:", self.login_button.is_enabled())

    self.login_button.click()
    self.page.wait_for_timeout(5000)