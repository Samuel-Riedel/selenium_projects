from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import os
from dotenv import load_dotenv

load_dotenv()


fb_username = "FB_MY_EMAIL"
fb_password = "FB_MY_PASSWORD"


timer = 35
profileTimer = 15
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com/?stype=lo&flo=1&deoia=1&jlou=AffagpcZgnYie2FFR4MAA5StkbXg14BOnQjbwExcGYY5nLKviv1hP8HHoBSUjQBc2JMMSHgSsJELbfovNkDY5TPw&smuh=26609&lh=Ac-IR-MwtEilomHInBU")


print("Looking for email input...")
#This code is for the username or email
time.sleep(10)
input_element = driver.find_element(By.ID, "email")
print("Success!")


#Here you insert username or email
print("Inserting Username")
time.sleep(2)
input_element.send_keys(fb_username)
print("Success!")



# This code block is for the password
print("Looking for Password input...")
time.sleep(2)
input_element = driver.find_element(By.ID, "pass")
print("Success!")


#Here you insert password
print("Inserting Password")
time.sleep(2)
input_element.send_keys(fb_password + Keys.ENTER)
print("Success!")


#This timer is for the 2fa waiting time
#time.sleep(35)
print("You have 35 seconds to approve log in")
while timer > 0:
    timer = timer - 1
    print(timer)
    time.sleep(1)

print("Success!")

#Here you click on open profile
print("Clicking on Profile")
time.sleep(5)
link = driver.find_element(By.LINK_TEXT, "PUT YOUR PROFILE NAME HERE")
link.click()
print("Success!")



print("Loading Profile")
while profileTimer > 0:
    profileTimer = profileTimer - 1
    print(f"{profileTimer} Seconds remaining")
    time.sleep(1)

# Here its going to click on 3 dots ( creo que debo solo buscar la clase y no hacer cs sselector )
#aria_label = "Actions for this post"
print("Loading three Dots part")
three_dots_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".xqcrz7y.x78zum5.x1qx5ct2.x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha.xw4jnvo"))
)
print("CSS_SELECTOR Found!")
print("About to click 3 dots")
time.sleep(5)
three_dots_button.click()
time.sleep(5)



#Here i will search inside the toggle for the words "Edit audience"
edit_audience = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "x1ey2m1c.xds687c.x17qophe.xg01cxk.x47corl.x10l6tqk.x13vifvy.x1ebt8du.x19991ni.x1dhq9h.x9jk4nr.x10vv0rk.x1mn05ot.x4u6ece"))
)

print(edit_audience)
time.sleep(10)
edit_audience.click()

time.sleep(30)

"""  
#Here the bot will click on "Only me"
only_me = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x676frb.x1lkfr7t.x1lbecb7.xk50ysn.xzsf02u.x1yc453h"))
)
print(only_me)
only_me.click()

time.sleep(100)


#Here the bot will click on "Save"
link = driver.find_element(By.LINK_TEXT, "Save")
link.click()

time.sleep(10)


"""
# Here its going to click on audiance using text

 
"x1ey2m1c xds687c x17qophe xg01cxk x47corl x10l6tqk x13vifvy x1ebt8du x19991ni x1dhq9h x9jk4nr x10vv0rk x1mn05ot x4u6ece"


# Here it will archive the post  this needs 3 second delay since it loads( doing this to make my job easier)

"html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x6s0dn4 x78zum5 x1q0g3np x1iyjqo2 x1qughib xeuugli"""