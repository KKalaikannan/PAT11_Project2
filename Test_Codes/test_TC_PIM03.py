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
        yield
        self.driver.close()

    def test_AddEmployee(self,booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().Pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().AddButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().FirstName_locator).send_keys(data.Add_Employee_Data().First_Name)
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().SecondName_locator).send_keys(data.Add_Employee_Data().Middle_Name)
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().LastName_locator).send_keys(data.Add_Employee_Data().Last_Name)
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().CreateLogindetails_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().LoginUsername_locator).send_keys(data.Add_Employee_Data().Login_Username)
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().LoginPassword_locator).send_keys(data.Add_Employee_Data().Login_Password)
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().ConfirmPassword_locator).send_keys(data.Add_Employee_Data().Confirm_Password)
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().SaveButton1_locator).click()
        assert self.driver.title == 'OrangeHRM'



    






    