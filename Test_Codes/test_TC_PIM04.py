from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from Test_Locator import locator
from Test_Data import data
import pyautogui
import pytest

class Test_OHRM:
   
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_Employee(self,booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().Pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EmpName_locator).send_keys(data.Add_Employee_Data().Search_Emp_Name)
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().SearchButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EditButton_locator).click()
        assert self.driver.title == 'OrangeHRM'


    def test_AddEmp_Personaldetails(self,booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().Pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EmpName_locator).send_keys(data.Add_Employee_Data().Search_Emp_Name)
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().SearchButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EditButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Emp_PersonalDetails_Locators().OtherID_locator).send_keys(data.PersonalDetails_Data().Other_ID)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_PersonalDetails_Locators().LicenseNO_locator).send_keys(data.PersonalDetails_Data().License_Number)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_PersonalDetails_Locators().LicenseExpDate_locator).send_keys(data.PersonalDetails_Data().License_ExpiryDate)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_PersonalDetails_Locators().SsnNum_locator).send_keys(data.PersonalDetails_Data().Ssn_Number)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_PersonalDetails_Locators().SinNum_locator).send_keys(data.PersonalDetails_Data().Sin_Number)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_PersonalDetails_Locators().Nationality_locator).click()
        pyautogui.press("down")
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_PersonalDetails_Locators().Marital_locator).click()
        pyautogui.press("down")
        self.driver.find_element(by=By.XPATH, value=locator.Emp_PersonalDetails_Locators().DateofBirth_locator).send_keys(data.PersonalDetails_Data().DateofBirth)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_PersonalDetails_Locators().Gender_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Emp_PersonalDetails_Locators().SaveButton2_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Emp_PersonalDetails_Locators().Bloodgroup_locator).click()
        pyautogui.press("down")
        self.driver.find_element(by=By.XPATH, value=locator.Emp_PersonalDetails_Locators().SaveButton2_locator).click()
        assert self.driver.title == 'OrangeHRM'




        

