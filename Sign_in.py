from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains 
from selenim import webdriver

class Sign_in:
  contact_button  = (By.ID,"contact-link")
  message = test-data.text("m")
  subject_heading = (By.ID, "id_contact")
  choose = (By.XPATH,'//select[@id="id_contact"]/option[@value = 2]')
  email = congig.data["email"]
    


order_reference = (By.NAME, "id_contact")
attach_file = (By.ID,"fileUpload")
message_input = (By.ID,"message")
send_button = (By.ID,"submitMessage")
message_text = testdata.text("message_text")
error_message = (By.XPATH,'//div[@class="alert alert-danger"]/p')
success_message = (By.XPATH,'//div[@class="alert alert-success"]')

email_address = (By.ID,"email")


def __init__(self,browser):
  self.browser =browser









