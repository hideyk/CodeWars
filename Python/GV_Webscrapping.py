import time
import os
from selenium import webdriver
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#my_url = "https://www.lazada.sg/catalog/?q=prism%2B&_keyori=ss&from=input&spm=a2o42.home.search.go.654346b5dBnRCC"
my_url = "https://www.google.com.sg/?gws_rd=ssl"
search_word = "lazada"
# Beautiful soup
# uClient = uReq(my_url)
# page_html = uClient.read()
# uClient.close()
# page_soup = soup(page_html, "html.parser")
# containers = page_soup.findAll("div", {"class": "c3gUW0"})
# print(containers)

# containers = page_soup.findAll("div", {"id": "root"})

# Selenium
# chrome_opts = webdriver.ChromeOptions()
# chrome_opts.add_argument("--incognito")

driver = webdriver.Chrome()
driver.get(my_url)
driver.implicitly_wait(5)
google_search = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
google_search.send_keys(search_word)
google_search.send_keys(Keys.RETURN)
driver.implicitly_wait(5)

results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
results[0].click() # clicks the first one
driver.implicitly_wait(5)

lazada_search = driver.find_element_by_css_selector("input[placeholder='Search in Lazada']")
lazada_search.send_keys("prism+")
lazada_search.send_keys(Keys.RETURN)
driver.implicitly_wait(5)

html = driver.page_source
page_soup = soup(html, "html.parser")
containers = page_soup.findAll("div", {"class": "c3KeDq"})
print(containers)
for i in range(len(containers)):
    container = containers[i]
    print(container)
    product = container.find("div", {"class": "c16H9d"})["title"]
#     price = container.find("div", {"class": "c3gUW0"})
#     print(product)
#     print(price)


driver.quit()


#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(5) # Let the user actually see something!
#driver.quit()