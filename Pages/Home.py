from Lib import LIB 
from selenium.webdriver.common.by import.BY 


class Home:

    #locators 
    logo           =(By.XPATH, "//*[@id='header_logo']//img")
    contact_us     =(By.ID,'contact-link')
    sign_in        =(By.XPATH,"//*[@id='header']//a[@class='login']")
    search_btn     =(By.XPATH,"//*[@id='searchbox']//button[@type='submit]")
    search_input   =(By.ID ,"search_query_top")

    
    def __init__(self, driver):
        self.driver=driver

    url=config.data['url']
    sign_in = data.txt['sign_in']
        
        
    def open_site(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        try:

     #click Contact_us  
     def click_contuct_us(self,browser):
         LIB.wait_for_element(self.browser,self.contact_us)       
         self..browser.find_element(*self.contact_us).click()

        
    
  
            
            
    
    