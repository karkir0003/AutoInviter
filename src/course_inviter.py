#use helium library to login to Udemy using credentials, go into DSGT Bootcamp Course, go to Students, select invite students. 
#Paste scraped email accounts into text field, click invite. You'll see some error messages in red saying X, Y, Z email accounts
# can't be invited. Parse that error message and autosend email notification from dsgtbootcamp@gmail.com with a message saying to 
# provide proper udemy account credentials

from helium import *
from constants import *
from chromedriver_autodownloader import download_chromedriver

def login_to_udemy():
    """
    Function to login to udemy
    """
    download_chromedriver('helium')
    start_chrome(UDEMY_URL)
    # click("Log in")
    write(DSGT_EMAIL, into="Email")
    write(DSGT_PASSWORD, into="Password")
    click("Log in")
    print("finished?")

login_to_udemy()



