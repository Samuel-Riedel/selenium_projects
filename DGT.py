from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://sede.dgt.gob.es/es/otros-tramites/cita-previa/")

time.sleep(5)
div_element = driver.find_element(By.CLASS_NAME, 'div-ico-dgt')
link_element = div_element.find_element(By.TAG_NAME, 'a')
link_element.click()


time.sleep(2)
search_text = "Barcelona"
element = WebDriverWait(driver, 15).until(
   EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{search_text}')]" ))
)


driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(5)
element.click()

#################################################################################################
# Below Here we select office #
time.sleep(5)
second_div_element = driver.find_element(By.CLASS_NAME, 'buscIntCamposEvProvSelect subeCombo')
time.sleep(1)
element = WebDriverWait(driver, 15).until(
   EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{search_text}')]" ))
)
element.click()









"""WebDriverWait(driver,50).until(
    EC.presence_of_element_located((By.CLASS_NAME, "div-ico-dgt"))
)"""




#WebDriverWait(driver, 15).until(
#   EC.presence_of_element_located((By.CLASS_NAME, "W0wltc"))
#)

#input_element = driver.find_element(By.CLASS_NAME, "W0wltc")
#button = driver.find_element(By.PARTIAL_LINK_TEXT, "W0wltc")

#input_element = driver.find_element(By.CLASS_NAME, "div-ico-dgt")
#input_element.send_keys(Keys.F5)

#input_element.send_keys("Hello" + Keys.ENTER)




time.sleep(10)

#driver.quit()