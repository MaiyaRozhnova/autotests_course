# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains


browser = webdriver.Chrome()
browser.set_window_size(1400, 1000)
browser.implicitly_wait(2)

try:
    # Авторизоваться на сайте https://fix-online.sbis.ru/
    browser.get('https://fix-online.sbis.ru/')
    sleep(2)
    user_login, user_password = 'warehouse_admin_sales_vdom', 'warehouse_admin_sales_vdom123'
    test_message = 'TEST MESSAGE'
    login = browser.find_elements(By.TAG_NAME, 'input')
    login[0].send_keys(user_login, Keys.ENTER)
    assert login[0].get_attribute('value') == user_login, 'Wrong login'

    sleep(2)
    password = browser.find_element(By.CSS_SELECTOR, '[type="password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(2)
    # Перейти в реестр Контакты
    contacts = browser.find_element(By.XPATH, '//span[text()="Контакты"]')
    contacts.click()
    sleep(1)
    contacts = browser.find_element(By.XPATH, '//span[text()="Контакты"]')
    contacts.click()
    sleep(2)

    # Отправить сообщение самому себе
    new_message = browser.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    new_message.click()
    sleep(2)
    search = browser.find_elements(By.TAG_NAME, 'input')
    search[0].send_keys('Склад В.А.')
    sleep(2)
    person = browser.find_element(By.CSS_SELECTOR, 'span[title="Склад Васаби"]')
    person.click()
    sleep(2)
    new_message = browser.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    new_message.send_keys(test_message)
    sleep(2)
    send_button = browser.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    send_button.click()
    sleep(2)

    # Убедиться, что сообщение появилось в реестре
    messages = browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item-wrapper')
    assert test_message in messages[0].text, 'Wrong message'
    sleep(2)

    # Удалить это сообщение и убедиться, что удалили
    action_chains = ActionChains(browser)
    action_chains.move_to_element(messages[0])
    action_chains.pause(1)
    action_chains.perform()

    del_icon = messages[0].find_element(By.CSS_SELECTOR, '.icon-Erase')
    action_chains = ActionChains(browser)
    action_chains.move_to_element(del_icon)
    action_chains.click(del_icon)
    action_chains.perform()
    sleep(2)
    messages = browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item-wrapper')
    assert test_message not in messages[0].text, 'Message was not delete'
    print('Test end')
except Exception as e:
    print(e)
finally:
    browser.quit()
