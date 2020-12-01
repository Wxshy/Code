'''
rom selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = 'C:/Users/samue/Documents/Code-LP/Code/hockey-league/chromedriver.exe'

driver = webdriver.Chrome(PATH)

webpage = 'https://www.flashscore.com/field-hockey/netherlands/hoofdklasse/'
driver.get(webpage)

idd = "box-table-type-1"

driver.find_element_by_id('li3').click()

teams = driver.find_element_by_id(idd)

print(teams)

driver.quit()
'''

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = '''http://www.englandhockey.co.uk/page.asp?section=67&sectionTitle=Men%27s+Hockey+League'''

PATH = 'C:/Users/samue/Documents/Code-LP/Code/hockey-league/chromedriver.exe'

driver = webdriver.Chrome(PATH)

page = requests.get(url)

driver.get(url)

driver.find_element_by_class_name(' first no-children')
