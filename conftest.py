import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.edge.options import Options as edge_options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

WINDOW_SIZE = '--window-size=1920,1080'
URL = "https://n1.gfc-russia.ru/"


def pytest_addoption(parser):
    parser.addoption('--browser', help='В каком браузере запустить тестирование?',
                     default='chrome')
    parser.addoption('--local', help='Локально или использовать CI?',
                     choices=['true', 'false'],
                     default='true')


@pytest.fixture(scope='session')
def test_browser(request):
    """ :returns Browser.NAME from --browser option """
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def local(request):
    """ :returns true or false from --local option """
    return request.config.getoption('--local')


@pytest.fixture(scope='session')
def get_chrome_options():
    """ Декоратор настройки параметров браузера Chrome """
    options_chrome = chrome_options()
    # "chrome" - Чтобы запустить с UI или "headless" - если не нужно отображать UI
    options_chrome.add_argument('chrome')
    options_chrome.add_argument('--start-maximized')
    options_chrome.add_argument(WINDOW_SIZE)
    options_chrome.add_argument('--no-sandbox')
    options_chrome.add_argument('--disable-dev-shm-usage')
    return options_chrome


@pytest.fixture(scope='session')
def get_firefox_options():
    """ Декоратор настройки параметров браузера FireFox """
    options_firefox = firefox_options()
    # "firefox" - Чтобы запустить с UI или "headless" - если не нужно отображать UI
    options_firefox.add_argument('firefox')
    options_firefox.add_argument('--start-maximized')
    options_firefox.add_argument(WINDOW_SIZE)
    return options_firefox


@pytest.fixture(scope='session')
def get_edge_options():
    """ Декоратор настройки параметров браузера Edge """
    options_edge = edge_options()
    # "edge" - Чтобы запустить с UI или "headless" - если не нужно отображать UI
    options_edge.add_argument('edge')
    options_edge.add_argument('--start-maximized')
    options_edge.add_argument(WINDOW_SIZE)
    return options_edge


@pytest.fixture(scope='session', autouse=True)
def driver(get_chrome_options, get_firefox_options, get_edge_options, test_browser):
    """ Вызов веб-драйвера в зависимости от выбора """
    if test_browser not in ('chrome', 'firefox', 'edge'):
        raise ValueError(f'--browser={test_browser}". Не выбран браузер или выбран некорректный.\n '
                         'Доступный браузеры:\n'
                         'Google Chrome - chrome\n'
                         'FireFox - firefox\n'
                         'Microsoft Edge - edge\n')
    if test_browser == 'chrome':
        chrome = Service('./webdrivers/chromedriver.exe')
        options = get_chrome_options
        driver = webdriver.Chrome(options=options, service=chrome)
    elif test_browser == 'firefox':
        options = get_firefox_options
        driver = webdriver.Remote(options=options)
    elif test_browser == 'edge':
        edge = Service('./webdrivers/msedgedriver.exe')
        options = get_edge_options
        driver = webdriver.Edge(options=options, service=edge)
    else:
        raise ValueError(f'--browser="{test_browser}" некорректное значение')
    yield driver
    driver.quit()


@pytest.fixture(scope='session', autouse=True)
def session(driver):
    """
    Авторизация под тестовым пользователем
    для последующих тестов
    """
    driver.get(URL)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/button[1]').click()
    driver.find_element(By.XPATH,
                        '//div[normalize-space()="Войти"]').click()
    driver.find_element(By.ID, "SIGN_IN_EMAIL").clear()
    driver.find_element(By.ID, "SIGN_IN_EMAIL").send_keys("gfc-test+alice@yandex.ru")
    driver.find_element(By.ID, "SIGN_IN_PASSWORD").clear()
    driver.find_element(By.ID, "SIGN_IN_PASSWORD").send_keys("GFCstart321!")
    driver.find_element(By.XPATH, '//button[normalize-space()="Войти"]').click()
    driver.implicitly_wait(5)
    yield
    driver.get(URL)