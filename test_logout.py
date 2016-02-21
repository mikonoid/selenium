from pyvirtualdisplay import Display
from selenium import webdriver

usr="admin"
pwd="softserve"

url="http://37.139.56.28/enter.php"
display = Display(visible=0, size=(1024, 768))
display.start()

browser = webdriver.Firefox()
browser.get(url)

username = browser.find_element_by_name( "user" )
password = browser.find_element_by_name( "pass" )
submit   = browser.find_element_by_name( "submit")

username.send_keys(usr)
password.send_keys(pwd)

submit.click()


logout = browser.find_element_by_link_text("Logout")
logout.click()

enter = browser.find_element_by_name( "submit")

if enter.is_displayed():
    print("test passed")
else:
    print("test not passed")



browser.close() # Close the current window.
browser.quit() # Quit the driver and close every associated window.
display.stop()

