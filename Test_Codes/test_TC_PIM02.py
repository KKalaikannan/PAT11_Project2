from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from Test_Locator import locator
from Test_Data import data
import pytest

class Test_OHRM:
   
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()
   
    # Test Login
    def test_Login(self, booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        assert self.driver.title == 'OrangeHRM'
       
    def test_AdminMenu(self,booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().AdminMenu_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().UserManagement_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().User_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().UserRole_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Admin_Locators().Status_locator).click()
        assert self.driver.title == 'OrangeHRM'



       
