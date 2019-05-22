import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def find_by_id_func():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    driver.get('https://www.google.com/')
    print(driver.title)
    driver.maximize_window()
    driver.find_element_by_name('q').clear()
    driver.find_element_by_name('q').send_keys('python')

    seach_button = wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
    seach_button.click()
    print(driver.title)

    driver.find_element_by_partial_link_text('Welcome to Python.org').click()
    print(driver.title)

    i = 0
    j = 0

    while True:
        i = i + 1
        try:
            while True:
                j = j + 1
                try:
                    element = driver.find_element_by_xpath(f"/html/body/div/header/div/nav/ul/li[{i}]/ul/li[{j}]/a")
                    print(f"{element.text}: {element.get_attribute('href')}")
                except NoSuchElementException:
                    j = 0
                    break

            element = driver.find_element_by_xpath(f"/html/body/div/header/div/nav/ul/li[{i+1}]/ul/li[{1}]/a")
        except NoSuchElementException:
            break
    driver.close()

if __name__ == '__main__':
    find_by_id()