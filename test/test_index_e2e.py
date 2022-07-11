import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

PATH = "C:\\bin\\firefox_drivers\\geckodriver.exe"

class E2ETest(unittest.TestCase):


    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, executable_path = PATH, )
        self.driver.get('http://localhost:5000')
    
    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity', self.driver.title)

    def test_page_heading_is_named_entity_finder(self):
        heading = self._find('heading').text
        self.assertEqual("Named Entity Finder", heading)
    
   
    def test_page_has_input_for_text(self):
        input_element = self._find("text-input")
        self.assertIsNotNone(input_element)

    def test_page_has_button_for_submitting_text(self):
        submit_button = self._find('find-button')
        self.assertIsNotNone(submit_button)

    def test_page_has_ner_table(self):
        input_element = self._find("text-input")
        submit_button = self._find('find-button')
        input_element.send_keys('Toronto is more of a capital city than Ottawa')
        submit_button.click()
        table = self._find('ner-table')
        self.assertIsNotNone(table)

    def _find(self, val):
        return self.driver.find_element(By.CSS_SELECTOR, f"[data-test-id='{val}']")
    