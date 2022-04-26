from selenium.webdriver.common.by import By


def test_auth(driver):
    """
    Перейти в личный кабинет
    Убедиться, что авторизовались
    """

    driver.find_element(By.XPATH, '//div[normalize-space()="Профиль"]').click()
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div/div[1]/aside/div/a[2]').click()
    driver.implicitly_wait(20)
    user = driver.find_element(By.XPATH,
                               "/html/body/div[2]/div/main/div/div/div[2]/div/div[2]/div/div[1]/span").text
    assert user == 'demetrius.belkin@gmail.com'


def test_negative_auth(driver):
    """Тест провальный"""
    driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div/div[1]/aside/div/a[2]').click()
    driver.implicitly_wait(20)
    user = driver.find_element(By.XPATH,
                               "/html/body/div[2]/div/main/div/div/div[2]/div/div[2]/div/div[1]/span").text
    assert user != 'demetrius.belkin@gmail.com'
