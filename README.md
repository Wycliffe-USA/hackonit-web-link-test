# hackonit-web-link-test
Web walk on Wycliffe USA

Problem sponsored by the Software Development Team, Information Technology
Facilitated by Brent Dehamer

About: Wycliffe USA’s Software Development Team equips and serves Bible translation partners by building timely innovative software solutions and integrated systems. Software development includes ongoing enhancement of the Wycliffe.org website.  

Overall Objective: With the constant iterative and incremental change happening on the Wycliffe.org website, maintaining a positive user experience is important and difficult. When links break or buttons do not work; the user experience is not acceptable. 

An automated testing effort has started, but the tests are currently programmed and changed on a case by case basis. This effort takes a lot of resource. To accelerate software development, we plan to create a program that can inventory website elements like hrefs, buttons, etc. and reflect those changes in the website tests.

Problem Inputs/Resources: 
•	Program languages:
    o	Python
    o	JavaScript
    o	Other
•	Testing environment:
    o	Vagrant setup of Docker with Selenium testing
•	Sources: 
    o	Wycliffe.org
    o	GitHub

Problem Outputs/Goals:
●	How to walk through the links/elements on the Wycliffe.org pages and links? 
●	How to inventory and track page changes?
●	How alter tests based on the elements catalog?

Helpful Skills:
●	Code languages:
    ○	Python
    ○	JavaScript
    ○	Other languages as needed
●	Familiarity with JSON or XML 

Setup/Prerequisites:
●	Vagrant loaded on your machine
●	Download and setup Vagrant VM 
●	Confirm Vagrant setup by running Selenium tests -
        1. start Vagrant vm
        2. in xterm window: python3 /testing/sample/sample_chrome.py
            result: Chrome
                    Home - Wycliffe Bible Translators
        3. in xterm window: python3 /testing/sample/sample_firefox.py
            result: Firefox
                    Home - Wycliffe Bible Translators
        4. Vagrant Selenium environment is setup with Chrome and Firefox
        
                    

