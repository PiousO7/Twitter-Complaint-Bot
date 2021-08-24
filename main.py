from selenium import webdriver
from dotenv import load_dotenv
import os
import time

load_dotenv()

DOWN_SPEED = float(os.getenv("DOWN_SPEED"))
UP_SPEED = float(os.getenv("UP_SPEED"))

chrome_driver_path = "E:\Softwares\Chrome Driver (python prject)/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.speedtest.net/")

go_button = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go_button.click()

time.sleep(50)
down_speed_str = driver.find_element_by_xpath(
    '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
    '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
up_speed_str = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                            '3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
down_speed = float(down_speed_str)
up_speed = float(up_speed_str)
print(down_speed)
print(up_speed)

time.sleep(10)

if down_speed < DOWN_SPEED and up_speed < UP_SPEED:
    driver.get("https://twitter.com/login")
    time.sleep(5)

    email_input = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div['
                                               '1]/label/div/div[2]/div/input')
    email_input.click()
    email_input.send_keys(os.getenv("USER_ID"))

    password_input = driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div['
        '2]/label/div/div[2]/div/input')
    password_input.click()
    password_input.send_keys(os.getenv("PASSWORD"))

    login_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div['
                                                '3]/div/div')
    time.sleep(3)
    login_button.click()

    time.sleep(3)
    tweet_button = driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
    tweet_button.click()
    time.sleep(2)
    tweet_input = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div['
                                               '3]/div/div/div/div[1]/div/div/div/div/div[2]/div['
                                               '1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div['
                                               '2]/div/div/div/div')
    tweet_input.click()
    tweet_input.send_keys(f"@JioCare My internet speed is {down_speed} mbps down/{up_speed} mbps up when I paid for"
                          f" {DOWN_SPEED} mbps down/ {UP_SPEED} mbps up. Please look into it")

    # Tweet button is not programmed
