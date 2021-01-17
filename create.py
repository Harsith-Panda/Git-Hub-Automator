import sys
import os
from selenium import webdriver

browser = webdriver.Chrome(executable_path= '/home/harsith-developer/Documents/driver/chromedriver')
browser.get('https://github.com/login')

browser.find_element_by_id("login_field").send_keys('github-usernamae')

browser.find_element_by_id("password").send_keys('github-password')

browser.find_element_by_name("commit").click()

browser.get('https://github.com/new')

browser.execute_script("window.scrollBy(0,1000)", "")

browser.find_element_by_id("repository_auto_init").click()





