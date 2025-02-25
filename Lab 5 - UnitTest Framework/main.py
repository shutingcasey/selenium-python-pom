import unittest
from selenium import webdriver
from page import MainPage, SearchResultPage

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.python.org")

    def test_search_python(self):
        main_page = MainPage(self.driver)
        
        self.assertTrue(main_page.is_title_matches())

        main_page.search_text_element = "pycon"
        main_page.click_go_button()

        search_result_page = SearchResultPage(self.driver)
        self.assertTrue(search_result_page.is_results_found())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
