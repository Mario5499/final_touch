from selenium.webdriver.common.by import By
import os
from selenium.common.exceptions import NoSuchElementException
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from all_git_passes import userid, passid , gitid, gitpass, gitdashboard, gitnew, gitprofie, gitreponame, giturl, gitlogurl, gitblankfile, docke1, dokereponame, workflowname, crreateanewblankworkflow, newfie, newfiereponame, workingflow
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import re
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"  # Path to the Chromium binary
options.add_argument("--headless")  # Run in headless mode (optional)
options.add_argument("--no-sandbox")  # Disable sandboxing
options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage
options.add_argument("--window-size=1345x610")
driver = webdriver.Chrome(options=options)
driver.set_window_size(1354, 610)
actions = ActionChains(driver)
print("script started")
driver.get("https://account.proton.me/mail")
time.sleep(10)

def kinih (userid,passid):
    global veric
    driver.execute_script("window.open('');") #to open another tab
    driver.switch_to.window(driver.window_handles[1]) #to switch to 2nd tab
    time.sleep(10)


    try:
        # Open the webpage
        driver.get("https://account.proton.me/mail")
    except Exception as e:
        print("Element not found:", str(e))   
    
    driver.find_element("id", "username").send_keys(userid)

    try:
        pasta_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
    except Exception as e:
        print("Element not found:", str(e))
        time.sleep(5)
    pasta_name.send_keys(passid)

    button_xpath = '/html/body/div[1]/div[4]/div[1]/main/div[1]/div[2]/form/button'

    button_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, button_xpath))
        )
    button_element.click()
    time.sleep(60)
    driver.execute_script("window.open('');") #to open another tab
    driver.switch_to.window(driver.window_handles[2]) #to switch to 3nd tab
    time.sleep(10)
    driver.get("https://account.proton.me/mail")
    time.sleep(30)
    cenx = 400
    ceny = 100
    time.sleep(30)
    actions.move_by_offset(0, 0).click().perform()
    actions.move_by_offset(cenx, ceny).click().perform()
    actions.move_by_offset(cenx, ceny).click().perform()
    print("clicker")
    time.sleep(50)

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)

    # Locate the element inside the iframe
    ema = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "proton-root"))
    )
    emx = ema.text

    # Print the email content
    print(emx)
    print("loream break\n")

    # exit iframe code 
    driver.switch_to.default_content()
    match = re.findall(r'\b\d{6}\b', emx)

    if match:
        verio = (f"{match[0]}")
        print("code is:: ", verio)
    else:
        print("no code found")
    time.sleep(10)
    veric = (f"{match[0]}")
    manc = int(veric)
    print(manc)
    driver.close()

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(10)

    driver.find_element("id", "otp").send_keys(manc)
    time.sleep(20)



try:
    # Open the webpage
    driver.get(gitlogurl)
except Exception as e:
    print("Element not found:", str(e))   
time.sleep(30)

driver.find_element("id", "login_field").send_keys(gitid)
time.sleep(25)
driver.find_element("id", "password").send_keys(gitpass)
time.sleep(15)

log_btu = '//*[@id="login"]/div[4]/form/div/input[13]'

bllllo_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, log_btu))
    )
bllllo_element.click()
time.sleep(20)
try:
    king_kilo = driver.find_element("id", "otp")
    time.sleep(5)
    kinih (userid,passid)
except NoSuchElementException:
    print("DEVICE VERIFICATION NOT NEEDED")
    
#further automations
driver.get(gitnew)
time.sleep(30)
#fillo = WebDriverWait(driver, 50).until(
#        EC.presence_of_element_located((By.XPATH, '//*[@id=":r5:"]'))
#   )
try:
    fillo = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=":r5:"]')))
    time.sleep(5)
    fillo.send_keys(gitreponame)
except NoSuchElementException:
    print("error")
#fillo.send_keys(gitreponame)
time.sleep(5)
crtbutton = driver.find_element(By.XPATH, "//button[span/span[text()='Create repository']]")
crtbutton.click()

#dilof = '/html/body/div[1]/div[5]/main/react-app/div/form/div[5]/button'
#sudd = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.XPATH, dilof))
#    )
#sudd.click()
time.sleep(10)
# to create a blank file in a new repository
driver.get(gitblankfile)
time.sleep(10)
#driver.set_window_size(1354, 610)
#cerrix = 500
#creeiy = 320
#actions.move_by_offset(0, 0).click().perform()
#actions.move_by_offset(cerrix, creeiy).click().perform()
#actions.move_by_offset(cerrix, creeiy).click().perform()
#time.sleep(3)
ActionChains(driver).send_keys(docke1).perform()
time.sleep(20)

djrockk = '//*[@id="repo-content-pjax-container"]/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/span[2]/input'
sanataan = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, djrockk))
    )
sanataan.send_keys(dokereponame)

comitbut = '//*[@id="repo-content-pjax-container"]/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/button/span/span'
commiert = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, comitbut))
    )
commiert.click()

comitbut2 = '//*[@id="__primerPortalRoot__"]/div/div/div/div[3]/button[2]/span/span'
             
commiert2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, comitbut2))
    )
commiert2.click()
print("docker created")
time.sleep(10)

driver.get(gitblankfile)
time.sleep(60)
try:
    ActionChains(driver).send_keys(newfie).perform()
    time.sleep(30)
    print("newfie created")
except NoSuchElementException:
    print("error101")
djrock = '//*[@id="repo-content-pjax-container"]/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[2]/span[2]/input'
sanatan = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, djrock))
    )
try:
    sanatan.send_keys(newfiereponame)
    time.sleep(10)
    print("newfie name created")
except:
    print("error10001")
try:
    comitbut = '//*[@id="repo-content-pjax-container"]/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/button'
    commiert = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, comitbut))
        )
    commiert.click()
    print("com1")
except:
    print("com1 error")
time.sleep(5)
try:
    comitbut22 = '//*[@id="__primerPortalRoot__"]/div/div/div/div[3]/button[2]'
    commiert2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, comitbut22))
        )
    commiert2.click()
    print("com2")
except:
    print("com2 error")

driver.get(crreateanewblankworkflow)
#time.sleep(20)
time.sleep(60)
ActionChains(driver).send_keys("name: Docker Image CI").perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
#time.sleep(random.randint(3,10))
ActionChains(driver).send_keys(Keys.ENTER).perform()
#time.sleep(random.randint(3,10))
ActionChains(driver).send_keys("on:").perform()
#time.sleep(random.randint(3,10))
ActionChains(driver).send_keys(Keys.ENTER).perform()
#time.sleep(random.randint(3,10))
ActionChains(driver).send_keys("  push:").perform()
#time.sleep(random.randint(3,10))
ActionChains(driver).send_keys(Keys.ENTER).perform()
#time.sleep(random.randint(3,10))
ActionChains(driver).send_keys('''  branches: [ "main" ]''').perform()
#time.sleep(random.randint(3,10))
ActionChains(driver).send_keys(Keys.ENTER).perform()
#time.sleep(random.randint(3,10))
ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
#time.sleep(random.randint(3,10))
ActionChains(driver).send_keys("pull_request:").perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys('''  branches: [ "main" ]''').perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys("jobs:").perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys("  build-and-run:").perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys("    runs-on: ubuntu-latest").perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys("    steps:").perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys("- name: Checkout code").perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys("  uses: actions/checkout@v4").perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
ActionChains(driver).send_keys("- name: Build the Docker image").perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys("  run: docker build -t my-app .").perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
ActionChains(driver).send_keys("- name: Run the Docker container").perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
ActionChains(driver).send_keys("  run: docker run --rm my-app python3 newtest.py").perform()
time.sleep(20)
try:
    comitbut = '//*[@id="repo-content-pjax-container"]/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/button'
    commiert = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, comitbut))
        )
    commiert.click()
    print("com1")
except:
    print("com1 error")
time.sleep(5)
try:
    comitbut22 = '//*[@id="__primerPortalRoot__"]/div/div/div/div[3]/button[2]'
    commiert2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, comitbut22))
        )
    commiert2.click()
    print("com2")
except:
    print("com2 error")

print("Done Everything You Are Great")

time.sleep(50)
driver.quit()
