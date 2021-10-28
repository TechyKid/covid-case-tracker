from selenium import webdriver
from bs4 import BeautifulSoup as soup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage') 
driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)   
answer = input('Choose a country to find there number of Covid-19 cases, \n USA, UK, CA, IRE, BRA, DOM, IND or the World: ') 
if answer == 'World': 
    url = 'https://www.worldometers.info/coronavirus/#countries'
    driver.get(url)
    print('Finding Data...')
    time.sleep(1.5)
    print()
    worldcase = 'Confirmed Cases'
    worlddeaths = 'Confirmed Deaths'
    worldrecover = 'Recovered'
    print(worldcase)
    worldcases = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[1]/td[3]').text)
    print()
    print(worlddeaths)
    worlddeaths = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[1]/td[5]').text)
    print()
    print(worldrecover)
    worldrecovered = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[1]/td[7]').text)
    print('-------------------------------------')
if answer == 'USA':
    usa = 'https://www.worldometers.info/coronavirus/#countries'
    driver.get(usa)
    print('Finding Data...')
    time.sleep(1.5)
    print()
    case = 'Confirmed Cases'
    deaths = 'Confirmed Deaths'
    recovered = 'Recovered'
    print(case)
    usacases = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[5]/td[3]').text)
    print()
    print(deaths)
    usadeaths = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[5]/td[5]').text)
    print()
    print(recovered)
    usarecovered = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[5]/td[7]').text)
    print('-------------------------------------')
if answer == 'UK':
    uk = 'https://www.worldometers.info/coronavirus/#countries'
    driver.get(uk)
    print('Finding Data...')
    time.sleep(1.5)
    print()
    ukcase = 'Confirmed Cases'
    ukdeaths = 'Confirmed Deaths'
    ukrecovered = 'Recovered'
    print(ukcase)
    ukcases = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[9]/td[3]').text)
    print()
    print(ukdeaths)
    ukdeaths = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[9]/td[5]').text)
    print()
    print(ukrecovered)
    ukrecovered = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[9]/td[7]').text)
    print('-------------------------------------')
if answer == 'CA':
    ca = 'https://www.worldometers.info/coronavirus/#countries'
    driver.get(ca)
    print('Finding Data...')
    time.sleep(1.5)
    print()
    cacase = 'Confirmed Cases'
    cadeaths = 'Confirmed Deaths'
    carecovered = 'Recovered'
    print(cacase)
    cacases = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[33]/td[3]').text)
    print()
    print(cadeaths)
    cadeaths = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[33]/td[5]').text)
    print()
    print(carecovered)
    carecovered = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[33]/td[7]').text)
    print('-------------------------------------')
if answer == 'IRE':
    ire = 'https://www.worldometers.info/coronavirus/#countries'
    driver.get(ire)
    print('Finding Data...')
    time.sleep(1.5)
    print()
    irecase = 'Confirmed Cases'
    iredeaths = 'Confirmed Deaths'
    irerecovered = 'Recovered'
    print(irecase)
    ircases = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[71]/td[3]').text)
    print()
    print(iredeaths)
    iredeaths = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[71]/td[5]').text)
    print()
    print(irerecovered)
    irerecoveed = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[71]/td[7]/span').text)
    print('-------------------------------------')
if answer == 'BRA':
    bra = 'https://www.worldometers.info/coronavirus/#countries'
    driver.get(bra)
    print('Finding Data...')
    time.sleep(1.5)
    print()
    bracase = 'Confirmed Cases'
    bradeaths = 'Confirmed Deaths'
    brarecovered = 'Recovered'
    print(bracase)
    bracases = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[8]/td[3]').text)
    print()
    print(bradeaths)
    bradeaths = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[8]/td[5]').text)
    print()
    print(brarecovered)
    recovered = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[8]/td[7]').text)
    print('-------------------------------------')
if answer == 'DOM':
    dom = 'https://www.worldometers.info/coronavirus/#countries'
    driver.get(dom)
    print('Finding Data...')
    time.sleep(1.5)
    print()
    domcase = 'Confirmed Cases'
    domdeaths = 'Confirmed Deaths'
    domrecovered = 'Recovered'
    print(domcase)
    domcases = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[78]/td[3]').text)
    print()
    print(domdeaths)
    domdeaths = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[78]/td[5]').text)
    print()
    print(domrecovered)
    domrecovered = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[78]/td[7]').text)
    print('-------------------------------------')
if answer == 'IND':
    ind = 'https://www.worldometers.info/coronavirus/#countries'
    driver.get(ind)
    print('Finding Data...')
    time.sleep(1.5)
    print()
    indcase = 'Confirmed Cases'
    inddeaths = 'Confirmed Deaths'
    indrecovered = 'Recovered'
    print(indcase)
    indcases = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[78]/td[3]').text)
    print()
    print(inddeaths)
    inddeaths = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[78]/td[5]').text)
    print()
    print(indrecovered)
    indrecovered = print(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[78]/td[7]').text)
    print('-------------------------------------')
