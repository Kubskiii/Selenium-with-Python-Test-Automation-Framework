import pytest
import pytest_html
from selenium import webdriver

@pytest.fixture(scope="function")
def setup(request,browser,url):

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.get(url)

    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


# https://www.cleartrip.com/
# python -m pytest -v --browser chrome --url https://www.cleartrip.com/ --html=Reports/report.html --self-contained-html