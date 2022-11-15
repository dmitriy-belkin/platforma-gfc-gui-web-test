from selenium.webdriver.common.by import By


def test_add_favorites(driver):
    """
    Добавление в избранное из каталога
    для авторизованного пользователя.
    """
    sku = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div[2]/div/div/div[1]/a[2]').get_attribute("title")
    driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/button[2]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/header/div/div[3]/div/div/div[2]/div/div[2]/div[2]').click()
    assert sku == driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/div/div[2]/div[2]/div/div/div/a[2]").get_attribute("title")


def test_delete_from_favorite(driver):
    """
     Удаление из "Избранное" для авторизованного пользователя
    """