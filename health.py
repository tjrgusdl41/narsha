import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

brow = webdriver.Chrome('C:\PY\chromedriver.exe')
brow.maximize_window()

brow.get('https://hcs.eduro.go.kr/')

#자가진단 버튼 클릭
elem = brow.find_element_by_xpath('//*[@id="btnConfirm2"]')
elem.click()

elem = brow.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button')
elem.click()
# 대구광역시 클릭
elem = brow.find_element_by_xpath('//*[@id="sidolabel"]/option[4]')
elem.click()

brow.find_element_by_xpath('//*[@id="crseScCode"]/option[5]').click()

elem = brow.find_element_by_xpath('//*[@id="orgname"]')
elem.send_keys('소프트웨어')
elem.send_keys(Keys.ENTER)
#바로안뜰수도있어서 1초쉼
time.sleep(1)

brow.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()
brow.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
elem = brow.find_element_by_xpath('//*[@id="user_name_input"]')
elem.send_keys('강석현')

elem = brow.find_element_by_xpath('//*[@id="birthday_input"]')
elem.send_keys('040910')
brow.find_element_by_xpath('//*[@id="btnConfirm"]').click()

time.sleep(1)

elem = brow.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input')
elem.send_keys('0910')  
brow.find_element_by_xpath('//*[@id="btnConfirm"]').click()

time.sleep(7)

brow.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/span[1]').click()
time.sleep(2)
brow.find_element_by_xpath('//*[@id="survey_q1a1"]').click()
brow.find_element_by_xpath('//*[@id="survey_q2a1"]').click()
brow.find_element_by_xpath('//*[@id="survey_q3a1"]').click()
brow.find_element_by_xpath('//*[@id="btnConfirm"]').click()
time.sleep(5)
brow.quit()