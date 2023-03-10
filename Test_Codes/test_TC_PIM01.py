from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from Test_Locator import locator
from Test_Data import data
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class Test_OHRM:
   
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()

    def Search_Function(self):
        search = self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator)
        action = ActionChains(self.driver)
        action.double_click(search).perform()
        return
    
    def test_SearchBox(self, booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator).click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator).send_keys('Admin')
        self.Search_Function()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator).send_keys('Pim')
        self.Search_Function()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator).send_keys('Leave')
        self.Search_Function()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator).send_keys('Time')
        self.Search_Function()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator).send_keys('Recruitment')
        self.Search_Function()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator).send_keys('My')
        self.Search_Function()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator).send_keys('Performance')
        self.Search_Function()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator).send_keys('Dashboard')
        self.Search_Function()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator).send_keys('Directory')
        self.Search_Function()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator).send_keys('Maintenance')
        self.Search_Function()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().SearchOption_locator).send_keys('Buzz')
        assert self.driver.title == 'OrangeHRM'
