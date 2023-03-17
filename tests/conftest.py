import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    print("\nquit browser..")
    browser.quit()