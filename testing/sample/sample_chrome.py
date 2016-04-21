from selenium import webdriver
import traceback
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
