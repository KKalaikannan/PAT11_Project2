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

    def test_AddEmp_Emergency_Contactdetails(self,booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().Pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EmpName_locator).send_keys(data.Add_Employee_Data().Search_Emp_Name)
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().SearchButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EditButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Emp_EmergencyContact_Locators().EmergencyContact_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Emp_EmergencyContact_Locators().ContactAddbutton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Emp_EmergencyContact_Locators().EmergencyContactName_locator).send_keys(data.Emp_EmergencyContact_Data().EmergencyContactName)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_EmergencyContact_Locators().Relationship_locator).send_keys(data.Emp_EmergencyContact_Data().Relationship)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_EmergencyContact_Locators().EmergencyContactNo_locator).send_keys(data.Emp_EmergencyContact_Data().EmergencyContactNo)
        self.driver.find_element(by=By.XPATH, value=locator.Emp_EmergencyContact_Locators().Savebutton5_locator).click()
        assert self.driver.title == 'OrangeHRM'

    def test_AddEmp_Dependentsdetails(self,booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().Pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EmpName_locator).send_keys(data.Add_Employee_Data().Search_Emp_Name)
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().SearchButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EditButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Dependents_Locators().Dependent_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Dependents_Locators().Add_Dependent_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Dependents_Locators().DependentName_locator).send_keys(data.Emp_DependentContact_Data().Dependent_Name)
        self.driver.find_element(by=By.XPATH, value=locator.Dependents_Locators().RelationshipDD_locator).click()
        sleep(2)
        pyautogui.press("down")
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locator.Dependents_Locators().DependentDOB_locator).send_keys(data.Emp_DependentContact_Data().Dependent_DOB)
        self.driver.find_element(by=By.XPATH, value=locator.Dependents_Locators().Savebutton6_locator).click()
        assert self.driver.title == 'OrangeHRM'

   

        





    









    







    