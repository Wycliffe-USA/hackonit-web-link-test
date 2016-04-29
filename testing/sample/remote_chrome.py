""" remote_chrome.py
28 March 2016
Verify acccess to local Selenium Vagrant VM for Chrome browser
"""
import traceback
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
browser = None

try:
    browser = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome'}) 
    browser.get('http://wycliffe.org')
    print( "Chrome remote" )
    print( browser.title )

except Exception as e:
    traceback.print_exc()

finally:
    if browser is not None:
        browser.quit()
