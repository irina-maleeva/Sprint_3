from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

url = 'https://stellarburgers.nomoreparties.site/'
user_email = 'irinamaleeva7123@yandex.ru'
user_password = '9876543'
def test_enter_to_personal_account_by_click(driver):
    # Кнопка "Войти в аккаунт"
    enter_account_button = driver.find_element(By.XPATH, '//button[text()="Войти в аккаунт"]')
    enter_account_button.click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Вход"]')))
    # Кнопка ввода email-а
    email_input_field = driver.find_element(By.XPATH, '//fieldset[1]//input')
    # Кнопка ввода пароя
    password_input_field = driver.find_element(By.XPATH, '//fieldset[2]//input')
    email_input_field.send_keys(user_email)
    password_input_field.send_keys(user_password)
    # Кнопка "Войти"
    enter_button = driver.find_element(By.XPATH, '//button[text()="Войти"]')
    enter_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Оформить заказ"]')))
    # Кпонка входа в личный кабинет
    personal_account_button = driver.find_element(By.XPATH, '//*[text()="Личный Кабинет"]')
    personal_account_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[text()="В этом разделе вы можете изменить свои персональные данные"]')))
    assert driver.current_url == url + 'account/profile'