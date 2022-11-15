from selenium.webdriver.common.by import By


def test_cart(driver):
    """
    В поиске найти товар и добавить его в корзину
    перейти в корзину и убедиться, что товар добавился
    Удалить товар из корзины
    """
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/div[1]/div/div/div/input').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div[3]/div/div/div[1]/div/div/div/input').send_keys("мясо")
    driver.find_element(By.XPATH, '//header/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/button[1]/*[1]').click()
    driver.find_element(By.XPATH, '//header/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/button[1]/*[1]').click()
    driver.get("https://n1.gfc-russia.ru/cart/")
