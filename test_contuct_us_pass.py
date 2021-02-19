from LIB import LIB
from POM.Contact_Us import Contact_Us 
from POM.Sign_in import Sign_in 
import json 
import pytest

'''
1.Go to URL
2.Click to Contact Us button
3.Fill all fields in Contact Us and click on Send button
4.Validate that success message displays
5.Close browser
'''

def test_1():
    try:
        #open browser
        obj_lib = LIB.open_browser()
        browser=obj_lib.open(browser) 

        #navigate to url  
        obj_lib.page_load(browser)
        

        #create contact_us object  
        obj_contuct_us=contact_us(browser)
        obj_home=Home(browser)

   
        #steps  
        obj_home.click_contuct_us(browser)
        obj_contact_us.choose_subject_head((ing(browser)
        obj_contact_us.input_email_address()
        obj_contact_us.input_order_reference()
        obj_contact_us.input_message()
        obj_contact_us.click_send_button()

        #Verify that message is sending successfull  
        success_message = onj_lib.get_data('contact_us_success_message')

        message_text=browser.find_element(*onj_contuct_us.success_message).txt 
        assert success_message in message_text 
        print('pass')

        except:_screenshot(browser)
        print('failed')

        finnaly:
        obj_lib.close_browser(browser)

test_1()