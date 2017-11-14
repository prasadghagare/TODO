from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_A_list_And_retrieve_later(self):

        self.browser.get("http://localhost:5000")

        self.assertIn ('To-Do' , self.browser.title)

        #self.fail('Finish the test!')

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a To-Do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        #time.sleep(2)

        #The book adds csrf protection by adding template syntax in HTML for Django projects.
        #But Flask/Jinja doesnt have this template as Flask takes care by avoiding form
        #validation framework, flask-wtf provides form validation and it provides this CSRF protection

        #The test fails though, exactly with same error but the reason is that in route we have not yet declared
        #the method as POST

        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        #Now we add another item to list and check both are present
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('use peacock feather to make hen')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: use peacock feather to make hen')
        """self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )"""
        self.browser.quit()

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)

    def test_multiple_users_can_start_lists_at_different_url(self):
        #self.browser = webdriver.Firefox()
        #Edith starts a list
        self.browser.get("http://localhost:5000")
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        #Check that the list has unique URL
        edith_list_url = self.browser.current_url
        #Check that the URL is RESTish, assertRegex is from unittest module
        self.assertRegexpMatches(edith_list_url, '/lists/.+')

        #Now a new user comes and starts list
        #For mocking new user, we exit current browser instance(session)
        self.browser.quit()
        #Start a new session
        self.browser = webdriver.Firefox()
        #Now next user , Fracis visits the site
        self.browser.get("http://localhost:5000")
        #Following code checks there is no any signs of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make hen', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #Again, following code checks there is no any signs of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make hen', page_text)

if __name__ == '__main__':
    unittest.main()
