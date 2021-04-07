'''
Created on 07-Apr-2021

@author: Ganga
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class ChatPage():
    
    def __init__(self, driver):
        self.driver = driver 
        
    def enter_userinput(self,text):
        usermessage_xpath = "//textarea[@placeholder='Message']"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, usermessage_xpath))).send_keys(text)        
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, usermessage_xpath))).send_keys(Keys.ENTER)  
            
    def get_userinput(self):    
        usertext_xpath = "(//button[text()='ethanadmin'])[last()]//following::div[1]"
        userinput = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, usertext_xpath))).text
        return userinput
        print(userinput)
        
    def get_botoutput(self):    
        botoutput_xpath = "(//button[text()='bot'])[last()]//following::div[1]"
        botoutput = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, botoutput_xpath))).text
        return botoutput
        print(botoutput)
        
    def click_accountmenu_sidebar(self):
        accountmenu_sidebar_xpath = "//*[@class='rc-icon sidebar__account-menu sidebar__account-menu--menu']"
        WebDriverWait(self.driver,50).until(EC.element_to_be_clickable((By.XPATH, accountmenu_sidebar_xpath))).click()
        
    def click_logout(self):  
        logout_xpath = "//span[contains(text(),'Logout')]"
        WebDriverWait(self.driver,50).until(EC.element_to_be_clickable((By.XPATH, logout_xpath))).click()
        
