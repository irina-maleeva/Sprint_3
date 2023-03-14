from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

url = 'https://stellarburgers.nomoreparties.site/'

def test_registration_email_correct_pattern_password_6_symbols_registration_pass_to_login_page(driver, correct_random_name, correct_random_email, correct_random_password):
    # Кнопка "Войти в аккаунт"
    enter_account_button = driver.find_element(By.XPATH, '//button[text()="Войти в аккаунт"]')
    enter_account_button.click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Вход"]')))
    # Ссылка "Зарегистрироваться"
    registration_link = driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj')
    registration_link.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Регистрация"]')))
    # Поле "Имя"
    name_field = driver.find_element(By.XPATH, '//fieldset[1]//input')
    # Поле "Email"
    email_field = driver.find_element(By.XPATH, '//fieldset[2]//input')
    # Поле "Пароль"
    password_field = driver.find_element(By.XPATH, '//fieldset[3]//input')
    name_field.send_keys(correct_random_name)
    email_field.send_keys(correct_random_email)
    password_field.send_keys(correct_random_password)
    # Кнопка "Зарегистироваться"
    registration_button = driver.find_element(By.XPATH, '//button[text()="Зарегистрироваться"]')
    registration_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Вход"]')))
    assert driver.current_url == url + 'login'

def test_registration_password_less_than_6_digits_registration_not_possible(driver, correct_random_name, correct_random_email, too_short_random_password):
    # Кнопка "Войти в аккаунт"
    enter_account_button = driver.find_element(By.XPATH, '//button[text()="Войти в аккаунт"]')
    enter_account_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Вход"]')))
    # Ссылка "Зарегистрироваться"
    registration_link = driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj')
    registration_link.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Регистрация"]')))
    # Поле "Имя"
    name_field = driver.find_element(By.XPATH, '//fieldset[1]//input')
    # Поле "Email"
    email_field = driver.find_element(By.XPATH, '//fieldset[2]//input')
    # Поле "Пароль"
    password_field = driver.find_element(By.XPATH, '//fieldset[3]//input')
    name_field.send_keys(correct_random_name)
    email_field.send_keys(correct_random_email)
    password_field.send_keys(too_short_random_password)
    # Кнопка "Зарегистироваться"
    registration_button = driver.find_element(By.XPATH, '//button[text()="Зарегистрироваться"]')
    registration_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//p[text()="Некорректный пароль"]')))
    assert driver.current_url == url + 'register'
    assert 'input__error' in driver.find_element(By.XPATH, '//fieldset[3]//p').get_attribute('class')
    assert driver.find_element(By.XPATH, '//fieldset[3]//p').text == "Некорректный пароль"