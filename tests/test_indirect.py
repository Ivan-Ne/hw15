import pytest
from models.github_page import github_page

@pytest.mark.parametrize('setup_browser', ['desktop'], indirect=True)
def test_github_desktop(setup_browser):
    github_page.open()
    github_page.desktop_sign_in()
    github_page.should_have_text_sign_in()


@pytest.mark.parametrize('setup_browser', ['mobile'], indirect=True)
def test_github_mobile(setup_browser):
    github_page.open()
    github_page.mobile_sign_in()
    github_page.should_have_text_sign_in()