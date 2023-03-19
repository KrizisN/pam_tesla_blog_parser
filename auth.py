import time

import selenium.webdriver
from selenium.webdriver.common.by import By

from config import config
from session import session


def login():
    login_url = "https://www.tesmanian.com/account/login"

    driver = _login_by_selenium(login_url)

    cookies = driver.get_cookies()

    _set_cookies_for_session(cookies)

    dashboard_url = "https://www.tesmanian.com/account/"
    response = session.get(dashboard_url)

    # Check the response URL to see if the user is logged in
    if "login" in response.url:
        print("User is not logged in")
    else:
        print("User is logged in")


def _login_by_selenium(login_url):
    driver = selenium.webdriver.Chrome()

    driver.delete_all_cookies()

    driver.get(login_url)

    username_field = driver.find_element("name", "customer[email]")
    username_field.send_keys(config.ACC_EMAIL)

    time.sleep(1)

    password_field = driver.find_element("name", "customer[password]")
    password_field.send_keys(config.ACC_PASSWORD)

    time.sleep(1)

    button = driver.find_element(
        By.XPATH,
        ("//button[contains(@class, 'button button--xl button--secondary w-full')]"),
    )
    button.click()

    time.sleep(2)

    return driver


def _set_cookies_for_session(cookies):
    for cookie in cookies:
        session.cookies.set(cookie["name"], cookie["value"])
