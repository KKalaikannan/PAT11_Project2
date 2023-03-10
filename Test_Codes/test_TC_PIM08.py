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

    def test_AddEmp_Salarydetails(self,booting_function):
        self.driver.get(data.Login_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Username_locator).send_keys(data.Login_Data().username)
        self.driver.find_element(by=By.NAME, value=locator.OHRM_Locators().Password_locator).send_keys(data.Login_Data.password)
        self.driver.find_element(by=By.XPATH, value=locator.OHRM_Locators().LoginButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.Pim_Locators().Pim_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EmpName_locator).send_keys(data.Add_Employee_Data().Search_Emp_Name)
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().SearchButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SearchEmp_Locators().EditButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SalaryDetails_Locators().Salary_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SalaryDetails_Locators().AddSalaryButton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SalaryDetails_Locators().SalaryComponent_locator).send_keys(data.Emp_SalaryDetails_Data().Salary_Component)
        self.driver.find_element(by=By.XPATH, value=locator.SalaryDetails_Locators().SelectCurrency_locator).click()
        pyautogui.press("down")
        self.driver.find_element(by=By.XPATH, value=locator.SalaryDetails_Locators().SalaryAmount_locator).send_keys(data.Emp_SalaryDetails_Data().Salary_Amount)
        self.driver.find_element(by=By.XPATH, value=locator.SalaryDetails_Locators().IncludeDepositDetails_locator).click()
        self.driver.find_element(by=By.XPATH, value=locator.SalaryDetails_Locators().AcNo_locator).send_keys(data.Emp_SalaryDetails_Data().Salary_Amount)
        self.driver.find_element(by=By.XPATH, value=locator.SalaryDetails_Locators().AcType_locator).click()
        sleep(2)
        pyautogui.press("down")
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locator.SalaryDetails_Locators().RoutingNo_locator).send_keys(data.Emp_SalaryDetails_Data().Routing_No)
        self.driver.find_element(by=By.XPATH, value=locator.SalaryDetails_Locators().Amount_locator).send_keys(data.Emp_SalaryDetails_Data().Deposit_Amount)
        self.driver.find_element(by=By.XPATH, value=locator.SalaryDetails_Locators().SaveButton9_locator).click()
        assert self.driver.title == 'OrangeHRM'

















