from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


PATH = './chromedriver.exe'  # this is for chrome version 93  download from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the same folder as this file
# you can view chrome version in chrome://version, paste this in url bar and see the version number and downlaod corresponding version of chromedriver

driver = webdriver.Chrome(executable_path=PATH)

driver.get('https://twitter.com/login')

email = "xxxxx@gmail.com"  # your email
password = "xxxxxx"  # your password

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'react-root')))
    time.sleep(3)
    email_input = main.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
    email_input.send_keys(email)
    password_input = main.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
    password_input.send_keys(password)
    password_input.submit()
    time.sleep(3)
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'react-root')))
        time.sleep(2)
        tweet = "Hey, This is tweet by Selenium"
        tweetInputField = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        print(tweetInputField)
        tweetInputField.send_keys(tweet)
        tweetButton = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        print(tweetButton)
        time.sleep(3)
        tweetButton.click()
        time.sleep(3)
    except:
        print("Error while tweeting")
except:
    print("Error while logging in")


driver.quit()
