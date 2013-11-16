"""
This file demonstrates writing tests using the LiveServerTestCase module. These will pass
when you run "manage.py test".
"""

#from django.test import LiveServerTestCase
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import datetime
from django.test import TestCase
from polls.models import Poll, Choice


#class PollsTest(LiveServerTestCase):

    #def setUp(self):
        #self.browser = webdriver.Firefox()
        #self.browser.implicitly_wait(3)

    #def tearDown(self):
        #self.browser.quit()

    #def test_can_create_new_poll_via_admin_site(self):
        # I open my web browser, and go to the admin page
        #self.browser.get(self.live_server_url + '/admin/')
        
        # I look througt the page a HTML element with a "body" tag  
        #body = self.browser.find_element_by_tag_name('body')

        # I say what i expect,here the Django administration title 
        #self.assertIn('Django administration', body.text)  
        
        #I enter my username and password hit return
        #username_field = self.browser.find_element_by_name('username')
        #username_field.send_keys('helpdeskadmin')
        
        #password_field = self.browser.find_element_by_name('password')
        #password_field.send_keys('Kigabo47**')
        #password_field.send_keys(Keys.RETURN)
        
        #The username and password accepted,i will be taken to the page for Administration
        #body = self.browser.find_element_by_tag_name('body')
        #self.assertIn('Site administration', body.text)
        
        #polls_links = self.browser.find_elements_by_link_text('Polls')
        #self.assertEquals(len(polls_links), 2)
        
        #self.fail('todo: finish tests')
        
        
class PollsViewsTestCase(TestCase):
    def test_index(self):
		poll_1=Poll.objects.create(question='Are you a student?',pub_date=datetime.datetime(2013, 11, 17, 9, 34))
		poll_1.save()
		choice_1=Choice.objects.create(poll=poll_1, choice_text='Yes', votes=0)
		choice_2=Choice.objects.create(poll=poll_1, choice_text='No', votes=0)
		
		resp = self.client.get('/polls/')
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('latest_poll_list' in resp.context)
		self.assertEqual([poll.pk for poll  in resp.context['latest_poll_list']], [1])
		
			
