# @title:   script fill  form & statics
# @date:    7/05/2018
# @author:  <MEG>
#
from selenium import webdriver


driver = webdriver.Chrome('chromedriver')
driver.get('http://www.ifts12online.com.ar/campus/')

loginuser = driver.find_element_by_id('login')
password  = driver.find_element_by_id('password')
loginuser.send_keys("") # poner usuario 
password.send_keys("")  # poner password

# open session
driver.find_element_by_name('submitAuth').click()


# inside campus #


# analytics basura
driver.get("http://www.ifts12online.com.ar/campus/claroline/tracking/userReport.php?userId=2552")
statics = driver.find_elements_by_class_name("claroTable")
for row in statics:
    print(row.text)


# close session
driver.get('http://www.ifts12online.com.ar/campus/index.php?logout=true')

driver.close()
