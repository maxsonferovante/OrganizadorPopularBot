## IMPORTS ##


from unicodedata import name
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import quote
from re import fullmatch

import time
import dateBase as dB
import setBrowser as sB



## SCRIPT ##
"""
Uses Selenium to send a text
"""
def dbReadListContats():
        return dB.Criar_lista_contatos()

def botSendMensage(driver, phone_no, name_interesed, message):
        pass
                