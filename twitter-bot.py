from selenium import webdriver
from dotenv import load_dotenv
import os
import time

load_dotenv()


class TwitterBot:
    def __init__(self):
        self.chrome_driver_path = "E:\Softwares\Chrome Driver (python prject)/chromedriver.exe"

        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.driver.get("https://twitter.com/login")

        self.email_input = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div['
            '1]/label/div/div[2]/div/input')
        self.email_input.click()
        self.email_input.send_keys("Pious071")

        self.password_input = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div['
            '2]/label/div/div[2]/div/input')
        self.password_input.click()
        self.password_input.send_keys(os.getenv("PASSWORD"))

        self.login_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div['
            '3]/div/div')
        time.sleep(3)
        self.login_button.click()

        self.time.sleep(3)
        self.tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        self.tweet_button.click()
        time.sleep(2)
        self.tweet_input = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div['
            '3]/div/div/div/div[1]/div/div/div/div/div[2]/div['
            '1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div['
            '2]/div/div/div/div')
        self.tweet_input.click()
        self.tweet_input.send_keys("Hello There")
