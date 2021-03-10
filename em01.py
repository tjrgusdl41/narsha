from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("C:\PY\chromedriver.exe")

browser.get("http://www.naver.com")

webtoon = browser.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[9]/a')
href = webtoon.get_attribute('href')
print(href)
#webtoon.click()

input_sear = browser.find_element_by_id('query')
input_sear.send_keys('python')

input_sear.send_keys(Keys.ENTER)

# elem = browser.find_element_by_link_text('위즈라이브')
# elem.get_attribute('href')
# elem.click()

elems = browser.find_elements_by_tag_name('a')
for e in elems :
    print("test")
    print(e.get_attribute('href'))

browser.save_screenshot("naver_python.png")

#어렵다 ㅠ
#애드
time.sleep(5)

browser.close()
browser.quit()