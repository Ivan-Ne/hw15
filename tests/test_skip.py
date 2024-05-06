import pytest
from models.github_page import github_page

def test_mobile_skip(setup_browser):
    if setup_browser == "mobile":
        pytest.skip("Это мобильное разрешение")
    github_page.open()
    github_page.desktop_sign_in()
    github_page.should_have_text_sign_in()

def test_desktop_skip(setup_browser):
    if setup_browser == "desktop":
        pytest.skip("Это десктопное разрешение")
    github_page.open()
    github_page.mobile_sign_in()
    github_page.should_have_text_sign_in()

