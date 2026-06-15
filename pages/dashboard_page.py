from playwright.sync_api import expect


class DashboardPage:
    def __init__(self, page):
        self.page = page

    def verify_dashboard_opened(self):
        expect(self.page).to_have_url("https://pwa.skordev.com/#/home")