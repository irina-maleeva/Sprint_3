from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

url = 'https://stellarburgers.nomoreparties.site/'
user_email = 'irinamaleeva7123@yandex.ru'
user_password = '9876543'
def test_move_to_constructor_via_click_on_constructor_in_personal_account(driver):
    # Кнопка "Войти в аккаунт"
    enter_account_button = driver.find_element(By.XPATH, '//button[text()="Войти в аккаунт"]')
    enter_account_button.click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Вход"]')))
    # Поле ввода email-а
    email_input_field = driver.find_element(By.XPATH, '//fieldset[1]//input')
    # Поле ввода пароля
    password_input_field = driver.find_element(By.XPATH, '//fieldset[2]//input')
    email_input_field.send_keys(user_email)
    password_input_field.send_keys(user_password)
    # Кнопка "Войти"
    enter_button = driver.find_element(By.XPATH, '//button[text()="Войти"]')
    enter_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Оформить заказ"]')))
    # Кнопка входа в Личный кабинет
    personal_account_button = driver.find_element(By.XPATH, '//*[text()="Личный Кабинет"]')
    personal_account_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[text()="В этом разделе вы можете изменить свои персональные данные"]')))
    # Кнопка "Конструктор"
    constructor_link = driver.find_element(By.XPATH, '//*[text()="Конструктор"]')
    constructor_link.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[text()="Соберите бургер"]')))
    assert driver.current_url == url


def test_move_to_constructor_via_click_on_logo_Stellar_Burgers_in_personal_account(driver):
    # Кнопка "Войти в аккаунт"
    enter_account_button = driver.find_element(By.XPATH, '//button[text()="Войти в аккаунт"]')
    enter_account_button.click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Вход"]')))
    # Поле ввода email-а
    email_input_field = driver.find_element(By.XPATH, '//fieldset[1]//input')
    # Поле ввода пароля
    password_input_field = driver.find_element(By.XPATH, '//fieldset[2]//input')
    email_input_field.send_keys(user_email)
    password_input_field.send_keys(user_password)
    # Кнопка "Войти"
    enter_button = driver.find_element(By.XPATH, '//button[text()="Войти"]')
    enter_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Оформить заказ"]')))
    # Кнопка входа в Личный кабинет
    personal_account_button = driver.find_element(By.XPATH, '//*[text()="Личный Кабинет"]')
    personal_account_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[text()="В этом разделе вы можете изменить свои персональные данные"]')))
    # Логотип
    logo = driver.find_element(By.XPATH, '//nav/div[@class="AppHeader_header__logo__2D0X2"]')
    logo.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[text()="Соберите бургер"]')))
    assert driver.current_url == url
