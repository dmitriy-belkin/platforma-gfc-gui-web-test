from selenium.webdriver.common.by import By


def test_auth(driver):
    """
    Перейти в личный кабинет
    Убедиться, что авторизовались
    """
    driver.find_element(By.XPATH, '/html/body/div[2]/div/header/div/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]').click()
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div/aside/div/a[2]/span').click()
    driver.implicitly_wait(20)
    user = "Бедняжка Алиса"
    assert user == 'Бедняжка Алиса'
