from selenium.webdriver.common.by import By

def test_move_to_bun_section_of_constructor(driver):
    # ссылка "Соусы"
    sauces_link = driver.find_element(By.XPATH, '//span[text()="Соусы"]/parent::div')
    # ссылка "Булки"
    buns_link = driver.find_element(By.XPATH, '//span[text()="Булки"]/parent::div')
    sauces_link.click()
    buns_link.click()
    assert 'tab_tab_type_current__2BEPc' in buns_link.get_attribute('class')
    assert 'tab_tab_type_current__2BEPc' not in sauces_link.get_attribute('class')

def test_move_to_sauces_section_of_constructor(driver):
    # ссылка "Соусы"
    sauces_link = driver.find_element(By.XPATH, '//*[text()="Соусы"]/parent::div')
    # ссылка "Булки"
    buns_link = driver.find_element(By.XPATH, '//*[text()="Булки"]/parent::div')
    sauces_link.click()
    assert 'tab_tab_type_current__2BEPc' in sauces_link.get_attribute('class')
    assert 'tab_tab_type_current__2BEPc' not in buns_link.get_attribute('class')

def test_move_to_filiings_section_of_constructor(driver):
    # ссылка "Булки"
    buns_link = driver.find_element(By.XPATH, '//*[text()="Булки"]/parent::div')
    # ссылка "Начинки"
    fillings_link = driver.find_element(By.XPATH, '//*[text()="Начинки"]/parent::div')
    fillings_link.click()
    assert 'tab_tab_type_current__2BEPc' in fillings_link.get_attribute('class')
    assert 'tab_tab_type_current__2BEPc' not in buns_link.get_attribute('class')