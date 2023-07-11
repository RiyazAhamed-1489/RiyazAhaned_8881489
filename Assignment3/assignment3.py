# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the linkedin homepage
driver.get("https://www.linkedin.com")
time.sleep(5)

# Finding the username and entering text

username = driver.find_element("id", "session_key")
username.send_keys("riyazahamed934@gmail.com")
time.sleep(2)

# Finding the username and entering text
password = driver.find_element("id", "session_password")
password.send_keys("riyazahamed@2016")
time.sleep(2)
# Click on Sign in button after entering user name and password
signin = driver.find_element("xpath","//*[@id='main-content']/section[1]/div/div/form[1]/div[2]/button")
signin.click()
time.sleep(6)

#search the value in the search bar
search_bar = driver.find_element("xpath","//*[@id='global-nav-typeahead']/input")
search_bar.send_keys("hiring")
# Submitting the search query
search_bar.send_keys(Keys.RETURN)
# Waiting for the search result page to load
time.sleep(5)

#click on My Network icon
mynetwork = driver.find_element("xpath","//*[@id='global-nav']/div/nav/ul/li[2]/a/span")
mynetwork.click()
# Waiting for the Network page to load
time.sleep(4)

#click on Jobs
myjobs = driver.find_element("xpath", "//*[@id='global-nav']/div/nav/ul/li[3]/a/span")
myjobs.click()
# Waiting for the Job page to load
time.sleep(4)
#Get the title of the Job page
title = driver.title
print("Title:", title)

#Verifying that the job page has loaded
assert "Jobs | LinkedIn" in driver.title

#click on messaging
message = driver.find_element("xpath","//*[@id='global-nav']/div/nav/ul/li[4]/a/span")
message.click()
# Waiting for the messaging page to load
time.sleep(3)

#click on my notification
notification = driver.find_element("xpath","//*[@id='global-nav']/div/nav/ul/li[5]/a/span")
notification.click()
# Waiting for the Notification page to load
time.sleep(3)

# Closing the webdriver
driver.close()