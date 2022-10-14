## IMPORTS ##


from unicodedata import name
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import quote
from re import fullmatch

import time
import dateBase as dB
import setBrowser as sB



message = "Olá, {name}, de {city}. \n Somos da Unidade Popular e tal ... \n Vimos que entrou em contato conosco nacionalmente ..."


## SCRIPT ##
"""
Uses Selenium to send a text
"""

list_contats = dB.Criar_lista_contatos()

# Loads browser
driver = sB.set_browser(sB.browser)

for i in list_contats.index:
        time.sleep(1)
        
        phone_no = list_contats.at[i,"Contato"]
        name_interesed = list_contats.at[i,"Nome"]
        city = list_contats.at[i,"Cidade"]

        # Goes to site
        site = f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message.format(name=name_interesed, city= city))}"
        driver.get(site)
        element = lambda d : d.find_elements(by=By.XPATH, value="//div//button/span[@data-icon='send']")
        
        time.sleep(4)
            
        # Waits until send is found (in case of login)
        loaded = WebDriverWait(driver, 1000).until(method=element, message="User never signed in")
        
        # Loads a send button
        driver.implicitly_wait(10)
        send = element(driver)[0]
        
        time.sleep(4)        
            
        # Clicks the send button
        send.click()     
                 
        # Sleeps for 5 secs to allow time for text to send before closing window
        time.sleep(5)        
            
# Closes windows
driver.close()