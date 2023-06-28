# Usage --
    # pip install selenium
    # python DuckDuckGo.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

os.system('cls' if os.name == 'nt' else 'clear')
print("""
██████╗  ██████╗ ██████╗ ██╗  ██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║  ██║██║   ██║██████╔╝█████╔╝     ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║  ██║██║   ██║██╔══██╗██╔═██╗     ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║  ██║██║  ██╗    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                                                                                              
┌┬┐┬ ┬┌─┐┬┌─┌┬┐┬ ┬┌─┐┬┌─┌─┐┌─┐                                                 
 │││ ││  ├┴┐ │││ ││  ├┴┐│ ┬│ │                                                 
─┴┘└─┘└─┘┴ ┴─┴┘└─┘└─┘┴ ┴└─┘└─┘                                                 
╔═╗┬─┐┌─┐┌─┐┌┬┐┌─┐┌┬┐  ╔╗ ┬ ┬  ╔╦╗┌─┐┌┐┌┌─┐┌─┐┬ ┬┬─┐╔═╗┌┐ ┌─┐┬ ┬┬ ┬┌─┐┬ ┬┌─┐┌┬┐
║  ├┬┘├┤ ├─┤ │ ├┤  ││  ╠╩╗└┬┘  ║║║├─┤│││└─┐│ ││ │├┬┘╠═╣├┴┐│ ││ │├─┤├─┤└┬┘├─┤ │ 
╚═╝┴└─└─┘┴ ┴ ┴ └─┘─┴┘  ╚═╝ ┴   ╩ ╩┴ ┴┘└┘└─┘└─┘└─┘┴└─╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴ ┴ ┴ ┴ ┴ 
""")
Query = input('Enter Your Query : ')

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
driver.get(f"https://duckduckgo.com/?q={Query}")

while(True):
    try:
        
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="more-results"]')))

        element.click()
    except:
        break


pageSource = driver.page_source
driver.quit()
if 'Make sure all words are spelled correctly.' in pageSource:
    exit('No Results Found.')
filename='Results'+str(datetime.date.today())+str(datetime.datetime.now().time())+'.txt'
print(filename)
file = open(filename, 'w')
urls = list(set(re.findall('</a></span><a href="(.*?)"',pageSource)))
for url in urls:
    print(url)
    file.write(url+'\n')


