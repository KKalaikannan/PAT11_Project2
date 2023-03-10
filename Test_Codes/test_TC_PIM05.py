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

    def test_AddEmp_Contactdetails(self,booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().Pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EmpName_locator).send_keys(data.Add_Employee_Data().Search_Emp_Name)
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().SearchButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EditButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Emp_ContactDetails_Locators().Contactdetails_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Emp_ContactDetails_Locators().Street1_locator).send_keys(data.Emp_ContactDetails_Data().Street1)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_ContactDetails_Locators().Street2_locator).send_keys(data.Emp_ContactDetails_Data().Street2)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_ContactDetails_Locators().City_locator).send_keys(data.Emp_ContactDetails_Data().City)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_ContactDetails_Locators().State_locator).send_keys(data.Emp_ContactDetails_Data().State)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_ContactDetails_Locators().Pincode_locator).send_keys(data.Emp_ContactDetails_Data().Pincode)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_ContactDetails_Locators().CountryButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Emp_ContactDetails_Locators().Mobile_locator).send_keys(data.Emp_ContactDetails_Data().Mobile)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_ContactDetails_Locators().WorkEmail_locator).send_keys(data.Emp_ContactDetails_Data().Email)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_ContactDetails_Locators().SaveButton4_locator).click()
        assert self.driver.title == 'OrangeHRM'



    
