from selenium.webdriver.common.by import By

class MainPageLocators:
    SEARCH_BOX = (By.NAME, "q")  
    GO_BUTTON = (By.ID, "submit")  

class SearchResultsPageLocators:
    NO_RESULTS_TEXT = "No results found."
