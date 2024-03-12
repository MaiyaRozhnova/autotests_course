# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


browser = webdriver.Chrome()
browser.set_window_size(1400, 1000)
browser.implicitly_wait(10)
wait = WebDriverWait(browser, 5)

try:
    # Перейти на https://sbis.ru/
    browser.get('https://sbis.ru/')

    # Перейти в раздел "Контакты"
    contacts = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, 'Контакты')))
    contacts.click()

    # Найти баннер Тензор, кликнуть по нему
    tensor_link = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')))
    tensor_link.click()

    # Перейти на https://tensor.ru/
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://tensor.ru/'

    # Проверить, что есть блок новости "Сила в людях"
    sila = browser.find_elements(By.XPATH, "//p[text()[contains(., 'Сила в людях')]]")
    assert len(sila) > 0

    # Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    elem = browser.find_element(By.XPATH, "//p[text()[contains(., 'Сила в людях')]]/parent::div")
    link = elem.find_element(By.LINK_TEXT, 'Подробнее')
    browser.execute_script("arguments[0].scrollIntoView(true);", link)
    link.click()
    assert browser.current_url == 'https://tensor.ru/about'
    print('Test end')
finally:
    browser.quit()
