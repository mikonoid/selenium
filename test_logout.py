from pyvirtualdisplay import Display
from selenium import webdriver

usr="admin"
pwd="softserve"
url="http://37.139.56.28/enter.php"

#init display for browser

display = Display(visible=0, size=(1024, 768))
display.start()

browser = webdriver.Firefox()
browser.get(url)

#looking for elements for auth

username = browser.find_element_by_name( "user" )
password = browser.find_element_by_name( "pass" )
submit   = browser.find_element_by_name( "submit")

username.send_keys(usr)
password.send_keys(pwd)

submit.click()

#looking for link "Logout"
logout = browser.find_element_by_link_text("Logout")
logout.click()

#try testing

enter = browser.find_element_by_name( "submit")

if enter.is_displayed():
    print("test passed")
else:
    print("test not passed")

##close browser and display
browser.close()
browser.quit()
display.stop()

