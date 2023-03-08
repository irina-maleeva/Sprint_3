import pytest
import random
import string
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

@pytest.fixture()
def correct_random_name():
    first_letter = random.choice(string.ascii_uppercase)
    correct_name = first_letter.join(random.choice(string.ascii_lowercase) for i in range(7))
    return correct_name

@pytest.fixture()
def correct_random_email():
    username = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
    domen = ''.join(random.choice(string.ascii_letters) for i in range(5))
    correct_random_email = username + '@' + domen + '.com'
    return correct_random_email

@pytest.fixture()
def correct_random_password():
    correct_random_password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(random.randint(6,12)))
    return correct_random_password

@pytest.fixture()
def too_short_random_password():
    too_short_random_password = ''.join(
    random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(random.randint(0,5)))
    return too_short_random_password