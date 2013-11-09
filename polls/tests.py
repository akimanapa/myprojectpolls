"""
This file demonstrates writing tests using the LiveServerTestCase module. These will pass
when you run "manage.py test fts".
"""

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PollsTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(9)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_poll_via_admin_site(self):
        # I open my web browser, and go to the admin page
        self.browser.get(self.live_server_url + '/admin/')
        
        # I look througt the page a HTML element with a "body" tag  
        body = self.browser.find_element_by_tag_name('body')

        # I say what i expect,here the Django administration title 
        self.assertIn('Django administration', body.text)  
        
        #I enter my username and password hit return
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)
        
        #The username and password accepted,i will be taken to the page for Administration
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)
        
        polls_links = self.browser.find_elements_by_link_text('Polls')
        self.assertEquals(len(polls_links), 2)
        
        self.fail('todo: finish tests')
