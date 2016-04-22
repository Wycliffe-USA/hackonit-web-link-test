from support import BaseTest
import unittest, re
# testsingle_dropdown.py
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



if __name__ == "__main__":
    unittest.main()
