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

# Activating the chrome driver
PATH = "C:\FILENAME\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Logging in to a different account after every 100 DMs sent
driver.get("https://www.yx.com/login")
old_email=pd.read_csv("New_Email_Accounts.csv")
email=old_email['Emails'].values.tolist()
number_count=0
for email_number in email:
    number_count+=1
    search1 = driver.find_element_by_css_selector('input#login_username')
    search1.send_keys(f'{email_number}')
    time.sleep(25)
    search1.send_keys(Keys.RETURN)
    time.sleep(25)
    search2 = driver.find_element_by_css_selector('input.up-input')
    search2.send_keys('Brokeman98')
    time.sleep(35)
    search2.send_keys(Keys.RETURN)
    time.sleep(35)
    
    # Collecting the first names of the members appearing on the platform
    namelist=[]
    for i in range(number_count,(number_count+10)): 
        driver.get('https://www.yx.com/profile/page='+str(i))
        namelistclear=[]
        for el in driver.find_elements_by_css_selector('div.identity-name'):
            namelist.append(el.text)
            namelistclear.append(el.text)
        newnamelistclear=[x[:-3] for x in namelistclear]    

        time.sleep(25)
        
        # Preparing to send the DMs to 100 prospects
        for row in range(0,10):
            driver.find_element_by_css_selector(f"div.up-card-section:nth-child({3+row}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(2)").click()
            time.sleep(25)
            driver.find_element_by_css_selector('textarea#interview-invitation-popup-message').clear()
            time.sleep(25)
            
            # Inputing the single lead generation message with the prospect's first name 
            driver.find_element_by_css_selector('textarea#interview-invitation-popup-message').send_keys(f'''Hi {newnamelistclear[row]},
INTRO + A/B TESTED LEAD GENERATION MESSAGE''')
            time.sleep(25)
            
            # Send the DM to a prospect
            invite=driver.find_element_by_css_selector('.mb-0.up-btn.up-btn-primary').text
            if invite=='Send':
                driver.find_element_by_css_selector('.mb-0.up-btn.up-btn-primary').click()
                time.sleep(25)
            elif invite=='Upgrade':
                webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
                time.sleep(25)
                webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
                time.sleep(25)
                webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
                time.sleep(25)
                webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
                time.sleep(25)
                driver.find_element_by_css_selector('.mb-0.up-btn.up-btn-primary').click()
                time.sleep(25)
                
                # If an error occur after sending the DM, record the last prospect who received our DM and break the script
            else:
                pd.DataFrame(namelist).to_csv(f'Name {number_count}.csv')
                break