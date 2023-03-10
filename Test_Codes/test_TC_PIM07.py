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


    def test_AddEmp_Jobsdetails(self,booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().Pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EmpName_locator).send_keys(data.Add_Employee_Data().Search_Emp_Name)
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().SearchButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EditButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().Job_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().Joineddate_locator).send_keys(data.Emp_JobDetails_Data().Joined_Date)
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().Jobtitle_locator).click()
        sleep(2)
        pyautogui.press("down")
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().JobCategory_locator).click()
        pyautogui.press("down")
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().SubUnit_locator).click()
        pyautogui.press("down")
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().JobLocation_locator).click()
        pyautogui.press("down")
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().Employmentstatus_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().Permanent_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().Inclbutton_Empl_Contract_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().ContStartdate_locator).send_keys(data.Emp_JobDetails_Data().Cont_Start_Date)
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().ContEnddate_locator).send_keys(data.Emp_JobDetails_Data().Cont_End_Date)
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().Savebutton7_locator).click()
        assert self.driver.title == 'OrangeHRM'

    def test_Employee_Termination_details(self,booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().Pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EmpName_locator).send_keys(data.Add_Employee_Data().Search_Emp_Name)
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().SearchButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EditButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().Job_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().TerminateEmployee_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().TerminateDate_locator).send_keys(data.Emp_JobDetails_Data().Terminate_Date)
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().TerminateReason_locator).click()
        sleep(2)
        pyautogui.press("down")
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().Note_locator).send_keys(data.Emp_JobDetails_Data().Note)
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().Savebutton8_locator).click()
        assert self.driver.title == 'OrangeHRM'


    def test_Employee_Activation(self,booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().Pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EmpName_locator).send_keys(data.Add_Employee_Data().Search_Emp_Name)
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().SearchButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EditButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().Job_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.JOB_Details_Locators().ActivateEmployee_locator).click()
        assert self.driver.title == 'OrangeHRM'
