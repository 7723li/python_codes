from selenium import webdriver as wd
import time

driver=wd.Chrome()
print('done 1')
driver.get("http://www.taobao.com")
time.sleep(5)
driver.quit()
