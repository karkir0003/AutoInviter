#use helium library to login to Udemy using credentials, go into DSGT Bootcamp Course, go to Students, select invite students. 
#Paste scraped email accounts into text field, click invite. You'll see some error messages in red saying X, Y, Z email accounts
# can't be invited. Parse that error message and autosend email notification from dsgtbootcamp@gmail.com with a message saying to 
# provide proper udemy account credentials

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
driver = webdriver.Firefox(executable_path=r'C:\Users\karki\geckodriver-v0.30.0-win64\geckodriver.exe')
driver.get("https://www.facebook.com")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()