""" remote_chrome.py
28 March 2016
Verify Selenium installation for Chrome browser inside the local Selenium Vagrant VM
"""
import traceback
from selenium import webdriver
browser = None

try:
    browser = webdriver.Chrome()
    browser.get('http://wycliffe.org')
    print( "Chrome" )
    print( browser.title )

except Exception as e:
    traceback.print_exc()

finally:
    if browser is not None:
        browser.quit()
