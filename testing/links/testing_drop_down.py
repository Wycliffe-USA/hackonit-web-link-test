from support import BaseTest
import unittest, re
# testing_drop_down.py
# 28 March 2016 - Donald Bell

class TestingDropDown(BaseTest):
           
    def test_drop_down(self):
# each link URL list has Button Text, Page Title and Page URL (as reg ex)
# Get Involved
        link_url_list_1 = ["Serve", "Join Us - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/serve/*", \
            "Pray With Us", "Prayer - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/prayer/*", \
            "Give a Gift", "Donate - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/donate/*", \
            "Start a Campaign", "Advocacy Select - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/promote/*", \
            "Find Events", "Events - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/events/*", \
            "Church Partnership", "Churches - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/churches/*", \
            "Women", "Hope Through The Word - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/women/*"]

        self.check_button("Get Involved", \
                "Get Involved - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/get-involved/*")

        result = self.check_drop_down("Get Involved", link_url_list_1)
        self.pass_fail(result, "Get Involved")

# Blog (no drop down menu)
        link_url_list_2 = [""]

        self.check_button("Blog", "Blog - Wycliffe Bible Translators", \
            r"https://www.wycliffe.org/blog/*")

        result = self.check_drop_down("Blog", link_url_list_2)
        self.pass_fail(result, "Blog")

# About
        link_url_list_3 = ["Why Bible Translation", \
                "Why Bible Translation - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/about/why/*", \
            "Where We Work", "Where We Work - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/about/where/*", \
            "Our Beliefs", "Our Beliefs - Wycliffe Bible Translators",  \
                r"https://www.wycliffe.org/about/our-beliefs/*", \
            "Meet Our Leaders", "Our Leaders - Wycliffe Bible Translators",  \
                r"https://www.wycliffe.org/about/our-leaders/*", \
            "Financial Accountability", \
                "Financial Accountability - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/about/financial-accountability/*", \
            "Partner Organizations", \
                "Associated Organizations - Wycliffe Bible Translators",
                r"https://www.wycliffe.org/about/associated-organizations/*", \
            "Contact Us", "Contact Us - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/contact/*"]

        self.check_button("About", "About Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/about/*")

        result = self.check_drop_down("About", link_url_list_3)
        self.pass_fail(result, "About")

# Resources
        link_url_list_4 = ["Discovery Center", "Wycliffe Discovery Center", \
                r"https://www.wycliffe.org/discoverycenter/*", \
            # should this be : https://villageshop.myshopify.com \
            "Shop Wycliffe", "shop.wycliffe.org", \
                r"https://shop.wycliffe.org/*", \
            # should this be : https://www.youtube.com/user/WycliffeUSA \
            "Videos", "Wycliffe Bible Translators - YouTube", \
                r"https://www.youtube.com/WycliffeUSA/*", \
            "Kids\u2019 Activities", "Kids - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/resources/kids/*", \
            "Language Resources", \
                "Language Resources - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/resources/*", \
            "Newsroom", "Newsroom - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/resources/newsroom/*", \
            "Publications", "Publications - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/resources/publications/*"]

        self.check_button("Resources", \
                "Language Resources - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/resources/*")

        result = self.check_drop_down("Resources", link_url_list_4)
        self.pass_fail(result, "Resources")
                           
# Missionaries
        link_url_list_5 = ["Find a Missionary", \
                "Partner - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/partner/*", \
            "Become a Missionary", "Join Us - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/serve/*"]

        self.check_button("Missionaries", "Partner - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/partner/*")

        result = self.check_drop_down("Missionaries", link_url_list_5)
        self.pass_fail(result, "Missionaries")
        
# Donate
        link_url_list_6 = ["Projects", "Projects - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/projects/*", \
            "Missionaries", "Partner - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/partner/*", \
            # should it be : https://www.wycliffe.org/donateyourstuff#/step1/car \
            "Non-Cash Gifts", "Donate Your Stuff - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/donateyourstuff/*", \
            "Gift Planning", "Planned Giving Home", \
                r"http://wycliffefoundation.org/*", \
            "Gift Catalog","Wycliffe Gift Catalog - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/giftcatalog/*", \
            "Current Mailing", "Peru - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/peru/*"]

        self.check_button("Donate", "Donate - Wycliffe Bible Translators", \
                r"https://www.wycliffe.org/donate/*")

        result = self.check_drop_down("Donate", link_url_list_6)
        self.pass_fail(result, "Donate")


if __name__ == "__main__":
    unittest.main()
