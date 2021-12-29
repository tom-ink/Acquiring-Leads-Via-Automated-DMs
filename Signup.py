# Importing relevant libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

# Reading the csv file containing the email addresses as well as the first name and last name of the accounts to be created.
old_email=pd.read_csv("New_Email_Accounts_1.csv")
email=old_email['Emails'].values.tolist()
first_names=pd.read_csv("First_Names.csv")
first_name=first_names['FirstName'].values.tolist()
last_names=pd.read_csv("Last_Names.csv")
last_name=last_names['LastName'].values.tolist()
count=0

# Automating the account creation process
for email_number in email:
    count+=1
    
    # Activating the chrome driver
    PATH = "C:\Python Extensions\chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    
    # Going to the platform's signup website
    driver.get("https://www.yx[.]com/")
    time.sleep(10)
    driver.get("https://www.yx[.]com/signup/")
    time.sleep(8)
    
    # Signing up
    insert_email = driver.find_element_by_css_selector('input#input-email')
    insert_email.send_keys(f'{email_number}')
    time.sleep(10)
    insert_email.send_keys(Keys.RETURN)
    time.sleep(10)
    insert_email.send_keys(Keys.RETURN)
    time.sleep(6)
    insert_first_name = driver.find_element_by_css_selector('input#first-name-input')
    insert_first_name.send_keys(f'{first_name[count]}')
    time.sleep(7)
    insert_last_name = driver.find_element_by_css_selector('input#last-name-input')
    insert_last_name.send_keys(f'{last_name[count]}')
    time.sleep(10)
    insert_password = driver.find_element_by_css_selector('input#password-input')
    insert_password.send_keys('P@ssw0rd')
    time.sleep(6)
    
    # Going through the onboarding process after successful registration
    insert_country = driver.find_element_by_css_selector('button.up-btn.up-btn-default.up-dropdown-toggle')
    driver.find_element_by_css_selector('button.up-btn.up-btn-default.up-dropdown-toggle').click()
    time.sleep(7)
    insert_country.send_keys('singapore singapore')
    time.sleep(10)
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(7)
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(7)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(7)
    driver.find_element_by_css_selector('label#button-role-hire').click()
    time.sleep(10)
    driver.find_element_by_css_selector('label#button-role-hire').click()
    time.sleep(7)
    driver.find_element_by_css_selector('input#checkbox-promo+span.up-checkbox-replacement-helper').click()
    time.sleep(7)
    driver.find_element_by_css_selector('input#checkbox-terms+span.up-checkbox-replacement-helper').click()
    time.sleep(10)
    driver.find_element_by_css_selector('button#button-submit-second-step').click()

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id*=title-]")))

    # Selecting the relevant members on the platform for DMing 
    headline_one = driver.find_element_by_css_selector('input[id*=title-]')
    headline_one.send_keys('Singapore')
    time.sleep(20)
    driver.find_element_by_css_selector('button.up-btn.up-btn-primary.mb-0.mr-0').click()
    time.sleep(15)
    driver.find_element_by_css_selector('div.up-skill-badge:nth-of-type(1)').click()
    time.sleep(15)
    driver.find_element_by_css_selector('div.up-skill-badge:nth-of-type(2)').click()
    time.sleep(10)
    driver.find_element_by_css_selector('button.up-btn.up-btn-primary.mb-0.mr-0').click()
    time.sleep(15)
    driver.find_element_by_css_selector('div.up-radio:first-of-type>label.up-checkbox-label>span.up-checkbox-replacement-helper').click()
    time.sleep(10)
    driver.find_element_by_css_selector('div.up-radio:first-of-type>label.up-checkbox-label>span.up-checkbox-replacement-helper').click()
    time.sleep(10)
    driver.find_element_by_css_selector('div.up-radio:first-of-type>label.up-checkbox-label>span.up-checkbox-replacement-helper').click()
    time.sleep(15)
    driver.find_element_by_css_selector('button.up-btn.up-btn-primary.mb-0.mr-0').click()
    time.sleep(15)
    driver.find_element_by_css_selector('button.up-btn.up-btn-primary.mb-0.mr-0').click()
    time.sleep(10)
    job_description = driver.find_element_by_css_selector('textarea[class*=up-textarea]')
    job_description.send_keys('Singapore')
    time.sleep(15)
    driver.find_element_by_css_selector('button.up-btn.up-btn-primary.mb-0.mr-0').click()
    time.sleep(20)
    
    # Finishing the onboarding process
    try:
        driver.find_element_by_css_selector('div.breadcrumb>a:nth-child(1)').click()
        time.sleep(15)
        driver.find_element_by_partial_link_text('Private').click()
        time.sleep(15)
        driver.close()
    except NoSuchElementException:
        driver.get("https://www.yx.com/")
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.break")))
        time.sleep(10)
        driver.find_element_by_css_selector('a.break').click()
        time.sleep(5)
        driver.find_element_by_css_selector('div.breadcrumb>a:nth-child(1)').click()
        time.sleep(15)
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Make private')))
        time.sleep(5)
        driver.find_element_by_partial_link_text('Private').click()
        time.sleep(15)
        driver.close()
    # time.sleep(600)   # In order to avoid being wrongly identified as DoS 