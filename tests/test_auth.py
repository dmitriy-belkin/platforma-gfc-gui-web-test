import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup')
class TestAuthIndividual:

    def test_auth(self, driver, login, password):
        """
        Найти на главной странице кнопку "Войти"
        Нажать на кнопку "Войти"
        Логин из файла поместить в поле "Логин"
        Из файла достать пароль и поместить в поле "Пароль"
        Нажать на кнопку "Войти"
        Перейти в личный кабинет
        Убедиться, что авторизовались
        """

        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/header/div[2]/div[3]/div/div/div/div/div/div[3]/div/div[2]").click()
        driver.find_element(By.ID, "SIGN_IN_EMAIL").clear()
        driver.find_element(By.ID, "SIGN_IN_EMAIL").send_keys(login)
        driver.find_element(By.ID, "SIGN_IN_PASSWORD").clear()
        driver.find_element(By.ID, "SIGN_IN_PASSWORD").send_keys(password)
        driver.find_element(By.XPATH, '//button[normalize-space()="Войти"]').click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//div[normalize-space()="Профиль"]').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div/div[1]/aside/div/a[2]').click()
        driver.implicitly_wait(5)
        user = driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div/main/div/div/div[2]/div/div[2]/div/div[1]/span").text
        assert user + '\n' == login

    def test_logout(self, driver, login, password):
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/header/div[2]/div[3]/div/div/div/div/div/div[3]/div/div[2]").click()
        driver.find_element(By.ID, "SIGN_IN_EMAIL").clear()
        driver.find_element(By.ID, "SIGN_IN_EMAIL").send_keys(login)
        driver.find_element(By.ID, "SIGN_IN_PASSWORD").clear()
        driver.find_element(By.ID, "SIGN_IN_PASSWORD").send_keys(password)
        driver.find_element(By.XPATH, '//button[normalize-space()="Войти"]').click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//div[normalize-space()="Профиль"]').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div/div[1]/aside/div/a[2]').click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//button[normalize-space()="Выйти"]').click()
