from selenium.webdriver.common.by import By


URL = "https://n1.gfc-russia.ru/"

def test_search_latin(driver):

    """
    Поиск товара по названию на латинице
    """
    search_input = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/div/div[1]/div/div/div[1]/input')
    search_input.click()
    search_input.send_keys("vjkjrj")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/div/div[1]/div/div/div[1]/span/div/button').click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    product = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[2]/div[2]/div/div/div[6]/a[2]').get_attribute("title")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[2]/div[2]/div/div/div[6]/a[2]').click()

    assert product == driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[2]/div[2]/div/div/div[6]/a[2]').get_attribute("title")


def test_search_misprint(driver):

    """
    Поиск товара по названию с ошибкой
    """
    driver.get(URL)
    search_input = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/div/div[1]/div/div/div[1]/input')
    search_input.click()
    search_input.send_keys("Малоко")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/div/div[1]/div/div/div[1]/span/div/button').click()
    product = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[2]/div[2]/div/div/div[4]/a[2]').get_attribute("title")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[2]/div[2]/div/div/div[4]/a[2]').click()

    assert product == driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[2]/div[2]/div/div/div[4]/a[2]').get_attribute("title")


def test_search_latinmisprint(driver):
    """
    Поиск товара по названию с ошибкой на латинице
    """
    driver.get(URL)
    search_input = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/div/div[1]/div/div/div[1]/input')
    search_input.click()
    search_input.send_keys("Vfkjrj")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/div/div[1]/div/div/div[1]/span/div/button').click()
    product = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[2]/div[2]/div/div/div[3]/a[2]').get_attribute("title")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[2]/div[2]/div/div/div[3]/a[2]').click()

    assert product == driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[2]/div[2]/div/div/div[3]/a[2]').get_attribute("title")


def test_search_emptyline(driver):
    """
    Выполнение пустого поиска
    """
    driver.get(URL)
    search_input = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/div/div[1]/div/div/div[1]/input')
    search_input.click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/div/div[1]/div/div/div[1]/span/div/button').click()
    mainpageelement = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[3]/div[1]/a/h3')
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[3]/div[1]/a/h3').click()

    assert mainpageelement == driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[3]/div[1]/a/h3')


def test_search_unavailablesku(driver):
    """
    Поиск несуществующего товара
    """
    driver.get(URL)
    search_input = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/div/div[1]/div/div/div[1]/input')
    search_input.click()
    search_input.send_keys("Молоток")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/div/div[1]/div/div/div[1]/span/div/button').click()
    message = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div/div/section[1]/div/h1')
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div/div/section[1]/div/h1').click()

    assert message == driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div/div/section[1]/div/h1')