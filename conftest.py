import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service


# Декоратор настройки параметров браузера Chrome
@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    # chrome - with UI or headless - when we don't need UI
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    return options


# Декоратор веб-драйвера
@pytest.fixture
def driver(get_chrome_options):
    s = Service('./webdrivers/chromedriver.exe')
    options = get_chrome_options
    driver = webdriver.Chrome(options=options, service=s)
    return driver


# Фикстура сервера проекта
@pytest.fixture(scope='function')
def setup(request, driver):
    driver = driver
    url = 'https://test-ssr.gfc-russia.ru/'
    if request.cls is not None:
        request.cls.driver = driver
        driver.get(url)
        yield driver
        driver.quit()


# Фикстура чтения логин в script.txt
@pytest.fixture(scope='session')
def login():
    file = open('script.txt', 'r')
    login = file.readlines()
    file.close()
    return login[0]


# Фикстура чтения пароля в script.txt
@pytest.fixture(scope='session')
def password():
    file = open('script.txt', 'r')
    password = file.readlines()
    file.close()
    return password[1]