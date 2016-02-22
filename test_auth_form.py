from pyvirtualdisplay import Display
from selenium import webdriver

usr="admin"
pwd="softserve"
url="http://37.139.56.28/enter.php"

#init display for browser
display = Display(visible=0, size=(1024, 768))
display.start()

#start browser
browser = webdriver.Firefox()
browser.get(url)

#looking for elements for auth
username = browser.find_element_by_name( "user" )
password = browser.find_element_by_name( "pass" )
submit   = browser.find_element_by_name( "submit")

#enter login pass and click submit
username.send_keys(usr)
password.send_keys(pwd)
submit.click()

#try testing
try:
    elem = browser.find_element_by_link_text("Logout")
    if elem.is_displayed():
        print("auth test passed")
    else:
        print("auth test not passed")
except:
    print("auth test not passed")


#close browser and display
browser.close()
browser.quit()
display.stop()