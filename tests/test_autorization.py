from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

url = 'https://stellarburgers.nomoreparties.site/'
user_email = 'irinamaleeva7123@yandex.ru'
user_password = '9876543'

def test_enter_via_enter_account_button(driver):
    #Кнопка Войти в аккаунт
    enter_account_button = driver.find_element(By.XPATH, '//button[text()="Войти в аккаунт"]')
    enter_account_button.click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Вход"]')))
    #Поле ввода email-а
    email_input_field = driver.find_element(By.XPATH, '//fieldset[1]//input')
    #Поле ввода пароля
    password_input_field = driver.find_element(By.XPATH, '//fieldset[2]//input')
    email_input_field.send_keys(user_email)
    password_input_field.send_keys(user_password)
    #Кнопка "Войти"
    enter_button = driver.find_element(By.XPATH, '//button[text()="Войти"]')
    enter_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Оформить заказ"]')))
    assert driver.current_url == url
    #Кнопка входа в Личный кабинет
    personal_account_button = driver.find_element(By.XPATH, '//*[text()="Личный Кабинет"]')
    personal_account_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="В этом разделе вы можете изменить свои персональные данные"]')))
    #Поле "Имя"
    name_field = driver.find_element(By.XPATH, '//li[1]//input')
    #Поле "email"
    email_field = driver.find_element(By.XPATH, '//li[2]//input')
    assert name_field.get_attribute('value') == 'Irina'
    assert email_field.get_attribute('value') == user_email

def test_enter_via_personal_account_button(driver):
    # Кнопка входа в Личный кабинет
    personal_account_button = driver.find_element(By.XPATH, '//*[text()="Личный Кабинет"]')
    personal_account_button.click()
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
    assert driver.current_url == url
    personal_account_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[text()="В этом разделе вы можете изменить свои персональные данные"]')))
    # Поле "Имя"
    name_field = driver.find_element(By.XPATH, '//li[1]//input')
    # Поле "email"
    email_field = driver.find_element(By.XPATH, '//li[2]//input')
    assert name_field.get_attribute('value') == 'Irina'
    assert email_field.get_attribute('value') == user_email

def test_enter_via_link_in_registration_form(driver):
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
    # Ссылка "Войти"
    enter_link = driver.find_element(By.XPATH, '//*[text()="Уже зарегистрированы?"]/a')
    enter_link.click()
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
    assert driver.current_url == url
    # Кнопка входа в Личный кабинет
    personal_account_button = driver.find_element(By.XPATH, '//*[text()="Личный Кабинет"]')
    personal_account_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[text()="В этом разделе вы можете изменить свои персональные данные"]')))
    # Поле "Имя"
    name_field = driver.find_element(By.XPATH, '//li[1]//input')
    # Поле "email"
    email_field = driver.find_element(By.XPATH, '//li[2]//input')
    assert name_field.get_attribute('value') == 'Irina'
    assert email_field.get_attribute('value') == user_email

def test_enter_via_link_in_restore_password_form(driver):
    # Кнопка "Войти в аккаунт"
    enter_account_button = driver.find_element(By.XPATH, '//button[text()="Войти в аккаунт"]')
    enter_account_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Вход"]')))
    # Ссылка "Восстановить пароль"
    restore_password_link = driver.find_element(By.XPATH, '//a[text()="Восстановить пароль"]')
    restore_password_link.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Восстановление пароля"]')))
    # Поле ввода email-а в форме восстановления пароля
    email_field_in_restore_form = driver.find_element(By.CLASS_NAME, 'input__textfield')
    email_field_in_restore_form.send_keys(user_email)
    # Ссылка "Войти"
    enter_link = driver.find_element(By.XPATH, '//a[text()="Войти"]')
    enter_link.click()
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
    assert driver.current_url == url
    # Кнопка входа в Личный кабинет
    personal_account_button = driver.find_element(By.XPATH, '//*[text()="Личный Кабинет"]')
    personal_account_button.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[text()="В этом разделе вы можете изменить свои персональные данные"]')))
    # Поле "Имя"
    name_field = driver.find_element(By.XPATH, '//li[1]//input')
    # Поле "email"
    email_field = driver.find_element(By.XPATH, '//li[2]//input')
    assert name_field.get_attribute('value') == 'Irina'
    assert email_field.get_attribute('value') == user_email