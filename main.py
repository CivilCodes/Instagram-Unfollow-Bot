from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
import os

path = "C:\Program Files (x86)\chromedriver.exe"

isExist = os.path.exists(path)
print(isExist) # Prints True if file is in right place, prints false if not

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")

time.sleep(3)

username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
# PUT YOUR USERNAME HERE
username.send_keys("USERNAME")

password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
# PUT YOUR PASSWORD HERE
password.send_keys("PASSWORD")

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
login.click()

time.sleep(3)
# YOUR PROFILE LINK
driver.get("https://www.instagram.com/btcchasin/")

following = driver.find_element_by_partial_link_text("following")
following.click()
time.sleep(3)

while True:
    for i in range(5):
        follow = driver.find_element_by_xpath('//button[text()="Following"]')
        follow.click()

        unfollow = driver.find_element_by_xpath('//button[text()="Unfollow"]')
        unfollow.click()
        time.sleep(3)

driver.quit()
