from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import csv

browser = webdriver.Firefox()
browser.get('https://www.nyse.com/listings_directory/stock')

symbol_list = []

garbage=1

def write_to_csv(company):
    with open('/home/h1ro/Documents/nyse_symbols', mode='a') as file:
        file_writer = csv.writer(file, delimiter='\n', lineterminator='\n', quoting=csv.QUOTE_NONE,escapechar='\\')
        file_writer.writerow(company)

while True:
    table_data = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//table//td")))
    for i in range(1, len(table_data)+1):
        td_text = browser.find_element_by_xpath("(//table//td)["+str(i)+"]").text
        if(not garbage%2==0):
            symbol_list.append(td_text)
            write_to_csv(symbol_list)
            symbol_list=[]
        garbage+=1
       
    try:
        print("Go to next page ...")
        next_page = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#" and contains(text(),"Next")]')))
        next_page.click()
        sleep(3)
    except Exception as e:
        print(e)
        print("This is last page.")
        break



