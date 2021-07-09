from selenium import webdriver
from pyvirtualdisplay import Display
  
# Taking input from user
search_string = input("Input the URL or string you want to search for:")
  
# This is done to structure the string 
# into search url.(This can be ignored)
search_string = search_string.replace(' ', '+') 
  
# Assigning the browser variable with chromedriver of Chrome.
# Any other browser and its respective webdriver 
# like geckodriver for Mozilla Firefox can be used
display = Display(visible=0, size=(800, 800))  
display.start()
browser = webdriver.Chrome('chromedriver')
  
for i in range(1):
    browser.get("https://www.google.com/search?q="+search_string+"&start=" + str(i))