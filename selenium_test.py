from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome() # Get local session of Chrome
browser.get("http://www.baidu.com") # Load page
assert "Yahoo" in browser.title
elem = browser.find_element_by_id("uh-search-box") # Find the query box
elem.send_keys("qq" + Keys.RETURN)
time.sleep(0.2) # Let the page load, will be added to the API
