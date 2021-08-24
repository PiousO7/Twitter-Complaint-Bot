from selenium import webdriver
from dotenv import load_dotenv
import os
import time


class SpeedTest:
    def __init__(self):
        self.chrome_driver_path = "E:\Softwares\Chrome Driver (python prject)/chromedriver.exe"

        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)

        self.driver.get("https://www.speedtest.net/")

        self.go_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go_button.click()

        time.sleep(50)

        self.down_speed_str = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
            '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        self.up_speed_str = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
            '3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        self.down_speed = float(self.down_speed_str)
        self.up_speed = float(self.up_speed_str)
