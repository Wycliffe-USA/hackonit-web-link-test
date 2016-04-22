# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re

class BaseTest(unittest.TestCase):

################################
# functions provided by Selenium
################################
  
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        time.sleep(3)
        # self.driver.implicitly_wait(30)
        self.base_url = "https://www.wycliffe.org/"
        if self.base_url[-1:]=="/":
            self.base_url = self.base_url[:-1]
        # make sure base_url has no trailing slash
        self.driver.get(self.base_url + "/")
        self.file = open(self.time_stamp() + ".txt", "w")
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.file.close()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

##############################
# functions used by many tests
##############################    
      
    def time_stamp(self):
        # returns mon_dd_year_hh_mm
        stamp = time.asctime(time.localtime(time.time())).lower()
        stamp = stamp[4:7] + "_" + stamp[8:10] + "_" + stamp[20:24] \
            + "_" + stamp[11:13] + "_" + stamp[14:16]
        return stamp
        
    def compare_list(list1, list2):
        if (len(list1) != len(list2)):
            return ("unequal lengths")
        if (len(list1) == 0):
            return ("no list")
        for j in range(0, len(list1)):
            if (list1[j] != list2[j]):
                return ("mismatch:" + list1[j] + ", " + list2[j])
        return 0

    def mouse_click(self, button_text):
        self.driver.find_element_by_link_text(button_text).click()
        
    def mouse_click_css(self, css_text):
        self.driver.find_element_by_css_selector(css_text).click()
        
    def fix_unicode(self, my_string):
        # smart quotes, bullets, dashes
        my_string = re.sub(u"(\u2018|\u2019|\u2032)", "'", my_string)
        my_string = re.sub(u"(\u201C|\u201D|\u2033)", '"', my_string)
        my_string = re.sub(u"(\u2013|\u2014|\u2015)", "-", my_string)
        my_string = re.sub(u"(\u2022|\u25A0|\u2023)", "*", my_string)
        return my_string

    def report (self, text_line):
        # console display and file entry
        # console can only cope with ASCII charcters
        text = self.fix_unicode(text_line)
        self.file.write(text_line)
        print (text, end='')
        
    def pass_fail(self, result, text):
        if result :
            self.report("\n        Section [" + text + "] - OK\n")
        else:
            self.report("\n****[" + text + "] - failed")
    
    def upto(self, text, target):
        index = text.find(target)
        if (index < 0):
            return None
        return text[:index]

    def onfrom(self, text, target):
        index = text.find(target)
        if (index < 0):
            return None
        index += len(target)
        return text[index:]
    
    def getHTML(self, link_text):
        # get the parent element of the link (usually an HTML list)
        elem = self.driver.find_element_by_link_text(link_text)
        parent = elem.find_element_by_xpath("..")
        return (parent.get_attribute("outerHTML"))
    
    def getHTML_2(self, link_text):
        # get the grandparent element of the link (usually an HTML list)
        elem = self.driver.find_element_by_link_text(link_text)
        parent = elem.find_element_by_xpath("..")
        grandparent = parent.find_element_by_xpath("..")
        return (grandparent.get_attribute("outerHTML"))

###########################################
# functions specific to "testing_drop_down"
###########################################
    
    def list_items(self, text):
        # make the HTML list items, each from <li> to </li>, into a Python list
        result = []
        alpha = text
        if alpha is None:
            return result
        while (True):
            alpha = self.onfrom(alpha, "<li>")
            if alpha is None:
                return result
            beta = self.upto(alpha, "</li>")
            if beta is None:
                return result
            result.append(beta)

# this method "link_test" was lifted wholesale from drop_down_.py
# but it does too many things and needs to be broken up a bit

    def link_test(self, top_link, sub_link, regexp_target, return_link):
        driver = self.driver
        menu = driver.find_element_by_link_text(top_link)
        ActionChains(driver).move_to_element(menu).perform()
        driver.find_element_by_link_text(sub_link).click()
        self.assertRegex(driver.current_url, regexp_target)
        driver.find_element_by_id(return_link).click()
        
    def url_and_link(self, full_link):
    # extract the URL and the link test from the element
    # return as a two element list
        result =[]
        text = self.onfrom(full_link, "\"")
        result.append(self.upto(text, "\""))
        text = self.onfrom(text, ">")
        result.append(self.upto(text, "<"))
        return result
    
    def check_url_title(self, url, my_title):
        # attempt to open the page at URL, check that the TITLE is right
        self.report("\n    URL = [" + url + "] / TITLE = [" + my_title + "]\n" )
        still_OK = True
        try:
            self.driver.get(url)
        except:
            self.report("\n**** failed to open page [" + url + "]\n")
            still_OK = False
        if still_OK:
            try:
                WebDriverWait(self.driver, \
                    10).until(expected_conditions.title_contains(my_title))
            except:
                self.report("\n**** failed to get [" + my_title + "]\n")
                still_OK = False
        return still_OK

    def check_button(self, link_text, title, regex_url):
        # can the button be found?
        # does it link to the expected URL?
        # does the destination page exist?
        # does its title check out?
        still_OK = True
        try:
            time.sleep(2)
            elem = self.driver.find_element_by_link_text(link_text)
        except:
            self.report ("\n**** there is no button with the name " + link_text)
            still_OK = False
        if still_OK:
            try:
                url = elem.get_attribute("href")
                self.assertRegex(url, regex_url)
            except:
                self.report("**** URL mismatch: " + url + " and " + regex_url)
                still_OK = False
        if still_OK:
            result = self.check_url_title(url, title)
            if not result:
                self.report("**** page not found : " + url)
                still_OK = False
        if still_OK:
            # go back to main page
            self.driver.get(self.base_url)
        return still_OK


    def check_link_list(self, text, link_list):
        # use the link text of just one button to get the whole list
        item_list = self.list_items(text)
        still_OK = True
        for j in range (0, len(item_list)):
            page_OK = True
            link_data = self.url_and_link(item_list[j])
            url = link_data[0]
            if url[:4] != "http":
                url = self.base_url + url
            link_text = link_data[1]
            self.report("\n    Button [" + link_text + "]")
            btext = link_list[3*j]
            title = link_list[3*j+1]
            regex_url = link_list[3*j+2]
            if link_text != btext:
                page_OK = False
                still_OK = False
                self.report("\n**** Link Text: " + btext + \
                            " should be "+link_text+"\n")
            if not re.match(regex_url, url):
                still_OK = False
                page_OK = False
                self.report("\n**** URL: " + regex_url + \
                            " should be " + url + "\n")
            if page_OK:
                if not self.check_url_title(url, title):
                    still_OK = False
                    page_OK = False
                    self.report("\n**** page " + url + \
                                " with " + title + " not found")
                if page_OK:
                    self.driver.get(self.base_url)   
        return still_OK

    def check_drop_down(self, button_text, link_list):
        # first parameter is link text of button which has more drop down buttons
        # second parameter has the link texts of those buttons
        # and their expected destinations
        # the properties of the drop down buttons are tested by reading the HTML
        # check that their link texts are correct
        # check that their destination URLs are correct
        if len(link_list) < 2:
            return True
        # the "Blog" button has no drop down buttons
        text = self.getHTML(button_text)
        text = self.onfrom(text, "<li>")
        # strip off the outermost <li> tag
        return self.check_link_list(text, link_list)
    
    
    def list_urls(self, text):
        # make the anchor URL items, each from <a href=" to ", into a Python list
        result = []
        alpha = text
        while (True):
            alpha = self.onfrom(alpha, '<a href="')
            if alpha is None:
                return result
            beta = self.upto(alpha, '"')
            if beta is None:
                return result
            result.append(beta)
        
    def check_social_media(self, site_list, target_href):
        # find one of the social media buttons in the footer
        # and use it to locate all the others
        # then check that all the links are working properly
        buttons = int(len(site_list)/2)
        elem = self.driver.find_element_by_xpath('//a[@href="'+target_href+'"]')
        parent = elem.find_element_by_xpath("..")
        url_text = parent.get_attribute("outerHTML")
        # self.report("\n\n" + url_text)
        url_list = self.list_urls(url_text)
        if len(url_list) != buttons:
            self.report("\n**** "+str(len(url_list)) + " buttons found, should be : " + \
                       buttons)
            return False
        for j in range (0,buttons):
            # self.report("\n" + site_list[2*j] + "\n")
            self.check_url_title(site_list[2*j],site_list[2*j+1])
