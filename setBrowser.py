# Driver Managers
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium import webdriver
from selenium.webdriver.edge.service import Service
## RUNTIME VARIABLES ##
"""
Place the associated driver manager above depending on the browser you want to launch.
Selenium supports the following:
- Chrome
- Edge
- Firefox
- Opera
- Brave

Below the script is configured set to use an Edge browser. Be sure to change it according to the browser you use.
"""
browser = "Edge"

def set_browser(browser):
    install = lambda dm : dm.install()
    try:
        if (browser == "Edge"):
            bm = EdgeChromiumDriverManager()
            return webdriver.Edge(service=Service(install(bm)))
        elif (browser == "Chrome"):
            bm = ChromeDriverManager()
            return webdriver.Chrome(service=Service(install(bm)))
        elif (browser == "Firefox"):
            bm = GeckoDriverManager()
            return webdriver.Firefox(service=Service(install(bm)))
        elif (browser == "Opera"):
            bm = OperaDriverManager()
            return webdriver.Opera(service=Service(install(bm)))
    except:
        raise Exception("Browser not found")
