import time
from selenium.webdriver.common.by import By
from seleniumbase import Driver
import datetime

"""
# Functions

# click function
def click_on(selector_type, path_to_element, wait_time):
    if selector_type == "id":
        click_element = driver.find_element(By.ID, path_to_element)
        click_element.click()
        time.sleep(wait_time)
    elif selector_type == "css":
        click_element = driver.find_element(By.CSS_SELECTOR, path_to_element)
        click_element.click()
        time.sleep(wait_time)


# type function
def write(selector_type, path_to_element, content, wait_time):
    if selector_type == "id":
        click_element = driver.find_element(By.ID, path_to_element)
        click_element.send_keys(content)
        time.sleep(wait_time)
    elif selector_type == "css":
        click_element = driver.find_element(By.CSS_SELECTOR, path_to_element)
        click_element.send_keys(content)
        time.sleep(wait_time)

# time difference in seconds function 
def time_difference_in_seconds(hour, minute):
    # get current time
    current_time = datetime.datetime.now().time() #16:48:33.441141, datetime.time object
    #current_time_value = datetime.datetime.strptime(str(current_time), "%H:%M:%S:%SS")
    i = type(current_time)
    current_delta = datetime.timedelta(hours=current_time.hour, minutes=current_time.minute, seconds=current_time.second)

    # create ending time variable
    test_time = datetime.time(hour, minute) #20:00:00, datetime.time object
    test_delta = datetime.timedelta(hours=test_time.hour, minutes=test_time.minute, seconds=test_time.second)

    a = type(test_time)

    # subtract current time from ending time
    difference_delta = test_delta - current_delta

    # transform difference to seconds
    difference_delta.total_seconds()
    return difference_delta.total_seconds()


driver = Driver(uc=True)

driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=AXo7B7WX_wrivAACh0TAbFpPcdmqaKlnznwQGhVeKNaBo5S1BJARBkliHBJJ4CI_tMdwEoRrRpjK_w&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1275157963%3A1691870213375590')
time.sleep(5)

# Type gmail
write("id", 'identifierId', "ovicenteferran", 3)

# Click on "Next"
click_on("css",  "#identifierNext .VfPpkd-dgl2Hf-ppHlrf-sM5MNb .lw1w4b", 3)

# Enter password
password = driver.find_element(By.CLASS_NAME, "zHQkBf")
password.send_keys("Qy>c7),R")
time.sleep(3)

# Click on "Next"
click_on("css", "#passwordNext .VfPpkd-dgl2Hf-ppHlrf-sM5MNb .VfPpkd-LgbsSe", 5)

# go to google meet website
driver.get("https://meet.google.com/")
time.sleep(5)

# Click on "Join Meeting" - ok
click_on("id", "i8", 3)

# Enter meeting link
write("id", "i8", "https://meet.google.com/xet-eahi-gnx", 3)

# Click on "Join"
click_on("css", ".KOM0mb .VfPpkd-dgl2Hf-ppHlrf-sM5MNb .VfPpkd-LgbsSe", 5)

# Click on deny access
click_on("css", ".nMIz8e .VfPpkd-dgl2Hf-ppHlrf-sM5MNb .ksBjEc", 5)

# Click on "Ask to join" | the following waiting time should: ending time - current time
click_on("css", ".XCoPyb .VfPpkd-dgl2Hf-ppHlrf-sM5MNb .nCP5yc", 60)
# ps: HTML returns hh:mm time values
"""
starting_time = "14:30"

hour = int(starting_time[0] + starting_time[1]) #14 (int)
minutes = int(starting_time[3] + starting_time[4]) #30 (int)


ending_time = "10:34"

finish_hour = int(ending_time[0] + ending_time[1]) #10 (int)
finish_minutes = int(ending_time[3] + ending_time[4]) #34 (int)


