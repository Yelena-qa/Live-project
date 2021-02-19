from LIB import LIB
from POM.HOME import Home 
from POM.Sign_in import Sign_in 
import json 
import pytest


'''
Scenario steps
1. Go to URL
2. Click to Sign In Home Page
3.Fill email address
4.Click Sign In button
5. Verify that you signed successfully

'''

def test_2():
    try:
        # get emailand pass from config
        # with open('config.json') as f:
        #    data=jsonload(f)
        # email_address=data['email']
        # password     =data['password]   

        #open browser   
        obj_lib = LIB()
        browser =obj_lib.open_browser()
        email=obj_lib.config_data['email']
        password=obj_lib.config['password']

        #navigate to url  
        obj_lib=Home(browser)
        
        #Create Home page object  
        obj_home=Home(browser)

        #click on Sign in 
        browser.find_element(*obj_home.sign_in).click()  


        #create Sign in obj  
        onj_signin=Sign_in(browser)

        #submit with email and pass  
        obj_lib.wait_for_element(browser,obg_sighin.email_address)
        browser.find_element(*obj_signin.email).send_keys(email_address)
       browser.find_element(*obj_signin.email).send_keys(password)

       #click on sign in button 
       browser.find_element(*obg_signin.my_account_title)

       print('pass')

       except Exception as e:
           print(e)
           obg_lib.save_screeshot(browser)
           print('test is failed')

        finally:
            obj_lib.close_browser(browser) 


test_2()      