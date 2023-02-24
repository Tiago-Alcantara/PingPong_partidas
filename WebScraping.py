import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Grab content from URL (Pegar conteúdo HTML a partir da URL)
url = "https://www.betsul.com/esportes/tenis-de-mesa/internacional/tt-elite-series"

option = Options()
option.headless = True
driver = webdriver.Firefox()
driver.get(url)

time.sleep(5)

driver.find_element(By.XPATH ,'/html/body/footer/div[1]/div/div[2]/button[1]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]').click()
driver.find_element(By.XPATH, "//div[@class ='wcl-PageContainer wcl-PageContainer_State1 wcl-PageContainer-scrollable']//div//div//div//div[@class= 'cm-CouponModule']").click()


print(driver)
# Parse HTML (Parsear o conteúdo HTML) - BeaultifulSoup

# Data Structure Conversion (Estruturar conteúdo em um Data Frame) - Pandas
# Convert to Dict (Transformar os Dados em um Dicionário de dados próprio)
#driver.quit()
# Dump and Save to JSON file (Converter e salvar em um arquivo JSON)