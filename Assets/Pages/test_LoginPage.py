'''
Created on 07-Apr-2021

@author: Ganga
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage():
    
              
    def __init__(self, driver):
        self.driver = driver
        

   
    def go(self):
        self.driver.get(self.url)    

 
        
    def enter_username(self,text):
        username_xpath = "//input[@id='emailOrUsername']"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, username_xpath))).send_keys(text)
              
            
    def enter_password(self,text):    
        password_xpath = "//input[@id='pass']"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, password_xpath))).send_keys(text)

        
    def click_login_button(self):    
        login_btn_xpath = "//span[contains(text(),'Login')]"
        self.driver.find_element_by_xpath(login_btn_xpath).click()
        
    def get_login_btn_text(self):
        login_btn_xpath = "//span[contains(text(),'Login')]"
        login_btn_text = self.driver.find_element_by_xpath(login_btn_xpath).text
        return login_btn_text

