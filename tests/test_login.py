from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_user_login(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.open()
    login_page.login("user2@st.com", "pass")

    dashboard_page.verify_dashboard_opened()