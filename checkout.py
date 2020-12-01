#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

#GLOBALS from config file

LOGIN_EMAIL = config['login']['LOGIN_EMAIL']
LOGIN_PW = config['login']['LOGIN_PW']
CVV = config['login']['CVV']

XBOX_URL = config['url']['XBOX_URL']
PS5_URL = config['url']['PS5_URL']
TEST_URL = config['url']['TEST_URL']

def setup_profile():
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    firefox_profile.set_preference("javascript.enabled", False)
    firefox_profile.set_preference("permissions.default.stylesheet", 2)
    #firefox_profile.set_preference("permissions.default.image", 2)

    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    driver.get(TEST_URL)
    driver.maximize_window()
    return driver

def smart_clicker(driver, xpath):
    while True:
        try:
            find_element = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            find_element.click()
            break
        except:
            driver.refresh()
            continue

def add_to_cart(driver):
    add_to_cart_xpath =  "(//*[@class='spin-button-children'])"
    smart_clicker(driver,add_to_cart_xpath)
    
def checkout(driver):
    checkout_xpath = "(//button[@data-automation-id='pac-pos-proceed-to-checkout'])[1]"
    smart_clicker(driver, checkout_xpath)

def signin(driver):
    signin_xpath = "(//input[@data-automation-id='signin-email-input'])[1]"
    signin_email = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, signin_xpath)))
    signin_email.send_keys(LOGIN_EMAIL)

    signin_pw_xpath = "(//input[@data-automation-id='signin-password-input'])[1]"
    signin_pw = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, signin_pw_xpath)))
    signin_pw.send_keys(LOGIN_PW)

    signin_btn_xpath = "(//button[@data-automation-id='signin-submit-btn'])[1]"
    smart_clicker(driver, signin_btn_xpath)

def review_finalize_order(driver):
    delivery_type_xpath = "(//button[@data-automation-id='fulfillment-continue'])[1]"
    smart_clicker(driver, delivery_type_xpath)

    addr_xpath = "(//button[@data-automation-id='address-book-action-buttons-on-continue'])[1]"
    smart_clicker(driver, addr_xpath)

    cvv_xpath = "(//input[@data-automation-id='cvv-verify-cc-0'])[1]"
    cvv = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, cvv_xpath)))
    cvv.send_keys(CVV)

    #submit credit card details - review order
    review_order_xpath = "(//button[@data-automation-id='submit-payment-cc'])[1]"
    review_order = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, review_order_xpath)))
    review_order.click()
    #_smart_clicker(driver, review_order_xpath)

    #This makes the purchase, only uncomment when ready to buy
    #finalize_order_xpath = "(//*[@class='button-wrapper'])"
    #finalize = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, finalize_order_xpath)))
    #finalize.click()

if __name__ == "__main__":
    driver = setup_profile()
    add_to_cart(driver)
    checkout(driver)
    signin(driver)
    review_finalize_order(driver)
