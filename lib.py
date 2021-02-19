from selenium import webdriver
from selenium.webdriver.support.ui import WebdriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains 
import json 
import os
import  sys 
#import pytest

'''
Lib class has the following methods
1.open_browser
2.page_load
3.write_to_file
4.move_to_element
5.move_to_elements
6.wait_for_elements
7.get_data
8.save_screenshot
9.close_browser 
'''  

class LIB:
    # create Chrome driver
    def open_browser(self):
        try:
            with open('config.json') as f:
                data=json.load(f)
            browser=webdriver.Chrome(data['driver_path'])
             browser.maximize_window()
             return browser
        except:
            print("Something went wrong during browser opening!") 

    # navigate to give url_page
    def page_load(self,browser):
        try:
            with open('config.json') as f:
                data=json.load(f)  
            browser.get(data['url'])
            except:
                print("Something wrong with page_load") 

    # open txt file write log name and write there given text
    def write_to_file (self,text):
        try:
            with open("log.txt","a")as file:
                return file.write("\n" + str(text))
        except:
            print("Error during writting to file !")

    # move to givvent element
    def move_to_element(self.browser,element):
        try:
            action=ActionChains(browser)
            action.move_to_element(elemnt).perform()
        except:
            print("Can not to move to given element !")

     # wait for given element to be vissible in UI  
     def move_to_elemnt(self,browser,element):
         try:
             WebdriverWait(browser,30).untill(EC.visibillity_of_eelement_located(element))
        except:
            print("Element is not visible") 

    # wait for given element to be vivible in UI
    def wait_for_element(self,browser,elements):
        try:
            WebDriverWait(browser,30).untill(EC.visibility_of_any_elements_located(elemennts))
        except:
            print("Elements are not visible !") 

    #data parsing  
    def get_data(self,key):
        try:
            with open('data.json') as f:
                data=json.load(f)
            return data[key] 
        except:
        print("Error diring data getting!")


    # save screenshot  
    def save_screeshot(self,browser):
        current_filename = os.path.basename(sys.argv[0][:-3])
        try:
            browser.save_screenshot(f'Test\\{current_filename}_screenshot.png')   
        except:
            print("Screenshot is nor saved!")
    
    #close browser(self,browser):
    try:
        browser.quit()
    except:
        print("Driver is not closed!")



                             