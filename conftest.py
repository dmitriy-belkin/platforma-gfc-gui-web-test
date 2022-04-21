import pytest
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption('--browser', help='В каком браузере тестировать?',
                     default='chrome')
    parser.addoption('--local', help='Локально или использовать CI?',
                     choices=['true', 'false'],
                     default='true')


@pytest.fixture(scope='session')
def test_browser(request):
    """ Возвращает название браузера """
    return request.config.getoption('--browser')


@pytest.fixture
def get_chrome_options():
    """ Декоратор настройки параметров браузера Chrome """
    options = chrome_options()
    # chrome - with UI or headless - when we don't need UI
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    return options


@pytest.fixture
def driver(get_chrome_options):
    """ Декоратор веб-драйвера """
    s = Service('./webdrivers/chromedriver.exe')
    options = get_chrome_options
    driver = webdriver.Chrome(options=options, service=s)
    return driver


@pytest.fixture(scope='function')
def setup(request, driver, remote_browser):
    """ Фикстура сервера проекта """
    driver = driver
    url = 'https://test-ssr.gfc-russia.ru/'
    if request.cls is not None:
        request.cls.driver = driver
        remote_browser.get(url)
        yield driver
        driver.quit()


@pytest.fixture(scope='session')
def login():
    """ Фикстура чтения логин в script.txt """
    file = open('script.txt', 'r')
    login = file.readlines()
    file.close()
    return login[0]


@pytest.fixture(scope='session')
def password():
    """ Фикстура чтения пароля в script.txt """
    file = open('script.txt', 'r')
    password = file.readlines()
    file.close()
    return password[1]


@pytest.fixture(scope='session')
def local(request):
    return request.config.getoption('--local')


@pytest.fixture(scope='function')
def remote_browser(test_browser, local) -> Remote:
    """ Выбирает значение браузера и хоста  """
    if local != 'true' and local != 'false':
        raise ValueError(f'--local={local}". Не удалось настроить драйвер.\n'
                         'указать "true" для локального запуска\n'
                         'указать "false" для использования CI')
    cmd_executor = {
        'true': 'http://localhost:4444/wd/hub',
        'false': f'http://selenium__standalone-{test_browser}:4444/wd/hub'
    }
    if test_browser == 'firefox':
        driver = webdriver.Remote(
            options=webdriver.FirefoxOptions(),
            command_executor=cmd_executor[local])
    elif test_browser == 'chrome':
        driver = webdriver.Remote(
            options=webdriver.ChromeOptions(),
            command_executor=cmd_executor[local])
    elif test_browser == 'edge':
        driver = webdriver.Remote(
            option=webdriver.EdgeOptions(),
            command_executor=cmd_executor[local])
    else:
        raise ValueError(
            f'--browser="{test_browser}" не то значение')
    yield driver
    driver.quit()
